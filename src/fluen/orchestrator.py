"""
orchestrator.py
Main orchestrator for the documentation generation process.
"""

import asyncio
from pathlib import Path
from typing import Optional
import logging
import time
from fluen.llm_providers.base_provider import BaseLLMProvider
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TaskID

from fluen.config import FluenConfig
from fluen.git_integration.manager import GitManager
from fluen.state.manager import StateManager
from fluen.analyzer.file_analyzer import FileAnalyzer
from fluen.analyzer.project_analyzer import ProjectAnalyzer
from fluen.generator.manifest import ManifestGenerator, ProjectManifest
from fluen.generator.doc_generator import DocumentationGenerator
from fluen.generator.templates.template_manager import TemplateManager
from fluen.generator.cross_referencer import CrossReferenceResolver

class Orchestrator:
    def __init__(self, config: FluenConfig):
        self.config = config
        self.console = Console()
        self.logger = logging.getLogger(__name__)
        
        # Initialize components
        self.git_manager = GitManager()
        self.state_manager = StateManager(self.config.cache_dir)
        self.template_manager = TemplateManager()

    async def generate_documentation(self, repo_url: Optional[str] = None) -> bool:
        """Main documentation generation process."""
        try:
            with Progress(
                SpinnerColumn(),
                TextColumn("[progress.description]{task.description}"),
                BarColumn(),
                TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
                console=self.console
            ) as progress:
                # Initialize repository
                init_task = progress.add_task("Initializing repository...", total=None)
                if not await self._initialize_repository(repo_url):
                    return False
                progress.remove_task(init_task)

                # Initialize components
                analyze_task = progress.add_task("Analyzing codebase...", total=100)
                
                manifest_generator = ManifestGenerator(
                    self.git_manager.repo_path,
                    self.config.output_dir
                )
                
                file_analyzer = FileAnalyzer(self._create_llm_provider())
                
                project_analyzer = ProjectAnalyzer(
                    Path(self.git_manager.repo_path),
                    self.git_manager,
                    self.state_manager,
                    file_analyzer,
                    manifest_generator
                )

                # Analyze project
                if not await self._run_analysis(project_analyzer, progress, analyze_task):
                    return False

                # Generate documentation
                doc_task = progress.add_task("Generating documentation...", total=100)
                if not await self._generate_docs(manifest_generator.manifest, progress, doc_task):
                    return False

                self.console.print("\n✨ Documentation generated successfully!")
                return True

        except Exception as e:
            self.logger.error(f"Documentation generation failed: {e}")
            self.console.print(f"\n❌ Error: {str(e)}")
            return False

    async def _initialize_repository(self, repo_url: Optional[str]) -> bool:
        """Initialize the git repository."""
        try:
            if repo_url:
                target_path = self.config.temp_dir / "repo"
                return await self.git_manager.clone(repo_url, target_path)
            else:
                return self.git_manager.initialize()
        except Exception as e:
            self.logger.error(f"Repository initialization failed: {e}")
            return False

    async def _run_analysis(self, 
                          analyzer: ProjectAnalyzer,
                          progress: Progress,
                          task_id: TaskID) -> bool:
        """Run the project analysis."""
        try:
            def update_progress(current: int, total: int):
                progress.update(task_id, completed=current, total=total)

            # Register progress callback
            self.state_manager.on_progress = update_progress
            
            # Run analysis
            return await analyzer.analyze()
        except Exception as e:
            self.logger.error(f"Analysis failed: {e}")
            return False

    async def _generate_docs(self,
                           manifest: 'ProjectManifest',
                           progress: Progress,
                           task_id: TaskID) -> bool:
        """Generate documentation from manifest."""
        try:
            # Initialize cross-reference resolver
            cross_referencer = CrossReferenceResolver(manifest)
            
            # Initialize documentation generator
            doc_generator = DocumentationGenerator(
                manifest,
                self.config.output_dir,
                self.template_manager
            )
            
            # Generate documentation
            progress.update(task_id, completed=10)
            success = await doc_generator.generate(self.config.default_export_type)
            progress.update(task_id, completed=100)
            
            return success
        except Exception as e:
            self.logger.error(f"Documentation generation failed: {e}")
            return False

    def _create_llm_provider(self) -> 'BaseLLMProvider':
        """Create LLM provider instance."""
        from .llm_factory import LLMProviderFactory
        return LLMProviderFactory.create(
            self.config.llm.provider,
            vars(self.config.llm)
        )

class ProcessManager:
    @staticmethod
    async def run(config_path: Path) -> bool:
        """Run the documentation generation process."""
        # Load configuration
        config = FluenConfig.load(config_path)
        
        # Create and run orchestrator
        orchestrator = Orchestrator(config)
        return await orchestrator.generate_documentation()

def main():
    """CLI entry point."""
    import sys
    
    config_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path('fluen_config.yml')
    
    asyncio.run(ProcessManager.run(config_path))

if __name__ == '__main__':
    main()