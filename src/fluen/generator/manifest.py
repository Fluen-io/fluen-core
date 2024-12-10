"""
generator/manifest.py
Enhanced manifest generator with relationship tracking and JSONP support.
"""

from pathlib import Path
from typing import Dict, List, Any, Optional, Set
from dataclasses import dataclass, asdict
import json
import logging
from datetime import datetime

from fluen.analyzer.file_analyzer import FileAnalysis
from fluen.analyzer.manifest_enricher import ManifestEnricher
from fluen.llm_providers.base_provider import BaseLLMProvider

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
    purpose: Optional[str] = None
    documentation: Optional[str] = None

@dataclass
class FileRelationships:
    dependencies: List[str]  # Files this file depends on
    dependents: List[str]   # Files that depend on this file
    imports: List[str]      # Direct import statements
    imported_by: List[str]  # Files that import this file

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
    relationships: FileRelationships

@dataclass
class ArchitectureInsights:
    """Represents architectural insights about the project"""
    summary: str
    primary_components: List[Dict[str, str]]

@dataclass
class ProjectInsights:
    """Represents enriched project insights from LLM analysis"""
    overview: str
    key_features: List[str]
    architecture: ArchitectureInsights
    code_organization: str
    tech_stack_analysis: str

@dataclass
class ProjectManifest:
    """Represents the complete project documentation manifest."""
    name: str
    root_path: str
    primary_language: str
    frameworks: List[str]
    files: Dict[str, FileManifest]
    dependencies: Dict[str, DependencyInfo]
    last_updated: str
    git_commit: str
    project_insights: Optional[ProjectInsights] = None  # Make it optional for backward compatibility

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'ProjectManifest':
        """Create a ProjectManifest instance from a dictionary."""
        # Handle project insights if present
        project_insights = None
        if 'project_insights' in data:
            insights_data = data['project_insights']
            architecture = ArchitectureInsights(
                summary=insights_data['architecture']['summary'],
                primary_components=insights_data['architecture']['primary_components']
            )
            project_insights = ProjectInsights(
                overview=insights_data['overview'],
                key_features=insights_data['key_features'],
                architecture=architecture,
                code_organization=insights_data['code_organization'],
                tech_stack_analysis=insights_data['tech_stack_analysis']
            )

        # Create FileManifest objects
        files = {
            path: FileManifest(**file_data) if isinstance(file_data, dict) else file_data
            for path, file_data in data['files'].items()
        }

        # Create DependencyInfo objects
        dependencies = {
            name: DependencyInfo(**dep_data) if isinstance(dep_data, dict) else dep_data
            for name, dep_data in data['dependencies'].items()
        }

        return cls(
            name=data['name'],
            root_path=data['root_path'],
            primary_language=data['primary_language'],
            frameworks=data['frameworks'],
            files=files,
            dependencies=dependencies,
            last_updated=data['last_updated'],
            git_commit=data['git_commit'],
            project_insights=project_insights
        )

