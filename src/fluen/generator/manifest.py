"""
generator/manifest.py
Generates and manages the documentation manifest.
"""

from pathlib import Path
from typing import Dict, List, Any, Optional
from dataclasses import dataclass, asdict
import json
import logging
from datetime import datetime

from fluen.analyzer.file_analyzer import FileAnalysis

@dataclass
class DependencyInfo:
    name: str
    type: str  # 'external', 'internal', 'system'
    version: Optional[str] = None
    used_by: List[str] = None  # list of file paths

@dataclass
class ElementReference:
    name: str
    type: str
    file_path: str
    line_number: int
    scope: Optional[str] = None

@dataclass
class FileManifest:
    path: str
    language: str
    purpose: str
    exposures: List[ElementReference]
    dependencies: List[DependencyInfo]
    elements: List[ElementReference]
    framework_hints: List[str]
    last_modified: str

@dataclass
class ProjectManifest:
    name: str
    root_path: str
    primary_language: str
    frameworks: List[str]
    files: Dict[str, FileManifest]
    dependencies: Dict[str, DependencyInfo]
    last_updated: str
    git_commit: str
    
class ManifestGenerator:
    def __init__(self, project_root: Path, output_dir: Path):
        self.project_root = project_root
        self.manifest_path = output_dir / "manifest.json"
        self.logger = logging.getLogger(__name__)
        self.manifest: Optional[ProjectManifest] = None

    def initialize_manifest(self, project_name: str, git_commit: str) -> ProjectManifest:
        """Initialize a new project manifest."""
        self.manifest = ProjectManifest(
            name=project_name,
            root_path=str(self.project_root),
            primary_language="",  # Will be determined later
            frameworks=[],
            files={},
            dependencies={},
            last_updated=datetime.utcnow().isoformat(),
            git_commit=git_commit
        )
        return self.manifest

    def load_existing_manifest(self) -> Optional[ProjectManifest]:
        """Load existing manifest if it exists."""
        try:
            if self.manifest_path.exists():
                data = json.loads(self.manifest_path.read_text())
                self.manifest = ProjectManifest(**data)
                return self.manifest
        except Exception as e:
            self.logger.error(f"Failed to load manifest: {e}")
        return None

    def add_file_analysis(self, file_analysis: 'FileAnalysis', relative_path: str):
        """Add or update a file analysis in the manifest."""
        if not self.manifest:
            raise ValueError("Manifest not initialized")

        # Convert file analysis to manifest format
        file_manifest = FileManifest(
            path=relative_path,
            language=file_analysis.language,
            purpose=file_analysis.purpose,
            exposures=[
                ElementReference(
                    name=exp,
                    type="exposure",
                    file_path=relative_path,
                    line_number=0  # Would need to be provided by analysis
                ) for exp in file_analysis.exposures
            ],
            dependencies=[
                DependencyInfo(
                    name=dep,
                    type="external" if not dep.startswith(".") else "internal"
                ) for dep in file_analysis.dependencies
            ],
            elements=[
                ElementReference(
                    name=elem.name,
                    type=elem.type,
                    file_path=relative_path,
                    line_number=elem.line_number,
                    scope=elem.scope
                ) for elem in file_analysis.elements
            ],
            framework_hints=file_analysis.framework_hints,
            last_modified=datetime.utcnow().isoformat()
        )

        # Update manifest
        self.manifest.files[relative_path] = file_manifest
        
        # Update project-level information
        self._update_project_information(file_manifest)

    def _update_project_information(self, file_manifest: FileManifest):
        """Update project-level information based on file analysis."""
        # Update language statistics (simplified)
        if not self.manifest.primary_language:
            self.manifest.primary_language = file_manifest.language

        # Update framework list
        for framework in file_manifest.framework_hints:
            if framework not in self.manifest.frameworks:
                self.manifest.frameworks.append(framework)

        # Update dependency tracking
        for dep in file_manifest.dependencies:
            if dep.name not in self.manifest.dependencies:
                self.manifest.dependencies[dep.name] = dep
            else:
                # Update existing dependency usage
                existing_dep = self.manifest.dependencies[dep.name]
                if not existing_dep.used_by:
                    existing_dep.used_by = []
                if file_manifest.path not in existing_dep.used_by:
                    existing_dep.used_by.append(file_manifest.path)

    def save(self) -> bool:
        """Save the current manifest to file."""
        try:
            if not self.manifest:
                raise ValueError("No manifest to save")

            self.manifest.last_updated = datetime.utcnow().isoformat()
            self.manifest_path.parent.mkdir(parents=True, exist_ok=True)
            
            with open(self.manifest_path, 'w') as f:
                json.dump(asdict(self.manifest), f, indent=2)
            
            return True
        except Exception as e:
            self.logger.error(f"Failed to save manifest: {e}")
            return False