# Summary

- [fluen-core Documentation](README.md)

## Project Structure

### JavaScript Files

- [src/fluen/generator/templates/default/static/script.js](reference/src_fluen_generator_templates_default_static_script.js.md)

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
- [src/fluen/models/__init__.py](reference/src_fluen_models___init__.py.md)
- [src/fluen/models/scan.py](reference/src_fluen_models_scan.py.md)
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
- [README.md](reference/README.md.md)
- [requirements.txt](reference/requirements.txt.md)
- [src/fluen/generator/templates/default/html/empty.html](reference/src_fluen_generator_templates_default_html_empty.html.md)
- [src/fluen/generator/templates/default/html/index.html](reference/src_fluen_generator_templates_default_html_index.html.md)
- [src/fluen/generator/templates/default/html/reference.html](reference/src_fluen_generator_templates_default_html_reference.html.md)
- [src/fluen/generator/templates/default/md/readme.md](reference/src_fluen_generator_templates_default_md_readme.md.md)
- [src/fluen/generator/templates/default/md/reference.md](reference/src_fluen_generator_templates_default_md_reference.md.md)
- [src/fluen/generator/templates/default/md/summary.md](reference/src_fluen_generator_templates_default_md_summary.md.md)
- [src/fluen/generator/templates/default/static/styles.css](reference/src_fluen_generator_templates_default_static_styles.css.md)


## Quick Links