class ManifestGenerator:
    def __init__(self, project_root: Path, output_dir: Path, llm_provider: Optional['BaseLLMProvider'] = None):
        self.project_root = project_root
        self.output_dir = output_dir
        self.manifest_path = output_dir / "manifest.json"
        # JSONP file should go in the html/assets directory
        self.manifest_jsonp_path = output_dir / "html" / "assets" / "manifest.jsonp"
        self.logger = logging.getLogger(__name__)
        self.manifest: Optional[ProjectManifest] = None
        self.relationship_graph: Dict[str, FileRelationships] = {}
        self.enricher = ManifestEnricher(llm_provider) if llm_provider else None

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
        """Add or update a file analysis in the manifest with relationship tracking."""
        if not self.manifest:
            raise ValueError("Manifest not initialized")

        # Initialize relationships for this file
        relationships = FileRelationships(
            dependencies=[],
            dependents=[],
            imports=file_analysis.dependencies,
            imported_by=[]
        )

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
                    line_number=0
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
                    purpose=elem.purpose,
                    documentation=elem.documentation,
                    file_path=relative_path,
                    line_number=elem.line_number,
                    scope=elem.scope
                ) for elem in file_analysis.elements
            ],
            framework_hints=file_analysis.framework_hints,
            last_modified=datetime.utcnow().isoformat(),
            relationships=relationships
        )

        # Update manifest
        self.manifest.files[relative_path] = file_manifest
        
        # Update project-level information
        self._update_project_information(file_manifest)
        
        # Update relationship tracking
        self._update_relationships(relative_path, file_analysis.dependencies)

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
            dep_name = dep.name if hasattr(dep, 'name') else dep
            if dep_name not in self.manifest.dependencies:
                self.manifest.dependencies[dep_name] = DependencyInfo(**dep) if isinstance(dep, dict) else dep
            else:
                # Update existing dependency usage
                ex_dep = self.manifest.dependencies[dep_name]
                existing_dep = DependencyInfo(**ex_dep) if isinstance(ex_dep, dict) else ex_dep
                if not existing_dep.used_by:
                    existing_dep.used_by = []
                if file_manifest.path not in existing_dep.used_by:
                    existing_dep.used_by.append(file_manifest.path)

    def _update_relationships(self, file_path: str, dependencies: List[str]):
        """Update the relationship graph with new file dependencies."""
        # Initialize relationships for this file if not exists
        if file_path not in self.relationship_graph:
            self.relationship_graph[file_path] = FileRelationships([], [], [], [])
        
        # Get all Python files that import this file
        file_without_ext = file_path.replace('.py', '')
        importable_names = [
            file_without_ext,
            file_without_ext.replace('/', '.'),
            Path(file_path).stem
        ]
        
        # Find all files that might be importing this file
        for other_file, other_manifest in self.manifest.files.items():
            if other_file == file_path:
                continue

            dependencies = []
            if isinstance(other_manifest, dict):
                dependencies = other_manifest.get('dependencies', [])
            else:
                dependencies = getattr(other_manifest, 'dependencies', [])

            # Check if other file imports this file
            for dep in dependencies:
                if isinstance(dep, DependencyInfo):
                    dep_name = dep.name
                elif isinstance(dep, dict):
                    dep_name = dep.get('name', '')
                else:
                    dep_name = str(dep)
                if any(name in dep_name for name in importable_names):
                    if other_file not in self.relationship_graph[file_path].imported_by:
                        self.relationship_graph[file_path].imported_by.append(other_file)
                        
                    # Add reverse relationship
                    if other_file not in self.relationship_graph:
                        self.relationship_graph[other_file] = FileRelationships([], [], [], [])
                    if file_path not in self.relationship_graph[other_file].imports:
                        self.relationship_graph[other_file].imports.append(file_path)

    def _resolve_dependencies(self, file_path: str, dependencies: List[str]) -> List[str]:
        """Resolve relative imports to actual file paths."""
        resolved = []
        file_dir = Path(file_path).parent
        
        for dep in dependencies:
            if dep.startswith('.'):
                # Handle relative imports
                try:
                    resolved_path = str((file_dir / dep).resolve().relative_to(self.project_root))
                    if resolved_path in self.manifest.files:
                        resolved.append(resolved_path)
                except (ValueError, RuntimeError):
                    self.logger.warning(f"Could not resolve relative import: {dep}")
            else:
                # Handle absolute imports within project
                potential_paths = [
                    f"{dep.replace('.', '/')}.py",
                    f"{dep.replace('.', '/')}/__init__.py"
                ]
                for path in potential_paths:
                    if path in self.manifest.files:
                        resolved.append(path)
                        break
        
        return resolved

    def get_file_relationships(self, file_path: str) -> Dict[str, Any]:
        """Get relationship data for a specific file."""
        if file_path not in self.relationship_graph:
            # Return minimal graph with just the current file
            return {
                "nodes": [{"id": file_path, "type": "current"}],
                "links": []
            }
        
        rels = self.relationship_graph[file_path]
        nodes = []
        links = []
        
        # Add current file
        nodes.append({
            "id": self._get_display_name(file_path),
            "type": "current",
            "fullPath": file_path
        })
        
        # Add imports (dependencies)
        for imp in rels.imports:
            nodes.append({
                "id": self._get_display_name(imp),
                "type": "dependency",
                "fullPath": imp
            })
            links.append({
                "source": self._get_display_name(file_path),
                "target": self._get_display_name(imp),
                "type": "dependency"
            })
        
        # Add imported_by (dependents)
        for dep in rels.imported_by:
            nodes.append({
                "id": self._get_display_name(dep),
                "type": "dependent",
                "fullPath": dep
            })
            links.append({
                "source": self._get_display_name(dep),
                "target": self._get_display_name(file_path),
                "type": "reference"
            })
        
        # Remove duplicate nodes
        nodes = [dict(t) for t in {tuple(d.items()) for d in nodes}]
        
        return {
            "nodes": nodes,
            "links": links
        }
    
    def _get_display_name(self, file_path: str) -> str:
        """Get a shorter display name for a file path."""
        return Path(file_path).stem

    async def save(self) -> bool:
        """Save the current manifest to file with enrichments if LLM provider available."""
        try:
            if not self.manifest:
                raise ValueError("No manifest to save")

            self.manifest.last_updated = datetime.utcnow().isoformat()
            
            # Convert manifest to dictionary
            manifest_dict = asdict(self.manifest)
            
            # Enrich manifest if LLM provider is available
            if self.enricher:
                try:
                    manifest_dict = await self.enricher.enrich_manifest(manifest_dict)
                except Exception as e:
                    self.logger.error(f"Failed to enrich manifest: {e}")
                    # Continue with un-enriched manifest
            
            self.manifest_path.parent.mkdir(parents=True, exist_ok=True)
            self.manifest_jsonp_path.parent.mkdir(parents=True, exist_ok=True)

            # Save standard JSON
            with open(self.manifest_path, 'w') as f:
                json.dump(manifest_dict, f, indent=2)
            
            # Save JSONP version with a proper callback
            with open(self.manifest_jsonp_path, 'w') as f:
                f.write(f"window.loadDocumentationManifest({json.dumps(manifest_dict, indent=2)});")
            
            return True
        except Exception as e:
            self.logger.error(f"Failed to save manifest: {e}")
            return False
