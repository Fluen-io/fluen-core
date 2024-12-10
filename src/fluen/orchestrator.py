"""
orchestrator.py
Main orchestrator for the documentation generation process.
"""

import asyncio
from pathlib import Path
from typing import Optional
import logging
import time
from fluen.models.scan import ScanOptions, ScanSelector
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

    async def generate_documentation(self, 
                                   repo_url: Optional[str] = None,
                                   scan_options: Optional[ScanOptions] = None) -> bool:
        """Main documentation generation process."""
        try:
            with Progress(
                SpinnerColumn(),
                TextColumn("[progress.description]{task.description}"),
                BarColumn(),
                TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
                console=self.console,
                expand=True,
                transient=False  # Keep finished tasks visible
            ) as progress:
                # Single overall progress task
                overall_task = progress.add_task(
                    "[cyan]Generating documentation...",
                    total=100
                )

                # Initialize repository (10% of progress)
                progress.update(overall_task, description="[cyan]Initializing repository...")
                if not await self._initialize_repository(repo_url):
                    progress.update(
                        overall_task,
                        description="[red]Repository initialization failed!",
                        completed=100
                    )
                    return False
                progress.update(overall_task, completed=10)

                # Initialize components for analysis
                manifest_generator = ManifestGenerator(
                    Path(self.git_manager.repo_path),
                    self.config.output_dir,
                    llm_provider=self._create_llm_provider()
                )
                
                file_analyzer = FileAnalyzer(self._create_llm_provider())
                
                # Setup project analyzer with progress callback (80% of progress)
                progress.update(overall_task, description="[cyan]Analyzing codebase...")
                
                def analysis_progress(current: int, total: int):
                    if total > 0:
                        # Scale progress to fit in the 10-90 range (80% of total)
                        percentage = (current / total * 80) + 10
                        progress.update(overall_task, completed=percentage)

                project_analyzer = ProjectAnalyzer(
                    Path(self.git_manager.repo_path),
                    self.git_manager,
                    self.state_manager,
                    file_analyzer,
                    manifest_generator,
                    progress_callback=analysis_progress
                )

                # Run analysis based on scan options
                analysis_success = False
                if scan_options and scan_options.is_selective_scan:
                    analysis_success = await project_analyzer.analyze_path(
                        Path(scan_options.selector.value),
                        force=scan_options.selector.force
                    )
                else:
                    force = scan_options.selector.force if scan_options else False
                    analysis_success = await project_analyzer.analyze(force=force)

                if not analysis_success:
                    progress.update(
                        overall_task,
                        description="[red]Analysis failed!",
                        completed=100
                    )
                    return False

                # Update progress for successful analysis
                progress.update(
                    overall_task,
                    description="[green]Analysis complete! Documentation manifest generated and saved.",
                    completed=100
                )

                self.console.print("\n✨ Documentation generation complete!")
                self.console.print(f"📚 Manifest output directory: {self.config.output_dir}")
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

    async def _run_selective_analysis(self,
                                    analyzer: ProjectAnalyzer,
                                    selector: ScanSelector,
                                    progress: Progress,
                                    task_id: TaskID) -> bool:
        """Run selective analysis based on scan selector."""
        try:
            if selector.is_path_selector:
                force = getattr(selector, 'force', False)  # Get force flag from selector
                return await analyzer.analyze_path(
                    Path(selector.value),
                    force=force
                )
            elif selector.is_element_selector:
                self.logger.warning("Element-based scanning not yet implemented")
                return False
            return False
        except Exception as e:
            self.logger.error(f"Selective analysis failed: {e}")
            return False
    
    async def _generate_docs(self,
                           manifest: 'ProjectManifest',
                           progress: Progress,
                           task_id: TaskID) -> bool:
        """Generate documentation from manifest."""
        try:
            # Initialize cross-reference resolver
            cross_referencer = CrossReferenceResolver(manifest)
            manifest_generator = ManifestGenerator(
                    Path(self.git_manager.repo_path),
                    self.config.output_dir
                )
            manifest_generator.load_existing_manifest()

            # Initialize documentation generator
            doc_generator = DocumentationGenerator(
                manifest,
                self.config.output_dir,
                self.template_manager,
                manifest_generator=manifest_generator
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