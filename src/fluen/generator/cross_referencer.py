"""
generator/cross_referencer.py
Handles cross-referencing between documentation elements.
"""

from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple
from dataclasses import dataclass
import re
import logging

from fluen.generator.manifest import ElementReference, ProjectManifest

@dataclass
class Reference:
    source_file: str
    target_file: str
    element_name: str
    element_type: str
    line_number: int

class CrossReferenceResolver:
    def __init__(self, manifest: 'ProjectManifest'):
        self.manifest = manifest
        self.logger = logging.getLogger(__name__)
        self._reference_map: Dict[str, List[Reference]] = {}
        self._build_reference_map()

    def _build_reference_map(self):
        """Build a map of all referenceable elements."""
        for file_path, file_manifest in self.manifest.files.items():
            # Add exposed elements
            for exposure in file_manifest.exposures:
                self._add_reference(exposure.name, file_path, exposure)
            
            # Add all documented elements
            for element in file_manifest.elements:
                self._add_reference(element.name, file_path, element)

    def _add_reference(self, name: str, file_path: str, element: 'ElementReference'):
        """Add a reference to the map."""
        if name not in self._reference_map:
            self._reference_map[name] = []
        
        self._reference_map[name].append(Reference(
            source_file=file_path,
            target_file=file_path,
            element_name=name,
            element_type=element.type,
            line_number=element.line_number
        ))

    def resolve_references(self, content: str, current_file: str) -> Tuple[str, List[str]]:
        """
        Resolve references in content and return the processed content
        along with a list of unresolved references.
        """
        unresolved = set()
        
        def replace_reference(match) -> str:
            """Replace reference with appropriate link."""
            ref_name = match.group(1)
            references = self._reference_map.get(ref_name, [])
            
            if not references:
                unresolved.add(ref_name)
                return f"`{ref_name}`"
            
            # Find best matching reference
            ref = self._find_best_reference(references, current_file)
            
            # Generate appropriate link
            if ref.source_file == current_file:
                return f"[`{ref_name}`](#{ref_name})"
            else:
                file_path = Path(ref.target_file)
                return f"[`{ref_name}`]({file_path.stem}.html#{ref_name})"
        
        # Replace references in content
        pattern = r'\[\[([^\]]+)\]\]'  # Matches [[reference_name]]
        processed_content = re.sub(pattern, replace_reference, content)
        
        return processed_content, list(unresolved)

    def _find_best_reference(self, references: List[Reference], current_file: str) -> Reference:
        """Find the most appropriate reference from a list of possibilities."""
        # First, try to find a reference in the current file
        for ref in references:
            if ref.source_file == current_file:
                return ref
        
        # If no local reference, return the first one
        return references[0]

    def get_incoming_references(self, file_path: str) -> Dict[str, List[Reference]]:
        """Get all references to elements in the specified file."""
        incoming_refs: Dict[str, List[Reference]] = {}
        
        for name, refs in self._reference_map.items():
            for ref in refs:
                if ref.target_file == file_path:
                    if name not in incoming_refs:
                        incoming_refs[name] = []
                    incoming_refs[name].append(ref)
        
        return incoming_refs

    def get_outgoing_references(self, file_path: str) -> Dict[str, List[Reference]]:
        """Get all references from elements in the specified file."""
        outgoing_refs: Dict[str, List[Reference]] = {}
        
        file_manifest = self.manifest.files.get(file_path)
        if not file_manifest:
            return {}
        
        # Process dependencies
        for dep in file_manifest.dependencies:
            if dep.name in self._reference_map:
                if dep.name not in outgoing_refs:
                    outgoing_refs[dep.name] = []
                outgoing_refs[dep.name].extend(self._reference_map[dep.name])
        
        return outgoing_refs

    def generate_reference_graph(self) -> Dict[str, Set[str]]:
        """Generate a dependency graph of file references."""
        graph: Dict[str, Set[str]] = {}
        
        for file_path in self.manifest.files:
            graph[file_path] = set()
            outgoing = self.get_outgoing_references(file_path)
            
            for refs in outgoing.values():
                for ref in refs:
                    if ref.target_file != file_path:
                        graph[file_path].add(ref.target_file)
        
        return graph