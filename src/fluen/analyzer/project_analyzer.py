"""
analyzer/project_analyzer.py
Handles project-level analysis and coordinates file analysis.
"""

from pathlib import Path
from typing import Dict, List, Optional, Set
import asyncio
import logging
from fluen.git_integration.manager import GitManager
from fluen.state.manager import StateManager
from fluen.analyzer.file_analyzer import FileAnalysis, FileAnalyzer
from fluen.generator.manifest import ManifestGenerator

class ProjectAnalyzer:
    def __init__(self, 
                 project_root: Path,
                 git_manager: GitManager,
                 state_manager: StateManager,
                 file_analyzer: FileAnalyzer,
                 manifest_generator: ManifestGenerator):
        self.project_root = project_root
        self.git_manager = git_manager
        self.state_manager = state_manager
        self.file_analyzer = file_analyzer
        self.manifest_generator = manifest_generator
        self.logger = logging.getLogger(__name__)
        
        # Analysis settings
        self.batch_size = 5  # Number of files to analyze concurrently
        self.batch_delay = 2  # Seconds to wait between batches

    async def analyze(self) -> bool:
        """
        Perform full project analysis or incremental update based on git state.
        """
        try:
            # Initialize or load manifest
            state = self.state_manager.load()
            last_commit = state.last_commit
            
            if last_commit:
                # Incremental update
                return await self._perform_incremental_update(last_commit)
            else:
                # Full analysis
                return await self._perform_full_analysis()
        except Exception as e:
            self.logger.error(f"Project analysis failed: {e}")
            return False

    async def _analyze_batch(self, files: List[Path]) -> List[tuple[Path, Optional['FileAnalysis']]]:
        """Analyze a batch of files with rate limiting."""
        tasks = []
        results = []
        
        for file_path in files:
            task = self._analyze_file(file_path)
            tasks.append(task)
        
        # Process batch with rate limiting
        for completed in asyncio.as_completed(tasks):
            try:
                result = await completed
                if result:
                    results.append(result)
            except Exception as e:
                self.logger.error(f"Batch analysis error: {e}")
        
        return results

    async def _perform_full_analysis(self) -> bool:
        """Perform full project analysis with batching."""
        try:
            current_commit = self.git_manager.get_current_commit()
            
            # Initialize manifest
            self.manifest_generator.initialize_manifest(
                project_name=self.project_root.name,
                git_commit=current_commit
            )
            
            # Get analyzable files
            files_to_analyze = list(self._get_analyzable_files())
            total_files = len(files_to_analyze)
            
            if total_files == 0:
                self.logger.warning("No files to analyze")
                return False
            
            self.state_manager.update_progress(0, total_files)
            
            # Process files in batches
            processed_count = 0
            for i in range(0, total_files, self.batch_size):
                batch = files_to_analyze[i:i + self.batch_size]
                
                # Process batch
                results = await self._analyze_batch(batch)
                
                # Update manifest with results
                for file_path, analysis in results:
                    if analysis:
                        relative_path = str(file_path.relative_to(self.project_root))
                        self.manifest_generator.add_file_analysis(analysis, relative_path)
                
                # Update progress
                processed_count += len(batch)
                self.state_manager.update_progress(processed_count, total_files)
                
                # Rate limiting delay between batches
                if i + self.batch_size < total_files:
                    await asyncio.sleep(self.batch_delay)
            
            # Save final manifest
            if self.manifest_generator.save():
                self.state_manager.update_commit(current_commit)
                return True
                
            return False
            
        except Exception as e:
            self.logger.error(f"Full analysis failed: {e}")
            return False

    async def _perform_incremental_update(self, last_commit: str) -> bool:
        """Perform incremental update based on git changes."""
        try:
            current_commit = self.git_manager.get_current_commit()
            changes = self.git_manager.get_changes_since_commit(last_commit)
            
            # Load existing manifest
            if not self.manifest_generator.load_existing_manifest():
                self.logger.warning("Failed to load existing manifest, performing full analysis")
                return await self._perform_full_analysis()
            
            # Analyze changed files
            files_to_analyze = set(changes.added_files + changes.modified_files)
            total_files = len(files_to_analyze)
            
            self.state_manager.update_progress(0, total_files)
            
            # Process changed files
            analysis_tasks = []
            for file_path in files_to_analyze:
                task = self._analyze_file(Path(file_path))
                analysis_tasks.append(task)
            
            # Handle results
            for i, task in enumerate(asyncio.as_completed(analysis_tasks)):
                try:
                    result = await task
                    if result:
                        file_path, analysis = result
                        relative_path = str(file_path.relative_to(self.project_root))
                        self.manifest_generator.add_file_analysis(analysis, relative_path)
                except Exception as e:
                    self.logger.error(f"Failed to process incremental analysis result: {e}")
                
                self.state_manager.update_progress(i + 1, total_files)
            
            # Remove deleted files from manifest
            for deleted_file in changes.deleted_files:
                if deleted_file in self.manifest_generator.manifest.files:
                    del self.manifest_generator.manifest.files[deleted_file]
            
            # Save updated manifest
            if self.manifest_generator.save():
                self.state_manager.update_commit(current_commit)
                return True
                
            return False
            
        except Exception as e:
            self.logger.error(f"Incremental update failed: {e}")
            return False

    def _get_analyzable_files(self) -> Set[Path]:
        """Get list of files that should be analyzed."""
        ignore_patterns = {
            '*.pyc', '__pycache__', '*.git*', '*.env*', 
            'venv', 'node_modules', 'build', 'dist'
        }
        
        files = set()
        for file_path in self.project_root.rglob('*'):
            if file_path.is_file():
                # Check if file should be ignored
                if any(file_path.match(pattern) for pattern in ignore_patterns):
                    continue
                files.add(file_path)
        
        return files

    async def _analyze_file(self, file_path: Path) -> Optional[tuple[Path, 'FileAnalysis']]:
        """Analyze a single file."""
        try:
            analysis = await self.file_analyzer.analyze_file(file_path)
            if analysis:
                return (file_path, analysis)
        except Exception as e:
            self.logger.error(f"Failed to analyze file {file_path}: {e}")
        return None
