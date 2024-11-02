"""
git/manager.py
Git repository management and analysis functionality.
"""

import git
from pathlib import Path
from typing import Optional, List, Dict
from dataclasses import dataclass
import logging

@dataclass
class GitDiff:
    """Represents changes between commits"""
    added_files: List[str]
    modified_files: List[str]
    deleted_files: List[str]
    raw_diff: str

class GitManager:
    def __init__(self, repo_path: Optional[str] = None):
        self.repo_path = repo_path or str(Path.cwd())
        self.repo: Optional[git.Repo] = None
        self.logger = logging.getLogger(__name__)

    def initialize(self) -> bool:
        """Initialize git repository connection."""
        try:
            self.repo = git.Repo(self.repo_path)
            return True
        except git.InvalidGitRepositoryError:
            self.logger.error(f"Invalid git repository: {self.repo_path}")
            return False

    def clone(self, url: str, target_path: Path) -> bool:
        """Clone a remote repository."""
        try:
            self.repo = git.Repo.clone_from(url, target_path)
            self.repo_path = str(target_path)
            return True
        except git.GitCommandError as e:
            self.logger.error(f"Failed to clone repository: {e}")
            return False

    def get_current_commit(self) -> str:
        """Get current commit hash."""
        if not self.repo:
            raise ValueError("Repository not initialized")
        return self.repo.head.commit.hexsha

    def get_changes_since_commit(self, since_commit: str) -> GitDiff:
        """Get changes between current HEAD and specified commit."""
        if not self.repo:
            raise ValueError("Repository not initialized")

        diff_index = self.repo.head.commit.diff(since_commit)
        
        added = [d.b_path for d in diff_index if d.new_file]
        modified = [d.a_path for d in diff_index if d.a_path == d.b_path]
        deleted = [d.a_path for d in diff_index if d.deleted_file]
        
        # Get raw diff for content analysis
        raw_diff = self.repo.git.diff(since_commit)
        
        return GitDiff(
            added_files=added,
            modified_files=modified,
            deleted_files=deleted,
            raw_diff=raw_diff
        )

    def get_file_content(self, file_path: str, commit: Optional[str] = None) -> Optional[str]:
        """Get content of a file at specific commit."""
        if not self.repo:
            raise ValueError("Repository not initialized")
        
        try:
            if commit:
                return self.repo.git.show(f"{commit}:{file_path}")
            else:
                file_path = Path(self.repo_path) / file_path
                return file_path.read_text()
        except git.GitCommandError:
            self.logger.error(f"Failed to read file: {file_path}")
            return None
