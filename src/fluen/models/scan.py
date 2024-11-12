from pathlib import Path
from typing import Optional

class ScanSelector:
    """Handles parsing and validation of scan selectors."""
    
    def __init__(self, selector: str):
        self.raw_selector = selector
        self.type: str = ""
        self.value: str = ""
        self.force: bool = False  # Add force flag
        self._parse_selector()
    
    def _parse_selector(self):
        """Parse the selector string into type and value."""
        if not self.raw_selector or ':' not in self.raw_selector:
            raise ValueError("Invalid selector format. Use format: type:value")
        
        parts = self.raw_selector.split(':', 1)
        if len(parts) != 2:
            raise ValueError("Invalid selector format. Use format: type:value")
            
        self.type = parts[0].lower()
        self.value = parts[1]
        
        if not self._validate():
            raise ValueError(f"Invalid selector type: {self.type}")
    
    def _validate(self) -> bool:
        """Validate the selector type and value."""
        valid_types = {'path', 'element'}  # Add more types as needed
        return self.type in valid_types
    
    @property
    def is_path_selector(self) -> bool:
        return self.type == 'path'
    
    @property
    def is_element_selector(self) -> bool:
        return self.type == 'element'

class ScanOptions:
    """Container for scan options."""
    
    def __init__(self, selector: Optional[str] = None, force: bool = False):
        self.selector: Optional[ScanSelector] = None
        if selector:
            self.selector = ScanSelector(selector)
            self.selector.force = force  # Add force flag to selector
    
    @property
    def is_selective_scan(self) -> bool:
        return self.selector is not None
