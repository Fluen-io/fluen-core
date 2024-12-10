"""
src/fluen/generator/templates/template_manager.py
Manages the template system for documentation generation.
"""

from pathlib import Path
from typing import Dict, Any, Optional
from jinja2 import Environment, FileSystemLoader, PackageLoader, ChoiceLoader
from markdown import markdown
import bleach
import logging

from fluen.generator.manifest import ProjectManifest

class TemplateManager:
    def __init__(self, custom_template_dir: Optional[Path] = None):
        self.logger = logging.getLogger(__name__)
        
        # Set up template loaders
        loaders = []
        
        # Add custom templates if provided
        if custom_template_dir:
            loaders.append(FileSystemLoader(custom_template_dir))
            
        # Add default package templates
        loaders.append(PackageLoader('fluen', 'generator/templates/default'))
        
        # Create Jinja environment with the loaders
        self.env = Environment(
            loader=ChoiceLoader(loaders),
            autoescape=True,
            trim_blocks=True,
            lstrip_blocks=True
        )
        
        # Register custom filters
        self._register_filters()

    def _register_filters(self):
        """Register custom template filters."""
        self.env.filters['format_type'] = lambda t: t.replace('_', ' ').title()
        self.env.filters['anchor_id'] = lambda s: s.lower().replace(' ', '-')
        self.env.filters['code_language'] = lambda path: self._detect_language(path)

        # Add markdown filter with safe HTML subset
        def markdown_filter(text):
            # Convert markdown to HTML
            html = markdown(text, extensions=['tables', 'fenced_code'])
            
            # Sanitize HTML output
            allowed_tags = [
                'p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 
                'strong', 'em', 'ul', 'ol', 'li', 'code', 'pre',
                'a', 'table', 'thead', 'tbody', 'tr', 'th', 'td'
            ]
            allowed_attributes = {
                'a': ['href', 'title'],
                'code': ['class'],
                'pre': ['class']
            }
            
            return bleach.clean(
                html,
                tags=allowed_tags,
                attributes=allowed_attributes,
                strip=True
            )
            
        self.env.filters['markdown'] = markdown_filter
        
    def _detect_language(self, path: str) -> str:
        """Detect language for syntax highlighting."""
        extension_map = {
            '.py': 'python',
            '.js': 'javascript',
            '.ts': 'typescript',
            '.java': 'java',
            '.cpp': 'cpp',
            '.hpp': 'cpp',
            '.c': 'c',
            '.h': 'c',
            '.rs': 'rust',
            '.go': 'go',
            '.rb': 'ruby',
            '.php': 'php',
        }
        suffix = Path(path).suffix.lower()
        return extension_map.get(suffix, 'plaintext')

    def render_template(self, template_name: str, context: Dict[str, Any]) -> str:
        """Render a template with given context."""
        try:
            template = self.env.get_template(template_name)
            return template.render(**context)
        except Exception as e:
            self.logger.error(f"Failed to render template {template_name}: {e}")
            raise

    def get_default_context(self, manifest: 'ProjectManifest') -> Dict[str, Any]:
        """Get default context for templates."""
        return {
            'project': {
                'name': manifest.name,
                'primary_language': manifest.primary_language,
                'frameworks': manifest.frameworks,
                'root_path': manifest.root_path
            },
            'generation_time': manifest.last_updated,
            'git_commit': manifest.git_commit
        }
