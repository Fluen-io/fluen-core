"""
generator/doc_generator.py
Main documentation generator that coordinates HTML and Markdown generation.
"""

import json
from pathlib import Path
from typing import Dict, Any, Optional, List
import shutil
import logging
from fluen.generator.templates.template_manager import TemplateManager
from fluen.generator.manifest import ManifestGenerator, ProjectManifest, ElementReference

class DocumentationGenerator:
    def __init__(self, 
                 manifest: ProjectManifest,
                 output_dir: Path,
                 template_manager: TemplateManager,
                 manifest_generator: ManifestGenerator):  # Add this parameter
        self.manifest = manifest
        self.output_dir = output_dir
        self.template_manager = template_manager
        self.manifest_generator = manifest_generator  # Store the manifest generator
        self.logger = logging.getLogger(__name__)

    async def generate(self, format_type: str = 'html') -> bool:
        """Generate documentation in specified format."""
        try:
            if not self.manifest or not self.manifest.files:
                self.logger.error("No files to document in manifest")
                return False

            generator = self._get_generator(format_type)
            success = await generator.generate()
            
            if not success:
                self.logger.error("Documentation generation failed")
                return False
                
            self.logger.info("Documentation generation completed successfully")
            return True
            
        except Exception as e:
            self.logger.error(f"Documentation generation failed: {e}")
            return False
    
    def _get_generator(self, format_type: str) -> 'BaseFormatGenerator':
        """Get appropriate format generator."""
        if format_type == 'html':
            return HTMLGenerator(
                self.manifest, 
                self.output_dir, 
                self.template_manager,
                self.manifest_generator  # Pass the manifest generator
            )
        elif format_type == 'md':
            return MarkdownGenerator(self.manifest, self.output_dir, self.template_manager)
        else:
            raise ValueError(f"Unsupported format type: {format_type}")

class BaseFormatGenerator:
    def __init__(self, 
                 manifest: ProjectManifest,
                 output_dir: Path,
                 template_manager: TemplateManager,
                 manifest_generator: Optional[ManifestGenerator] = None):  # Add optional parameter
        self.manifest = manifest
        self.output_dir = output_dir
        self.template_manager = template_manager
        self.manifest_generator = manifest_generator
        self.logger = logging.getLogger(__name__)

    async def generate(self) -> bool:
        """Generate documentation in specific format."""
        raise NotImplementedError()

class HTMLGenerator(BaseFormatGenerator):
    async def generate(self) -> bool:
        """Generate HTML documentation."""
        try:
            # Create output directory structure
            docs_dir = self.output_dir / 'html'
            reference_dir = docs_dir / 'reference'
            assets_dir = docs_dir / 'assets'
            
            docs_dir.mkdir(parents=True, exist_ok=True)
            reference_dir.mkdir(exist_ok=True)
            assets_dir.mkdir(exist_ok=True)

            # Copy static assets
            self._copy_static_assets(assets_dir)

            # Ensure we have files to document
            if not self.manifest.files:
                self.logger.warning("No files to document")
                return self._generate_empty_documentation(docs_dir)

            # Generate index page
            await self._generate_index_page(docs_dir)

            # Generate reference pages
            await self._generate_reference_pages(reference_dir)

            return True

        except Exception as e:
            self.logger.error(f"HTML generation failed: {e}")
            return False

    def _copy_static_assets(self, assets_dir: Path):
        """Copy static assets (CSS, JS) to output directory."""
        static_dir = Path(__file__).parent / 'templates' / 'default' / 'static'
        if static_dir.exists():
            shutil.copytree(static_dir, assets_dir, dirs_exist_ok=True)

    async def _generate_index_page(self, output_dir: Path):
        """Generate main index page."""
        context = self.template_manager.get_default_context(self.manifest)
        context.update({
            'files_by_type': self._group_files_by_type(),
            'dependencies': self.manifest.dependencies,
            'frameworks': self.manifest.frameworks,
            'project_insights': self.manifest.project_insights
        })
        
        content = self.template_manager.render_template('html/index.html', context)
        (output_dir / 'index.html').write_text(content)

    async def _generate_reference_pages(self, reference_dir: Path):
        """Generate individual reference pages with relationship data."""
        for file_path, file_manifest in self.manifest.files.items():
            context = self.template_manager.get_default_context(self.manifest)
            
            # Get relationship data if manifest_generator is available
            relationships = None
            if self.manifest_generator:
                relationships = self.manifest_generator.get_file_relationships(file_path)
            
            context.update({
                'file': file_manifest,
                'elements_by_type': self._group_elements_by_type(file_manifest.get('elements', [])),
                'relationships': relationships,  # Add relationship data to context
            })
            
            # Generate lineage data for JavaScript if relationships exist
            lineage_script = ""
            if relationships:
                lineage_script = f"<script>window.lineageData = {json.dumps(relationships)};</script>"
            
            # Convert file path to a safe filename
            safe_filename = file_path.replace('/', '_').replace('\\', '_')
            output_path = reference_dir / f"{safe_filename}.html"
            
            # Render template
            content = self.template_manager.render_template('html/reference.html', context)
            
            # Insert lineage data script before closing body tag if it exists
            if lineage_script:
                content = content.replace('</body>', f'{lineage_script}</body>')
            
            output_path.write_text(content)

    def _group_files_by_type(self) -> Dict[str, List[str]]:
        """Group files by their language/type."""
        groups = {}
        for file_path, file_manifest in self.manifest.files.items():
            lang = file_manifest.language
            if lang not in groups:
                groups[lang] = []
            groups[lang].append(file_path)
        return groups

    def _group_elements_by_type(self, elements: List['ElementReference']) -> Dict[str, List['ElementReference']]:
        """Group elements by their type."""
        groups = {}
        for element in elements:
            element_type = element.get('type', 'Unknown')
            if element_type not in groups:
                groups[element_type] = []
            groups[element_type].append(element)
        return groups

    def _generate_empty_documentation(self, docs_dir: Path) -> bool:
        """Generate documentation for empty project."""
        try:
            context = self.template_manager.get_default_context(self.manifest)
            context.update({
                'files_by_type': {},
                'dependencies': {},
                'frameworks': [],
                'is_empty': True
            })
            
            content = self.template_manager.render_template('html/empty.html', context)
            (docs_dir / 'index.html').write_text(content)
            return True
        except Exception as e:
            self.logger.error(f"Failed to generate empty documentation: {e}")
            return False
        
    def _group_files_by_type(self) -> Dict[str, List[str]]:
        """Group files by their language/type with safety checks."""
        groups = {}
        if self.manifest and hasattr(self.manifest, 'files'):
            for file_path, file_manifest in self.manifest.files.items():
                
                lang = file_manifest.get('language', 'Unknown')
                if lang not in groups:
                    groups[lang] = []
                groups[lang].append(file_path)
        return groups


