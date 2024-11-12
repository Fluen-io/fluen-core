# Summary

- [fluen-core Documentation](README.md)

## Project Structure

### JavaScript Files

- [src/fluen/generator/templates/default/script.js](reference/src_fluen_generator_templates_default_script.js.md)

### Python Files

- [setup.py](reference/setup.py.md)
- [src/fluen/__init__.py](reference/src_fluen___init__.py.md)
- [src/fluen/analyzer/__init__.py](reference/src_fluen_analyzer___init__.py.md)
- [src/fluen/analyzer/file_analyzer.py](reference/src_fluen_analyzer_file_analyzer.py.md)
- [src/fluen/analyzer/project_analyzer.py](reference/src_fluen_analyzer_project_analyzer.py.md)
- [src/fluen/cli.py](reference/src_fluen_cli.py.md)
- [src/fluen/config.py](reference/src_fluen_config.py.md)
- [src/fluen/generator/__init__.py](reference/src_fluen_generator___init__.py.md)
- [src/fluen/generator/cross_referencer.py](reference/src_fluen_generator_cross_referencer.py.md)
- [src/fluen/generator/doc_generator.py](reference/src_fluen_generator_doc_generator.py.md)
- [src/fluen/generator/manifest.py](reference/src_fluen_generator_manifest.py.md)
- [src/fluen/generator/templates/template_manager.py](reference/src_fluen_generator_templates_template_manager.py.md)
- [src/fluen/git_integration/__init__.py](reference/src_fluen_git_integration___init__.py.md)
- [src/fluen/git_integration/manager.py](reference/src_fluen_git_integration_manager.py.md)
- [src/fluen/llm_factory.py](reference/src_fluen_llm_factory.py.md)
- [src/fluen/llm_providers/__init__.py](reference/src_fluen_llm_providers___init__.py.md)
- [src/fluen/llm_providers/base_provider.py](reference/src_fluen_llm_providers_base_provider.py.md)
- [src/fluen/llm_providers/mistral_ai_provider.py](reference/src_fluen_llm_providers_mistral_ai_provider.py.md)
- [src/fluen/llm_providers/ollama_provider.py](reference/src_fluen_llm_providers_ollama_provider.py.md)
- [src/fluen/llm_providers/openai_provider.py](reference/src_fluen_llm_providers_openai_provider.py.md)
- [src/fluen/orchestrator.py](reference/src_fluen_orchestrator.py.md)
- [src/fluen/state/__init__.py](reference/src_fluen_state___init__.py.md)
- [src/fluen/state/manager.py](reference/src_fluen_state_manager.py.md)
- [src/fluen/tests/__init__.py](reference/src_fluen_tests___init__.py.md)
- [src/fluen/tests/conftest.py](reference/src_fluen_tests_conftest.py.md)
- [src/fluen/tests/test_file_analyzer.py](reference/src_fluen_tests_test_file_analyzer.py.md)
- [src/fluen/tests/test_git_manager.py](reference/src_fluen_tests_test_git_manager.py.md)

### Unknown Files

- [.fluen/cache/state.json](reference/.fluen_cache_state.json.md)
- [fluen_config.example.yml](reference/fluen_config.example.yml.md)
- [fluen_config.yml](reference/fluen_config.yml.md)
- [LICENSE](reference/LICENSE.md)
- [requirements.txt](reference/requirements.txt.md)
- [src/fluen/generator/templates/default/html/index.html](reference/src_fluen_generator_templates_default_html_index.html.md)
- [src/fluen/generator/templates/default/html/reference.html](reference/src_fluen_generator_templates_default_html_reference.html.md)
- [src/fluen/generator/templates/default/md/readme.md](reference/src_fluen_generator_templates_default_md_readme.md.md)
- [src/fluen/generator/templates/default/md/reference.md](reference/src_fluen_generator_templates_default_md_reference.md.md)
- [src/fluen/generator/templates/default/styles.css](reference/src_fluen_generator_templates_default_styles.css.md)