- [Project Overview](README.md#project-overview)
- [Frameworks Used](README.md#frameworks)

## Reference Documentation

### [.fluen/cache/state.json](reference/.fluen_cache_state.json.md)

This JSON object represents metadata for a project, possibly for tracking purposes in version...

**Public API:**
- `files_processed` (exposure)
- `last_commit` (exposure)
- `last_run_timestamp` (exposure)
- `manifest_path` (exposure)
- `total_files` (exposure)

### [LICENSE](reference/LICENSE.md)

The primary purpose of this text is to provide the full terms and conditions of the Apache...


### [README.md](reference/README.md.md)

Fluen is a documentation generator powered by LLMs (Large Language Models). It creates...

**Public API:**
- `fluen.docs.export` (exposure)
- `fluen.docs.generate` (exposure)
- `fluen_config.yml` (exposure)

### [fluen_config.example.yml](reference/fluen_config.example.yml.md)

Configuration file for the Fluen code documentation generator, allowing users to specify...

**Public API:**
- `cache_dir` (exposure)
- `default_export_type` (exposure)
- `llm:api_key` (exposure)
- `llm:model` (exposure)
- `llm:provider` (exposure)
- `output_dir` (exposure)
- `project:description` (exposure)
- `project:ignore_patterns` (exposure)
- `project:name` (exposure)
- `temp_dir` (exposure)

### [fluen_config.yml](reference/fluen_config.yml.md)

This configuration file is for setting up parameters for an application using GPT models via a...

**Public API:**
- `cache directories` (exposure)
- `llm settings` (exposure)
- `output directories` (exposure)

### [requirements.txt](reference/requirements.txt.md)

This file lists the dependencies required for a Python project, including their specific versions.


### [setup.py](reference/setup.py.md)

This code serves as a setup script for a Python package named &#39;fluen&#39;. It defines the package...

**Public API:**
- `fluen.cli:cli` (exposure)

### [src/fluen/__init__.py](reference/src_fluen___init__.py.md)

Empty file or package marker


### [src/fluen/analyzer/__init__.py](reference/src_fluen_analyzer___init__.py.md)

Empty file or package marker


### [src/fluen/analyzer/file_analyzer.py](reference/src_fluen_analyzer_file_analyzer.py.md)

File in analyzer module


### [src/fluen/analyzer/project_analyzer.py](reference/src_fluen_analyzer_project_analyzer.py.md)

Analyzes project files and manages full or incremental analysis based on git changes and state...

**Public API:**
- `ProjectAnalyzer` (exposure)

### [src/fluen/cli.py](reference/src_fluen_cli.py.md)

This code defines a command-line interface (CLI) application using Click, designed to handle...

**Public API:**
- `cli` (exposure)
- `docs` (exposure)
- `export` (exposure)
- `generate` (exposure)

### [src/fluen/config.py](reference/src_fluen_config.py.md)

This code provides a configuration management system for an application that uses a large...

**Public API:**
- `FluenConfig` (exposure)
- `FluenConfig.create_default` (exposure)
- `FluenConfig.ensure_directories` (exposure)
- `FluenConfig.load` (exposure)
- `LLMConfig` (exposure)

### [src/fluen/generator/__init__.py](reference/src_fluen_generator___init__.py.md)

Empty file or package marker


### [src/fluen/generator/cross_referencer.py](reference/src_fluen_generator_cross_referencer.py.md)

The primary purpose of this code is to handle cross-referencing between documentation elements...

**Public API:**
- `CrossReferenceResolver.__init__` (exposure)
- `CrossReferenceResolver.generate_reference_graph` (exposure)
- `CrossReferenceResolver.get_incoming_references` (exposure)
- `CrossReferenceResolver.get_outgoing_references` (exposure)
- `CrossReferenceResolver.resolve_references` (exposure)

### [src/fluen/generator/doc_generator.py](reference/src_fluen_generator_doc_generator.py.md)

The primary purpose of this code is to generate project documentation in HTML and Markdown...

**Public API:**
- `BaseFormatGenerator` (exposure)
- `DocumentationGenerator` (exposure)
- `HTMLGenerator` (exposure)
- `MarkdownGenerator` (exposure)

### [src/fluen/generator/manifest.py](reference/src_fluen_generator_manifest.py.md)

The primary purpose of this code is to generate a manifest file for a project, which includes...

**Public API:**
- `DependencyInfo` (exposure)
- `ElementReference` (exposure)
- `FileManifest` (exposure)
- `FileRelationships` (exposure)
- `ManifestGenerator` (exposure)
- `ProjectManifest` (exposure)

### [src/fluen/generator/templates/default/html/empty.html](reference/src_fluen_generator_templates_default_html_empty.html.md)

This HTML code serves as a static web page template for displaying project documentation, with...

**Public API:**
- `CSS for styling` (exposure)
- `HTML structure elements` (exposure)
- `JavaScript for dynamic behavior` (exposure)

### [src/fluen/generator/templates/default/html/index.html](reference/src_fluen_generator_templates_default_html_index.html.md)

The primary purpose of this code is to generate an HTML page for project documentation with a...

**Public API:**
- `dependencies-section` (exposure)
- `main-content` (exposure)
- `project-info` (exposure)
- `search-input` (exposure)
- `sidebar` (exposure)

### [src/fluen/generator/templates/default/html/reference.html](reference/src_fluen_generator_templates_default_html_reference.html.md)

This HTML code serves as a template for generating a documentation page for a project file. It...

**Public API:**
- `dependencies-section` (exposure)
- `element-navigation` (exposure)
- `elements-section` (exposure)
- `file-header` (exposure)
- `lineage-section` (exposure)
- `search-container` (exposure)
- `sidebar-header` (exposure)

### [src/fluen/generator/templates/default/md/readme.md](reference/src_fluen_generator_templates_default_md_readme.md.md)

This code acts as a Jinja2 template for generating documentation for a software project. It...

**Public API:**
- `Dependencies` (exposure)
- `Navigation` (exposure)
- `Project Overview` (exposure)
- `Project Structure` (exposure)

### [src/fluen/generator/templates/default/md/reference.md](reference/src_fluen_generator_templates_default_md_reference.md.md)

This code serves as a template for generating documentation for a codebase, likely dynamically...

**Public API:**
- `exposed_class_1` (exposure)
- `exposed_function_1` (exposure)

### [src/fluen/generator/templates/default/md/summary.md](reference/src_fluen_generator_templates_default_md_summary.md.md)

This code is a template script for generating documentation for a project. It aims to create...

**Public API:**
- `Project Structure` (exposure)
- `Quick Links` (exposure)
- `README.md` (exposure)
- `Reference Documentation` (exposure)
- `{% set project_overview = &#39;Project Overview&#39; %}` (exposure)

### [src/fluen/generator/templates/default/static/script.js](reference/src_fluen_generator_templates_default_static_script.js.md)

The code provides functionality for searching documentation and visualizing data through a...

**Public API:**
- `DocumentationSearch` (exposure)
- `LineageGraph` (exposure)

### [src/fluen/generator/templates/default/static/styles.css](reference/src_fluen_generator_templates_default_static_styles.css.md)

This CSS stylesheet is designed to provide a consistent and responsive layout for a web...

**Public API:**
- `*` (exposure)
- `.content` (exposure)
- `.element` (exposure)
- `.element-header` (exposure)
- `.element-header code` (exposure)
- `.lineage-graph` (exposure)
- `.main-content` (exposure)
- `.main-header` (exposure)
- `.scope-badge` (exposure)
- `.search-active .search-results` (exposure)
- `.search-container` (exposure)
- `.search-input` (exposure)
- `.search-result-item` (exposure)
- `.search-results` (exposure)
- `.sidebar` (exposure)
- `.sidebar-content` (exposure)
- `.sidebar-header` (exposure)
- `.sidebar-header h1` (exposure)
- `.sidebar-header h1 a` (exposure)
- `.type-badge` (exposure)
- `:root` (exposure)
- `@media (max-width: 768px)` (exposure)
- `body` (exposure)

### [src/fluen/generator/templates/template_manager.py](reference/src_fluen_generator_templates_template_manager.py.md)

The primary purpose of this code is to manage a template system for documentation generation...

**Public API:**
- `TemplateManager` (exposure)

### [src/fluen/git_integration/__init__.py](reference/src_fluen_git_integration___init__.py.md)

Empty file or package marker


### [src/fluen/git_integration/manager.py](reference/src_fluen_git_integration_manager.py.md)

The primary purpose of this code is to provide functionality for managing and analyzing Git...

**Public API:**
- `GitDiff` (exposure)
- `GitManager` (exposure)

### [src/fluen/llm_factory.py](reference/src_fluen_llm_factory.py.md)

The primary purpose of this code is to provide a factory class, LLMProviderFactory, that creates...

**Public API:**
- `LLMProviderFactory` (exposure)
- `LLMProviderFactory.create` (exposure)

### [src/fluen/llm_providers/__init__.py](reference/src_fluen_llm_providers___init__.py.md)

Empty file or package marker


### [src/fluen/llm_providers/base_provider.py](reference/src_fluen_llm_providers_base_provider.py.md)

This code outlines an abstract base class for a language model provider interface. It defines...

**Public API:**
- `BaseLLMProvider` (exposure)
- `generate` (exposure)
- `get_embedding` (exposure)

### [src/fluen/llm_providers/mistral_ai_provider.py](reference/src_fluen_llm_providers_mistral_ai_provider.py.md)

This code provides an implementation of a language model provider using the Mistral service. It...

**Public API:**
- `generate` (exposure)
- `get_embedding` (exposure)
- `MistralAIProvider` (exposure)

### [src/fluen/llm_providers/ollama_provider.py](reference/src_fluen_llm_providers_ollama_provider.py.md)

The primary purpose of this code is to provide an implementation of a language model provider...

**Public API:**
- `generate` (exposure)
- `get_embedding` (exposure)
- `OllamaProvider` (exposure)

### [src/fluen/llm_providers/openai_provider.py](reference/src_fluen_llm_providers_openai_provider.py.md)

The primary purpose of this code is to serve as a provider for interacting with OpenAI&#39;s APIs to...

**Public API:**
- `OpenAIProvider` (exposure)

### [src/fluen/models/__init__.py](reference/src_fluen_models___init__.py.md)

Empty file or package marker


### [src/fluen/models/scan.py](reference/src_fluen_models_scan.py.md)

The code provides functionality for parsing, validating, and handling selectors for a scanning...

**Public API:**
- `ScanOptions` (exposure)
- `ScanOptions.is_selective_scan` (exposure)
- `ScanSelector` (exposure)
- `ScanSelector.is_element_selector` (exposure)
- `ScanSelector.is_path_selector` (exposure)

### [src/fluen/orchestrator.py](reference/src_fluen_orchestrator.py.md)

The primary purpose of this code is to orchestrate the process of generating documentation for a...

**Public API:**
- `main` (exposure)
- `Orchestrator` (exposure)
- `ProcessManager` (exposure)

### [src/fluen/state/__init__.py](reference/src_fluen_state___init__.py.md)

Empty file or package marker


### [src/fluen/state/manager.py](reference/src_fluen_state_manager.py.md)

This module manages the state of a documentation generation process, allowing for saving,...

**Public API:**
- `DocumentationState` (exposure)
- `load` (exposure)
- `save` (exposure)
- `set_manifest_path` (exposure)
- `StateManager` (exposure)
- `update_commit` (exposure)
- `update_progress` (exposure)

### [src/fluen/tests/__init__.py](reference/src_fluen_tests___init__.py.md)

Empty file or package marker


### [src/fluen/tests/conftest.py](reference/src_fluen_tests_conftest.py.md)

This code provides PyTest fixtures for setting up testing environments such as temporary file...

**Public API:**
- `mock_config` (exposure)
- `sample_repo` (exposure)
- `temp_dir` (exposure)

### [src/fluen/tests/test_file_analyzer.py](reference/src_fluen_tests_test_file_analyzer.py.md)

Unit tests for file analysis functionality utilizing a mock LLM provider.

**Public API:**
- `test_analyze_binary_file` (exposure)
- `test_analyze_file` (exposure)
- `test_element_extraction` (exposure)

### [src/fluen/tests/test_git_manager.py](reference/src_fluen_tests_test_git_manager.py.md)

Unit tests for verifying the functionality of GitManager and GitDiff classes for managing Git operations.

**Public API:**
- `test_get_changes_since_commit` (exposure)
- `test_get_current_commit` (exposure)
- `test_get_file_content` (exposure)
- `test_git_manager_initialization` (exposure)


---
Generated on 2024-11-13T18:00:12.228147  
Git commit: 9997683a