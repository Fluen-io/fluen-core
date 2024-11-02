"""
tests/test_file_analyzer.py
Tests for the file analysis functionality
"""

import pytest
from pathlib import Path
from unittest.mock import Mock, AsyncMock
from analyzer.file_analyzer import FileAnalyzer, FileAnalysis, CodeElement

@pytest.fixture
def mock_llm_provider():
    """Create a mock LLM provider."""
    provider = Mock()
    provider.generate = AsyncMock(return_value='''
    {
        "purpose": "Test file with sample functions",
        "exposures": ["hello_world", "TestClass"],
        "dependencies": [],
        "elements": [
            {
                "name": "hello_world",
                "type": "function",
                "purpose": "Sample function for testing",
                "documentation": "Prints Hello, World!",
                "line_number": 1
            },
            {
                "name": "TestClass",
                "type": "class",
                "purpose": "Sample class for testing",
                "documentation": "A test class with a method",
                "line_number": 5
            }
        ],
        "framework_hints": []
    }''')
    return provider

@pytest.mark.asyncio
async def test_analyze_file(sample_repo: Path, mock_llm_provider):
    """Test file analysis functionality."""
    analyzer = FileAnalyzer(mock_llm_provider)
    
    # Analyze main.py
    file_path = sample_repo / "main.py"
    analysis = await analyzer.analyze_file(file_path)
    
    assert isinstance(analysis, FileAnalysis)
    assert analysis.language == "Python"
    assert len(analysis.elements) == 2
    assert analysis.elements[0].name == "hello_world"
    assert analysis.elements[1].name == "TestClass"

@pytest.mark.asyncio
async def test_analyze_binary_file(sample_repo: Path, mock_llm_provider):
    """Test that binary files are skipped."""
    # Create a binary file
    binary_file = sample_repo / "binary.bin"
    binary_file.write_bytes(b'\x00\x01\x02\x03')
    
    analyzer = FileAnalyzer(mock_llm_provider)
    analysis = await analyzer.analyze_file(binary_file)
    
    assert analysis is None

@pytest.mark.asyncio
async def test_element_extraction(sample_repo: Path, mock_llm_provider):
    """Test extraction of code elements."""
    analyzer = FileAnalyzer(mock_llm_provider)
    file_path = sample_repo / "main.py"
    analysis = await analyzer.analyze_file(file_path)
    
    # Check function element
    function_element = next(e for e in analysis.elements if e.name == "hello_world")
    assert function_element.type == "function"
    assert function_element.line_number == 1
    
    # Check class element
    class_element = next(e for e in analysis.elements if e.name == "TestClass")
    assert class_element.type == "class"
    assert class_element.line_number == 5