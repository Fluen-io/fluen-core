"""
tests/conftest.py
PyTest configuration and shared fixtures
"""

import pytest
from pathlib import Path
import tempfile
import shutil
import git
from typing import Generator

from config import FluenConfig, LLMConfig

@pytest.fixture
def temp_dir() -> Generator[Path, None, None]:
    """Provide a temporary directory for tests."""
    with tempfile.TemporaryDirectory() as tmp_dir:
        yield Path(tmp_dir)

@pytest.fixture
def sample_repo(temp_dir: Path) -> Generator[Path, None, None]:
    """Create a sample git repository for testing."""
    repo_dir = temp_dir / "sample_repo"
    repo_dir.mkdir()
    
    # Initialize git repo
    repo = git.Repo.init(repo_dir)
    
    # Create sample files
    (repo_dir / "main.py").write_text("""
def hello_world():
    \"\"\"Sample function for testing\"\"\"
    print("Hello, World!")

class TestClass:
    \"\"\"Sample class for testing\"\"\"
    def method(self):
        return "test"
    """)
    
    (repo_dir / "utils.py").write_text("""
from typing import Any

def utility_function(param: Any) -> Any:
    \"\"\"Utility function for testing\"\"\"
    return param
    """)
    
    # Create subdirectory with files
    lib_dir = repo_dir / "lib"
    lib_dir.mkdir()
    (lib_dir / "__init__.py").touch()
    (lib_dir / "helper.py").write_text("""
def helper_function():
    \"\"\"Helper function for testing\"\"\"
    return "help"
    """)
    
    # Add and commit files
    repo.index.add("*")
    repo.index.commit("Initial commit")
    
    yield repo_dir

@pytest.fixture
def mock_config(temp_dir: Path) -> FluenConfig:
    """Create a mock configuration for testing."""
    return FluenConfig(
        llm=LLMConfig(
            provider="openai",
            api_key="test-key",
            model="gpt-3.5-turbo"
        ),
        output_dir=temp_dir / "docs",
        cache_dir=temp_dir / ".fluen/cache",
        temp_dir=temp_dir / ".fluen/temp",
        default_export_type="html"
    )