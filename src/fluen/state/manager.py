"""
state/manager.py
Manages the state of documentation generation process.
"""

import json
from pathlib import Path
from dataclasses import dataclass, asdict
from typing import Optional, Dict, Any
import logging

@dataclass
class DocumentationState:
    last_commit: Optional[str] = None
    last_run_timestamp: Optional[float] = None
    files_processed: int = 0
    total_files: int = 0
    manifest_path: Optional[str] = None

class StateManager:
    def __init__(self, state_dir: Path):
        self.state_file = state_dir / "state.json"
        self.logger = logging.getLogger(__name__)
        self.current_state = DocumentationState()

    def load(self) -> DocumentationState:
        """Load state from file."""
        try:
            if self.state_file.exists():
                with open(self.state_file, 'r') as f:
                    data = json.load(f)
                    self.current_state = DocumentationState(**data)
            return self.current_state
        except Exception as e:
            self.logger.error(f"Failed to load state: {e}")
            return DocumentationState()

    def save(self) -> bool:
        """Save current state to file."""
        try:
            self.state_file.parent.mkdir(parents=True, exist_ok=True)
            with open(self.state_file, 'w') as f:
                json.dump(asdict(self.current_state), f, indent=2)
            return True
        except Exception as e:
            self.logger.error(f"Failed to save state: {e}")
            return False

    def update_progress(self, files_processed: int, total_files: int):
        """Update documentation progress."""
        self.current_state.files_processed = files_processed
        self.current_state.total_files = total_files
        self.save()

    def update_commit(self, commit_hash: str):
        """Update last processed commit."""
        self.current_state.last_commit = commit_hash
        self.save()

    def set_manifest_path(self, path: str):
        """Set the path to the generated manifest file."""
        self.current_state.manifest_path = path
        self.save()