class MarkdownGenerator(BaseFormatGenerator):
    async def generate(self) -> bool:
        """Generate Markdown documentation."""
        try:
            # Create output directory structure
            docs_dir = self.output_dir / 'md'
            reference_dir = docs_dir / 'reference'
            
            docs_dir.mkdir(parents=True, exist_ok=True)
            reference_dir.mkdir(exist_ok=True)

            # Generate main README
            await self._generate_readme(docs_dir)

            # Generate reference documents
            await self._generate_reference_docs(reference_dir)

            # Generate summary document
            await self._generate_summary(docs_dir)

            return True

        except Exception as e:
            self.logger.error(f"Markdown generation failed: {e}")
            return False

    async def _generate_readme(self, docs_dir: Path):
        """Generate main README file."""
        context = self.template_manager.get_default_context(self.manifest)
        context.update({
            'files_by_type': self._group_files_by_type(),
            'dependencies': self.manifest.dependencies
        })
        
        content = self.template_manager.render_template('md/readme.md', context)
        (docs_dir / 'README.md').write_text(content)

    async def _generate_reference_docs(self, reference_dir: Path):
        """Generate reference documentation files."""
        for file_path, file_manifest in self.manifest.files.items():
            context = self.template_manager.get_default_context(self.manifest)
            context.update({
                'file': file_manifest,
                'elements_by_type': self._group_elements_by_type(file_manifest.get("elements", []))
            })
            
            # Convert file path to a safe filename
            safe_filename = file_path.replace('/', '_').replace('\\', '_')
            output_path = reference_dir / f"{safe_filename}.md"
            content = self.template_manager.render_template('md/reference.md', context)
            output_path.write_text(content)

    async def _generate_summary(self, docs_dir: Path):
        """Generate SUMMARY.md for navigation."""
        context = self.template_manager.get_default_context(self.manifest)
        context.update({
            'files': self.manifest.files,
            'groups': self._group_files_by_type()
        })
        
        content = self.template_manager.render_template('md/summary.md', context)
        (docs_dir / 'summary.md').write_text(content)

    def _group_files_by_type(self) -> Dict[str, List[str]]:
        """Group files by their language/type with safety checks."""
        groups = {}
        if self.manifest and hasattr(self.manifest, 'files'):
            for file_path, file_manifest in self.manifest.files.items():
                
                lang = file_manifest.get('language', 'Unknown')
                if lang not in groups:
                    groups[lang] = []
                groups[lang].append(file_path)
        return groups

    def _group_elements_by_type(self, elements: List['ElementReference']) -> Dict[str, List['ElementReference']]:
        """Group elements by their type."""
        groups = {}
        for element in elements:
            element_type = element.get('type', 'Unknown')
            if element_type not in groups:
                groups[element_type] = []
            groups[element_type].append(element)
        return groups