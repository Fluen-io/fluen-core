"""
tests/test_git_manager.py
Tests for the Git management functionality
"""

import pytest
from pathlib import Path
from git_integration.manager import GitManager, GitDiff

def test_git_manager_initialization(sample_repo: Path):
    """Test GitManager initialization with existing repository."""
    manager = GitManager(str(sample_repo))
    assert manager.initialize() is True
    assert manager.repo is not None

def test_get_current_commit(sample_repo: Path):
    """Test getting current commit hash."""
    manager = GitManager(str(sample_repo))
    manager.initialize()
    
    commit_hash = manager.get_current_commit()
    assert isinstance(commit_hash, str)
    assert len(commit_hash) == 40  # SHA-1 hash length

def test_get_file_content(sample_repo: Path):
    """Test retrieving file content."""
    manager = GitManager(str(sample_repo))
    manager.initialize()
    
    content = manager.get_file_content("main.py")
    assert content is not None
    assert "hello_world" in content
    assert "TestClass" in content

def test_get_changes_since_commit(sample_repo: Path):
    """Test getting changes between commits."""
    manager = GitManager(str(sample_repo))
    manager.initialize()
    
    # Get initial commit
    initial_commit = manager.get_current_commit()
    
    # Make changes
    (sample_repo / "new_file.py").write_text("print('new')")
    (sample_repo / "main.py").write_text("print('modified')")
    manager.repo.index.add("*")
    manager.repo.index.commit("Second commit")
    
    # Get changes
    changes = manager.get_changes_since_commit(initial_commit)
    assert isinstance(changes, GitDiff)
    assert "new_file.py" in changes.added_files
    assert "main.py" in changes.modified_files