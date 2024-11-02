"""
src/fluen/analyzer/file_analyzer.py
Analyzes individual files for documentation generation with improved filtering and rate limiting.
"""

from pathlib import Path
import re
from typing import Dict, Any, List, Optional
from dataclasses import dataclass
import logging
import mimetypes
import json
import asyncio
import time

from git import Union

from fluen.llm_providers.base_provider import BaseLLMProvider

@dataclass
class CodeElement:
    name: str
    type: str
    purpose: str
    documentation: str
    line_number: int
    scope: Optional[str] = None

@dataclass
class FileAnalysis:
    path: str
    language: str
    purpose: str
    exposures: List[str]
    dependencies: List[str]
    elements: List[CodeElement]
    framework_hints: List[str]

class FileAnalyzer:
    def __init__(self, llm_provider: 'BaseLLMProvider'):
        self.llm = llm_provider
        self.logger = logging.getLogger(__name__)
        mimetypes.init()
        
        # Ignore patterns for files and directories
        self.ignore_patterns = {
            # Git files
            '.git',
            '.gitignore',
            '.gitmodules',
            '.gitattributes',
            
            # Python artifacts
            '__pycache__',
            '*.pyc',
            '*.pyo',
            '*.pyd',
            '.Python',
            '*.egg-info',
            'build',
            'dist',
            
            # Virtual environments
            'venv',
            '.env',
            '.venv',
            'env',
            
            # IDE files
            '.idea',
            '.vscode',
            '*.swp',
            '*.swo',
            
            # Cache directories
            '.pytest_cache',
            '.coverage',
            '.tox',
            
            # Package manager files
            'node_modules',
            'package-lock.json',
            'yarn.lock',
            
            # Documentation output
            'docs',
            'site',
            
            # Temporary files
            '.tmp',
            '.temp',
            '*.log',
        }

    def should_ignore_file(self, file_path: Path) -> bool:
        """Check if file should be ignored based on patterns."""
        # Check each path component against ignore patterns
        for part in file_path.parts:
            if any(part.startswith(pat.strip('*')) for pat in self.ignore_patterns):
                return True
            if any(part.endswith(pat.strip('*')) for pat in self.ignore_patterns):
                return True
        return False
    
    def parse_json(self, response: str) -> Union[Any, Dict[str, str]]:
        """
        Extract and parse a JSON object from an LLM response.
        
        Args:
        response (str): The full response from the LLM.
        
        Returns:
        Any: The parsed JSON object, or an error dictionary if parsing fails.
        """
        # Attempt to directly parse the response as JSON
        parsed_json = self._attempt_parse(response)
        if parsed_json is not None:
            return parsed_json

        # Attempt to extract JSON from markdown-style code blocks or other common patterns
        json_string = self._extract_json_from_response(response)
        if json_string:
            json_string = self._fix_json_syntax(json_string)
            parsed_json = self._attempt_parse(json_string)
            if parsed_json is not None:
                return parsed_json
        
        # If all attempts fail, try to construct a JSON-like structure
        constructed_json = self._construct_json_from_text(response)
        if constructed_json:
            return constructed_json
        
        # If all attempts fail, return an error dictionary with the raw response
        self.logger.error("Failed to parse JSON after all attempts")
        return {
            "error": "Failed to parse JSON",
            "raw_response": response
        }

    def _attempt_parse(self, json_string: str) -> Union[Any, None]:
        """Attempt to parse a string as JSON."""
        try:
            return json.loads(json_string)
        except json.JSONDecodeError:
            return None

    def _extract_json_from_response(self, response: str) -> Union[str, None]:
        """Extract JSON string from different potential formats in the response."""
        # Look for JSON in markdown code block with or without "json" identifier
        json_match = re.search(r'```(?:json)?\s*([\s\S]*?)\s*```', response)
        if json_match:
            self.logger.info("Found JSON in code block")
            return json_match.group(1).strip()
        
        # Look for the first JSON-like structure in the text
        json_match = re.search(r'(\{.*?\}|\[.*?\])', response, re.DOTALL)
        if json_match:
            self.logger.info("Found JSON-like structure in response")
            return json_match.group(1).strip()
        
        self.logger.warning("No JSON structure found in response")
        return None

    def _fix_json_syntax(self, json_string: str) -> str:
        """Fix common JSON syntax errors."""
        # Remove any text after the last closing bracket or brace
        json_string = re.sub(r'([}\]])\s*[^}\]]*$', r'\1', json_string, flags=re.DOTALL)
        
        # Fix missing commas between array elements
        json_string = re.sub(r'(\}\s*\{|\]\s*\[)', r'\1,', json_string)
        
        # Fix trailing commas in arrays and objects
        json_string = re.sub(r',\s*([\]}])', r'\1', json_string)
        
        # Fix unclosed quotes
        json_string = re.sub(r'(?<!\\)"([^"]*?)(?<!\\)"(?=\s*[:,\]}])', r'"\1"', json_string)
        
        # Remove newlines and extra spaces between keys and values
        json_string = re.sub(r'"\s*:\s*"', '":"', json_string)
        json_string = re.sub(r'"\s*:\s*\[', '":[', json_string)
        json_string = re.sub(r'"\s*:\s*\{', '":{', json_string)
        
        return json_string

    def _construct_json_from_text(self, text: str) -> Union[Dict[str, Any], None]:
        """Attempt to construct a JSON-like structure from free text."""
        # Look for key-value pairs in the text
        pairs = re.findall(r'(?:^|\n)(["\w\s]+?):\s*(.+?)(?=\n["\w\s]+?:|$)', text, re.DOTALL)
        if pairs:
            result = {}
            for key, value in pairs:
                key = key.strip().strip('"')
                value = value.strip()
                # Check if value looks like a list
                if value.startswith('[') and value.endswith(']'):
                    try:
                        value = json.loads(value)
                    except json.JSONDecodeError:
                        # If parsing as JSON fails, split by commas and strip whitespace
                        value = [v.strip().strip('"') for v in value[1:-1].split(',')]
                elif value.lower() in ['true', 'false']:
                    value = value.lower() == 'true'
                elif value.isdigit():
                    value = int(value)
                elif value.replace('.', '', 1).isdigit():
                    value = float(value)
                else:
                    value = value.strip('"')
                result[key] = value
            self.logger.info("Constructed JSON-like structure from text")
            return result
        
        self.logger.warning("Failed to construct JSON-like structure from text")
        return None

    async def analyze_file(self, file_path: Path) -> Optional[FileAnalysis]:
        """Analyze a single file with improved error handling."""
        try:
            # Skip ignored files
            if self.should_ignore_file(file_path):
                self.logger.debug(f"Skipping ignored file: {file_path}")
                return None

            # Skip non-text files
            if not self._is_text_file(file_path):
                self.logger.debug(f"Skipping non-text file: {file_path}")
                return None

            # Read file content
            try:
                content = file_path.read_text(encoding='utf-8')
                
                # Handle empty or nearly empty files (like __init__.py)
                if not content.strip():
                    return self._create_empty_analysis(file_path)
                
                # If file is too small, handle it simply
                if len(content.strip().splitlines()) < 5:
                    return self._analyze_simple_file(file_path, content)
                
            except UnicodeDecodeError:
                self.logger.debug(f"Skipping binary file: {file_path}")
                return None

            # Try analysis with rate limit handling
            max_retries = 3
            base_delay = 1.0
            
            for attempt in range(max_retries):
                try:
                    # Get LLM response
                    analysis_result = await self.llm.generate(self._create_analysis_prompt(content))
                    
                    # Parse the response with our robust parser
                    parsed_result = self.parse_json(analysis_result)
                    
                    if "error" in parsed_result:
                        if attempt < max_retries - 1:
                            delay = base_delay * (2 ** attempt)
                            self.logger.warning(f"Parse failed, retrying in {delay}s...")
                            await asyncio.sleep(delay)
                            continue
                        return self._create_basic_analysis(file_path)
                    
                    return self._create_analysis_from_parsed_result(file_path, parsed_result)
                        
                except Exception as e:
                    if 'rate_limit' in str(e).lower():
                        if attempt < max_retries - 1:
                            delay = base_delay * (2 ** attempt)
                            self.logger.warning(f"Rate limit hit, retrying in {delay}s...")
                            await asyncio.sleep(delay)
                            continue
                    raise

        except Exception as e:
            self.logger.error(f"Failed to analyze file {file_path}: {e}")
            return self._create_basic_analysis(file_path)

    def _create_analysis_from_parsed_result(self, file_path: Path, result: Dict[str, Any]) -> FileAnalysis:
        """Create FileAnalysis from parsed JSON result with validation."""
        elements = []
        for elem in result.get('elements', []):
            if isinstance(elem, dict):
                try:
                    elements.append(CodeElement(
                        name=elem.get('name', 'unknown'),
                        type=elem.get('type', 'unknown'),
                        purpose=elem.get('purpose', ''),
                        documentation=elem.get('documentation', ''),
                        line_number=elem.get('line_number', 0),
                        scope=elem.get('scope')
                    ))
                except Exception as e:
                    self.logger.error(f"Failed to create CodeElement: {e}")
                    continue
            else:
                self.logger.warning(f"Invalid element format: {elem}")
                continue

        return FileAnalysis(
            path=str(file_path),
            language=self._detect_language(file_path),
            purpose=result.get('purpose', 'Purpose not specified'),
            exposures=result.get('exposures', []),
            dependencies=result.get('dependencies', []),
            elements=elements,
            framework_hints=result.get('framework_hints', [])
        )

    def _is_text_file(self, file_path: Path) -> bool:
        """Check if file is a text file that should be analyzed."""
        # Known text file extensions
        text_extensions = {
            '.py', '.js', '.ts', '.java', '.cpp', '.hpp', 
            '.c', '.h', '.rs', '.go', '.rb', '.php',
            '.css', '.html', '.xml', '.json', '.yml', '.yaml',
            '.md', '.txt', '.sh', '.bash', '.zsh'
        }
        
        if file_path.suffix.lower() in text_extensions:
            return True
            
        # Try to read as text
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                f.readline()
            return True
        except (UnicodeDecodeError, IOError):
            return False

    def _create_analysis_prompt(self, content: str) -> str:
        """Create prompt for LLM analysis."""
        return f"""Analyze the following code and provide:
1. The primary purpose of this code
2. All exposed elements (public APIs, functions, classes)
3. External dependencies
4. Detailed analysis of each code element (classes, methods, variables)
5. Any frameworks or specific language features used

Code:
{content}

Provide the analysis in the following JSON format:
{{
    "purpose": "brief description",
    "exposures": ["list", "of", "exposed", "elements"],
    "dependencies": ["list", "of", "dependencies"],
    "elements": [
        {{
            "name": "element_name",
            "type": "class|method|function|variable",
            "purpose": "brief description",
            "documentation": "detailed documentation",
            "line_number": 0,
            "scope": "optional_scope"
        }}
    ],
    "framework_hints": ["detected", "frameworks"]
}}"""

    def _parse_analysis_result(self, file_path: Path, content: str, analysis_result: str) -> FileAnalysis:
        """Parse LLM analysis result into FileAnalysis structure."""
        try:
            # Parse JSON response from LLM
            analysis_data = json.loads(analysis_result)
            
            # Create CodeElement instances
            elements = [
                CodeElement(**elem) for elem in analysis_data.get('elements', [])
            ]
            
            return FileAnalysis(
                path=str(file_path),
                language=self._detect_language(file_path, content),
                purpose=analysis_data.get('purpose', ''),
                exposures=analysis_data.get('exposures', []),
                dependencies=analysis_data.get('dependencies', []),
                elements=elements,
                framework_hints=analysis_data.get('framework_hints', [])
            )
            
        except json.JSONDecodeError:
            self.logger.error(f"Failed to parse LLM response for {file_path}")
            raise

    def _detect_language(self, file_path: Path) -> str:
        """Detect programming language based on file extension and content."""
        extension_map = {
            '.py': 'Python',
            '.js': 'JavaScript',
            '.ts': 'TypeScript',
            '.java': 'Java',
            '.cpp': 'C++',
            '.hpp': 'C++',
            '.c': 'C',
            '.h': 'C',
            '.rs': 'Rust',
            '.go': 'Go',
            '.rb': 'Ruby',
            '.php': 'PHP',
        }
        
        return extension_map.get(file_path.suffix.lower(), 'Unknown')

    def _create_empty_analysis(self, file_path: Path) -> FileAnalysis:
        """Create analysis for empty files like __init__.py."""
        return FileAnalysis(
            path=str(file_path),
            language=self._detect_language(file_path),
            purpose="Empty file or package marker",
            exposures=[],
            dependencies=[],
            elements=[],
            framework_hints=[]
        )
    
    def _create_basic_analysis(self, file_path: Path) -> FileAnalysis:
        """Create basic analysis when full analysis fails."""
        try:
            content = file_path.read_text(encoding='utf-8')
            dependencies = []
            
            # Try to extract at least the imports
            for line in content.splitlines():
                if line.strip().startswith(('import ', 'from ')):
                    try:
                        # Extract the main package name from import
                        if line.strip().startswith('from '):
                            package = line.split('from ')[1].split('.')[0].split()[0]
                        else:
                            package = line.split('import ')[1].split('.')[0].split()[0]
                        if package not in dependencies:
                            dependencies.append(package)
                    except:
                        continue

            return FileAnalysis(
                path=str(file_path),
                language=self._detect_language(file_path),
                purpose=f"File in {file_path.parent.name} module",
                exposures=[],
                dependencies=dependencies,
                elements=[],
                framework_hints=[]
            )
        except Exception as e:
            self.logger.debug(f"Error in basic analysis: {e}")
            return FileAnalysis(
                path=str(file_path),
                language=self._detect_language(file_path),
                purpose="Unable to analyze file",
                exposures=[],
                dependencies=[],
                elements=[],
                framework_hints=[]
            )

    def _analyze_simple_file(self, file_path: Path, content: str) -> FileAnalysis:
        """Create simple analysis for small files."""
        dependencies = []
        exposures = []
        elements = []
        
        for line_number, line in enumerate(content.splitlines(), 1):
            line = line.strip()
            
            # Extract imports
            if line.startswith(('import ', 'from ')):
                try:
                    if line.startswith('from '):
                        package = line.split('from ')[1].split('.')[0].split()[0]
                    else:
                        package = line.split('import ')[1].split('.')[0].split()[0]
                    if package not in dependencies:
                        dependencies.append(package)
                except:
                    continue
            
            # Extract function definitions
            elif line.startswith('def '):
                try:
                    func_name = line[4:line.index('(')]
                    exposures.append(func_name)
                    elements.append(CodeElement(
                        name=func_name,
                        type='function',
                        purpose='Simple function',
                        documentation='',
                        line_number=line_number
                    ))
                except:
                    continue
            
            # Extract class definitions
            elif line.startswith('class '):
                try:
                    class_name = line[6:line.index('(') if '(' in line else line.index(':')]
                    exposures.append(class_name)
                    elements.append(CodeElement(
                        name=class_name,
                        type='class',
                        purpose='Simple class',
                        documentation='',
                        line_number=line_number
                    ))
                except:
                    continue

        return FileAnalysis(
            path=str(file_path),
            language=self._detect_language(file_path),
            purpose=self._infer_simple_purpose(file_path, content),
            exposures=exposures,
            dependencies=dependencies,
            elements=elements,
            framework_hints=[]
        )

    def _infer_simple_purpose(self, file_path: Path, content: str) -> str:
        """Infer a simple purpose for a file based on its name and content."""
        filename = file_path.name
        
        if filename == '__init__.py':
            return 'Package initialization file'
        elif filename.startswith('test_'):
            return 'Test file'
        elif 'setup' in filename:
            return 'Package setup file'
        elif content.strip().startswith('"""') or content.strip().startswith("'''"):
            # Try to extract docstring
            try:
                first_line = content.strip().split('\n')[0].strip('"\'')
                return first_line
            except:
                pass
            
        # Default purpose based on directory
        return f"File in {file_path.parent.name} module"