## Quick Links

- [Project Overview](README.md#project-overview)
- [Frameworks Used](README.md#frameworks)

## Reference Documentation

### [.fluen/cache/state.json](reference/.fluen_cache_state.json.md)

Represents metadata or a summary of a project&#39;s source code processing status.

**Public API:**
- `files_processed` (exposure)
- `last_commit` (exposure)
- `last_run_timestamp` (exposure)
- `manifest_path` (exposure)
- `total_files` (exposure)

### [LICENSE](reference/LICENSE.md)

The primary purpose of this document is to define the conditions under which software may be...

**Public API:**
- `TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION` (exposure)

### [fluen_config.example.yml](reference/fluen_config.example.yml.md)

This configuration file is used for setting up and managing settings for a project named...

**Public API:**
- `cache_dir` (exposure)
- `default_export_type` (exposure)
- `llm` (exposure)
- `output_dir` (exposure)
- `project` (exposure)
- `temp_dir` (exposure)

### [fluen_config.yml](reference/fluen_config.yml.md)

This configuration file is designed to set up and control the behavior of a code documentation...

**Public API:**
- `cache_dir` (exposure)
- `default_export_type` (exposure)
- `llm.api_key` (exposure)
- `llm.model` (exposure)
- `llm.provider` (exposure)
- `output_dir` (exposure)
- `project.description` (exposure)
- `project.ignore_patterns` (exposure)
- `project.name` (exposure)
- `temp_dir` (exposure)

### [requirements.txt](reference/requirements.txt.md)

This code represents a list of dependencies for a Python project. It specifies the external...


### [setup.py](reference/setup.py.md)

Sets up a Python package named &#39;fluen&#39;, configuring its metadata, dependencies, and entry points.

**Public API:**
- `find_packages` (exposure)
- `setup` (exposure)

### [src/fluen/__init__.py](reference/src_fluen___init__.py.md)

Empty file or package marker


### [src/fluen/analyzer/__init__.py](reference/src_fluen_analyzer___init__.py.md)

Empty file or package marker


### [src/fluen/analyzer/file_analyzer.py](reference/src_fluen_analyzer_file_analyzer.py.md)

Purpose not specified


### [src/fluen/analyzer/project_analyzer.py](reference/src_fluen_analyzer_project_analyzer.py.md)

The code provides functionality for analyzing a software project at a project level. It handles...

**Public API:**
- `ProjectAnalyzer.__init__` (exposure)
- `ProjectAnalyzer.analyze` (exposure)
- `ProjectAnalyzer.analyze_path` (exposure)

### [src/fluen/cli.py](reference/src_fluen_cli.py.md)

This code defines a CLI application for generating and exporting code documentation using large...

**Public API:**
- `cli` (exposure)
- `docs` (exposure)
- `export` (exposure)
- `generate` (exposure)

### [src/fluen/config.py](reference/src_fluen_config.py.md)

This code defines configurations for a language model application, allowing for these...

**Public API:**
- `FluenConfig` (exposure)
- `FluenConfig.create_default` (exposure)
- `FluenConfig.ensure_directories` (exposure)
- `FluenConfig.load` (exposure)
- `LLMConfig` (exposure)

### [src/fluen/generator/__init__.py](reference/src_fluen_generator___init__.py.md)

Empty file or package marker


### [src/fluen/generator/cross_referencer.py](reference/src_fluen_generator_cross_referencer.py.md)

The code is designed to resolve cross-references between documentation elements and generate...

**Public API:**
- `CrossReferenceResolver` (exposure)
- `Reference` (exposure)

### [src/fluen/generator/doc_generator.py](reference/src_fluen_generator_doc_generator.py.md)

The primary purpose of this code is to manage the generation of documentation in HTML and...

**Public API:**
- `DocumentationGenerator` (exposure)
- `generate` (exposure)
- `HTMLGenerator` (exposure)
- `MarkdownGenerator` (exposure)

### [src/fluen/generator/manifest.py](reference/src_fluen_generator_manifest.py.md)

The primary purpose of this code is to generate and manage a documentation manifest for a given...

**Public API:**
- `DependencyInfo` (exposure)
- `ElementReference` (exposure)
- `FileManifest` (exposure)
- `ManifestGenerator` (exposure)
- `ProjectManifest` (exposure)

### [src/fluen/generator/templates/default/html/index.html](reference/src_fluen_generator_templates_default_html_index.html.md)

The primary purpose of this code is to generate a static HTML documentation page for a software...

**Public API:**
- `HTML structure with placeholders for project data` (exposure)
- `Link to an external JavaScript file` (exposure)
- `Link to an external stylesheet` (exposure)
- `Project information such as primary language, frameworks, last update, and git commit` (exposure)
- `Sidebar navigation menu with links to reference files` (exposure)
- `Table of project dependencies with version and used-by information` (exposure)

### [src/fluen/generator/templates/default/html/reference.html](reference/src_fluen_generator_templates_default_html_reference.html.md)

File in html module


### [src/fluen/generator/templates/default/md/readme.md](reference/src_fluen_generator_templates_default_md_readme.md.md)

The primary purpose of this code is to generate documentation for a project using templating. It...

**Public API:**
- `reference/` (exposure)
- `Summary.md` (exposure)

### [src/fluen/generator/templates/default/md/reference.md](reference/src_fluen_generator_templates_default_md_reference.md.md)

This template is intended to generate documentation for a code file automatically. It outlines...

**Public API:**
- `{{ exposure.name }}` (exposure)

### [src/fluen/generator/templates/default/script.js](reference/src_fluen_generator_templates_default_script.js.md)

This code implements a search functionality for documentation, and also highlights the current...

**Public API:**
- `DocumentationSearch` (exposure)
- `highlightCurrentPage` (exposure)

### [src/fluen/generator/templates/default/styles.css](reference/src_fluen_generator_templates_default_styles.css.md)

This code provides styles for a webpage layout that includes a sidebar, content area, and search...

**Public API:**
- `*` (exposure)
- `.content` (exposure)
- `.element` (exposure)
- `.element-header` (exposure)
- `.element-header code` (exposure)
- `.file-group` (exposure)
- `.file-group a` (exposure)
- `.file-group a:hover` (exposure)
- `.file-group h3` (exposure)
- `.file-group li` (exposure)
- `.file-group ul` (exposure)
- `.metadata` (exposure)
- `.scope-badge` (exposure)
- `.search-active .search-results` (exposure)
- `.search-container` (exposure)
- `.search-input` (exposure)
- `.search-result-item` (exposure)
- `.search-result-item:hover` (exposure)
- `.search-results` (exposure)
- `.sidebar` (exposure)
- `.sidebar-content` (exposure)
- `.sidebar-header` (exposure)
- `.sidebar-header h1` (exposure)
- `.sidebar-header p` (exposure)
- `.type-badge` (exposure)
- `:root` (exposure)
- `body` (exposure)

### [src/fluen/generator/templates/template_manager.py](reference/src_fluen_generator_templates_template_manager.py.md)

The primary purpose of the code is to manage the template system for documentation generation...

**Public API:**
- `TemplateManager.__init__` (exposure)
- `TemplateManager._detect_language` (exposure)
- `TemplateManager._register_filters` (exposure)
- `TemplateManager.get_default_context` (exposure)
- `TemplateManager.render_template` (exposure)

### [src/fluen/git_integration/__init__.py](reference/src_fluen_git_integration___init__.py.md)

Empty file or package marker


### [src/fluen/git_integration/manager.py](reference/src_fluen_git_integration_manager.py.md)

This module provides functionality for managing and analyzing Git repositories, including...

**Public API:**
- `GitDiff` (exposure)
- `GitManager` (exposure)

### [src/fluen/llm_factory.py](reference/src_fluen_llm_factory.py.md)

This code defines a factory class used to create instances of various LLM provider classes based...

**Public API:**
- `LLMProviderFactory` (exposure)
- `LLMProviderFactory.create` (exposure)

### [src/fluen/llm_providers/__init__.py](reference/src_fluen_llm_providers___init__.py.md)

Empty file or package marker


### [src/fluen/llm_providers/base_provider.py](reference/src_fluen_llm_providers_base_provider.py.md)

The primary purpose of the code is to define an abstract base class for a language model...

**Public API:**
- `BaseLLMProvider` (exposure)

### [src/fluen/llm_providers/mistral_ai_provider.py](reference/src_fluen_llm_providers_mistral_ai_provider.py.md)

The primary purpose of this code is to provide an implementation of the MistralAIProvider class...

**Public API:**
- `generate` (exposure)
- `get_embedding` (exposure)
- `MistralAIProvider` (exposure)

### [src/fluen/llm_providers/ollama_provider.py](reference/src_fluen_llm_providers_ollama_provider.py.md)

The code defines an asynchronous provider for interacting with an LLM service via HTTP API, with...

**Public API:**
- `OllamaProvider` (exposure)
- `OllamaProvider.__init__` (exposure)
- `OllamaProvider.generate` (exposure)
- `OllamaProvider.get_embedding` (exposure)

### [src/fluen/llm_providers/openai_provider.py](reference/src_fluen_llm_providers_openai_provider.py.md)

The primary purpose of this code is to define an asynchronous provider class, OpenAIProvider,...

**Public API:**
- `generate` (exposure)
- `get_embedding` (exposure)
- `OpenAIProvider` (exposure)

### [src/fluen/orchestrator.py](reference/src_fluen_orchestrator.py.md)

The primary purpose of this code is to orchestrate the process of generating documentation for a...

**Public API:**
- `main` (exposure)
- `Orchestrator.__init__` (exposure)
- `Orchestrator._create_llm_provider` (exposure)
- `Orchestrator._generate_docs` (exposure)
- `Orchestrator._initialize_repository` (exposure)
- `Orchestrator._run_analysis` (exposure)
- `Orchestrator.generate_documentation` (exposure)
- `ProcessManager.run` (exposure)

### [src/fluen/state/__init__.py](reference/src_fluen_state___init__.py.md)

Empty file or package marker


### [src/fluen/state/manager.py](reference/src_fluen_state_manager.py.md)

Manage the state of a documentation generation process by saving, loading, and updating progress...

**Public API:**
- `DocumentationState` (exposure)
- `StateManager` (exposure)

### [src/fluen/tests/__init__.py](reference/src_fluen_tests___init__.py.md)

Empty file or package marker


### [src/fluen/tests/conftest.py](reference/src_fluen_tests_conftest.py.md)

This code defines configuration and shared fixtures for PyTest to facilitate testing by setting...

**Public API:**
- `mock_config` (exposure)
- `sample_repo` (exposure)
- `temp_dir` (exposure)

### [src/fluen/tests/test_file_analyzer.py](reference/src_fluen_tests_test_file_analyzer.py.md)

Tests for the file analysis functionality in a Python project using mock and asynchronous testing.

**Public API:**
- `mock_llm_provider` (exposure)
- `test_analyze_binary_file` (exposure)
- `test_analyze_file` (exposure)
- `test_element_extraction` (exposure)

### [src/fluen/tests/test_git_manager.py](reference/src_fluen_tests_test_git_manager.py.md)

This code provides test cases for the GitManager functionality, ensuring correct behavior of Git...

**Public API:**
- `test_get_changes_since_commit` (exposure)
- `test_get_current_commit` (exposure)
- `test_get_file_content` (exposure)
- `test_git_manager_initialization` (exposure)


---
Generated on 2024-11-12T20:10:07.635990  
Git commit: c529b8f6