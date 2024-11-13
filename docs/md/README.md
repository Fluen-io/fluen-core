# fluen-core Documentation

## Project Overview

- **Primary Language:** Python
- **Frameworks:** dataclasses is used for simplified class definitions, YAML configuration style, dataclasses, Jiva Framework, Claude by Anthropic, asyncio (implicit async usage for asynchronous operations), artifacts follow Python&#39;s typing hints for better type checking, Detected use of the Jinja2 template engine based on template syntax., Possible integration with Sphinx or a custom documentation generation tool., D3.js, JavaScript ES6 features, YAML format for configuration, Jinja2, Markdown, Python, logging, pathlib, regular expressions (re), Click, Rich, asyncio, Python Type Hints, setuptools, jinja2, pytest, unittest.mock (AsyncMock and Mock), aiohttp, Python type hinting, Jinja2 template engine (indicated by use of {{ }} for variable interpolation and {% %} for control structures), AsyncIO, Python: asyncio, rich for async operations and console progress updates, typing
- **Last Updated:** 2024-11-13T18:00:12.228147
- **Git Commit:** 9997683a

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


## Dependencies

| Name | Type | Version | Used By |
|------|------|---------|---------|
| An API key from OpenAI or Mistral AI | external | None | N/A |
| BaseLLMProvider | external | None | N/A |
| Claude by Anthropic | external | None | N/A |
| Git | external | None | N/A |
| Jinja2 | external | None | [src/fluen/generator/templates/default/md/readme.md](reference/src_fluen_generator_templates_default_md_readme.md.md) |
| Jinja2==3.1.4 | external | None | N/A |
| Jiva Framework | external | None | N/A |
| MarkupSafe==3.0.2 | external | None | N/A |
| Mistral API | external | None | N/A |
| Ollama API | external | None | N/A |
| OpenAI API | external | None | N/A |
| PyYAML==6.0.2 | external | None | N/A |
| Pygments==2.18.0 | external | None | N/A |
| Python 3.9+ | external | None | N/A |
| abc | external | None | N/A |
| aiohttp | external | None | N/A |
| aiohttp&gt;=3.8.0 | external | None | N/A |
| analyzer.file_analyzer | external | None | N/A |
| assets/script.js | external | None | N/A |
| assets/styles.css | external | None | N/A |
| asyncio | external | None | [src/fluen/analyzer/file_analyzer.py](reference/src_fluen_analyzer_file_analyzer.py.md), [src/fluen/analyzer/project_analyzer.py](reference/src_fluen_analyzer_project_analyzer.py.md), [src/fluen/orchestrator.py](reference/src_fluen_orchestrator.py.md) |
| base_provider | external | None | [src/fluen/llm_providers/mistral_ai_provider.py](reference/src_fluen_llm_providers_mistral_ai_provider.py.md) |
| black&gt;=23.0.0 | external | None | N/A |
| click | external | None | N/A |
| click==8.1.7 | external | None | N/A |
| click&gt;=8.0.0 | external | None | N/A |
| config | external | None | N/A |
| coverage==7.6.4 | external | None | N/A |
| d3 | external | None | N/A |
| d3.js | external | None | N/A |
| d3.js (from https://cdnjs.cloudflare.com/ajax/libs/d3/7.8.5/d3.min.js) | external | None | N/A |
| dataclasses | external | None | [src/fluen/analyzer/file_analyzer.py](reference/src_fluen_analyzer_file_analyzer.py.md), [src/fluen/git_integration/manager.py](reference/src_fluen_git_integration_manager.py.md) |
| dataclasses.asdict | external | None | [src/fluen/generator/manifest.py](reference/src_fluen_generator_manifest.py.md) |
| dataclasses.dataclass | external | None | [src/fluen/generator/manifest.py](reference/src_fluen_generator_manifest.py.md), [src/fluen/state/manager.py](reference/src_fluen_state_manager.py.md) |
| datetime.datetime | external | None | N/A |
| dependency_1 | external | None | N/A |
| dependency_2 | external | None | N/A |
| exceptiongroup==1.2.2 | external | None | N/A |
| flake8&gt;=6.0.0 | external | None | N/A |
| fluen | external | None | N/A |
| fluen.analyzer.file_analyzer.FileAnalysis | external | None | [src/fluen/analyzer/project_analyzer.py](reference/src_fluen_analyzer_project_analyzer.py.md) |
| fluen.analyzer.file_analyzer.FileAnalyzer | external | None | [src/fluen/analyzer/project_analyzer.py](reference/src_fluen_analyzer_project_analyzer.py.md) |
| fluen.analyzer.project_analyzer.ProjectAnalyzer | external | None | N/A |
| fluen.config.FluenConfig | external | None | [src/fluen/orchestrator.py](reference/src_fluen_orchestrator.py.md) |
| fluen.generator.cross_referencer.CrossReferenceResolver | external | None | N/A |
| fluen.generator.doc_generator.DocumentationGenerator | external | None | [src/fluen/orchestrator.py](reference/src_fluen_orchestrator.py.md) |
| fluen.generator.manifest.ElementReference | external | None | [src/fluen/generator/cross_referencer.py](reference/src_fluen_generator_cross_referencer.py.md) |
| fluen.generator.manifest.ManifestGenerator | external | None | [src/fluen/analyzer/project_analyzer.py](reference/src_fluen_analyzer_project_analyzer.py.md), [src/fluen/cli.py](reference/src_fluen_cli.py.md), [src/fluen/orchestrator.py](reference/src_fluen_orchestrator.py.md) |
| fluen.generator.manifest.ProjectManifest | external | None | [src/fluen/generator/cross_referencer.py](reference/src_fluen_generator_cross_referencer.py.md), [src/fluen/orchestrator.py](reference/src_fluen_orchestrator.py.md) |
| fluen.generator.templates.template_manager.TemplateManager | external | None | [src/fluen/cli.py](reference/src_fluen_cli.py.md), [src/fluen/orchestrator.py](reference/src_fluen_orchestrator.py.md) |
| fluen.git_integration.manager.GitManager | external | None | [src/fluen/analyzer/project_analyzer.py](reference/src_fluen_analyzer_project_analyzer.py.md) |
| fluen.llm_providers.base_provider | external | None | N/A |
| fluen.llm_providers.base_provider.BaseLLMProvider | external | None | N/A |
| fluen.llm_providers.mistral_ai_provider | external | None | N/A |
| fluen.llm_providers.ollama_provider | external | None | N/A |
| fluen.llm_providers.openai_provider | external | None | N/A |
| fluen.models.scan.ScanOptions | external | None | [src/fluen/orchestrator.py](reference/src_fluen_orchestrator.py.md) |
| fluen.models.scan.ScanSelector | external | None | [src/fluen/orchestrator.py](reference/src_fluen_orchestrator.py.md) |
| fluen.orchestrator.Orchestrator | external | None | N/A |
| fluen.state.manager.StateManager | external | None | [src/fluen/analyzer/project_analyzer.py](reference/src_fluen_analyzer_project_analyzer.py.md) |
| git | external | None | [src/fluen/analyzer/file_analyzer.py](reference/src_fluen_analyzer_file_analyzer.py.md), [src/fluen/tests/conftest.py](reference/src_fluen_tests_conftest.py.md) |
| git_integration.manager | external | None | N/A |
| gitpython&gt;=3.1.0 | external | None | N/A |
| iniconfig==2.0.0 | external | None | N/A |
| jinja2 | external | None | N/A |
| jinja2&gt;=3.0.0 | external | None | N/A |
| json | external | None | [src/fluen/analyzer/file_analyzer.py](reference/src_fluen_analyzer_file_analyzer.py.md), [src/fluen/generator/manifest.py](reference/src_fluen_generator_manifest.py.md), [src/fluen/llm_providers/ollama_provider.py](reference/src_fluen_llm_providers_ollama_provider.py.md), [src/fluen/state/manager.py](reference/src_fluen_state_manager.py.md) |
| logging | external | None | [src/fluen/analyzer/file_analyzer.py](reference/src_fluen_analyzer_file_analyzer.py.md), [src/fluen/analyzer/project_analyzer.py](reference/src_fluen_analyzer_project_analyzer.py.md), [src/fluen/generator/cross_referencer.py](reference/src_fluen_generator_cross_referencer.py.md), [src/fluen/generator/doc_generator.py](reference/src_fluen_generator_doc_generator.py.md), [src/fluen/generator/manifest.py](reference/src_fluen_generator_manifest.py.md), [src/fluen/generator/templates/template_manager.py](reference/src_fluen_generator_templates_template_manager.py.md), [src/fluen/orchestrator.py](reference/src_fluen_orchestrator.py.md), [src/fluen/state/manager.py](reference/src_fluen_state_manager.py.md) |
| markdown-it-py==3.0.0 | external | None | N/A |
| mdurl==0.1.2 | external | None | N/A |
| mimetypes | external | None | N/A |
| mistralai | external | None | N/A |
| mistralai==1.1.0 | external | None | N/A |
| mistralai&gt;=0.0.7 | external | None | N/A |
| mypy&gt;=1.0.0 | external | None | N/A |
| openai | external | None | [src/fluen/llm_providers/openai_provider.py](reference/src_fluen_llm_providers_openai_provider.py.md) |
| openai==1.43.0 | external | None | N/A |
| openai&gt;=1.0.0 | external | None | N/A |
| os | external | None | N/A |
| packaging==24.1 | external | None | N/A |
| pathlib | external | None | [src/fluen/analyzer/file_analyzer.py](reference/src_fluen_analyzer_file_analyzer.py.md), [src/fluen/cli.py](reference/src_fluen_cli.py.md), [src/fluen/generator/templates/template_manager.py](reference/src_fluen_generator_templates_template_manager.py.md), [src/fluen/git_integration/manager.py](reference/src_fluen_git_integration_manager.py.md), [src/fluen/models/scan.py](reference/src_fluen_models_scan.py.md), [src/fluen/tests/conftest.py](reference/src_fluen_tests_conftest.py.md), [src/fluen/tests/test_git_manager.py](reference/src_fluen_tests_test_git_manager.py.md) |
| pathlib.Path | external | None | [src/fluen/analyzer/project_analyzer.py](reference/src_fluen_analyzer_project_analyzer.py.md), [src/fluen/generator/cross_referencer.py](reference/src_fluen_generator_cross_referencer.py.md), [src/fluen/generator/manifest.py](reference/src_fluen_generator_manifest.py.md), [src/fluen/orchestrator.py](reference/src_fluen_orchestrator.py.md), [src/fluen/state/manager.py](reference/src_fluen_state_manager.py.md) |
| pluggy==1.5.0 | external | None | N/A |
| pytest | external | None | [src/fluen/tests/conftest.py](reference/src_fluen_tests_conftest.py.md), [src/fluen/tests/test_git_manager.py](reference/src_fluen_tests_test_git_manager.py.md) |
| pytest-asyncio==0.24.0 | external | None | N/A |
| pytest-asyncio&gt;=0.21.0 | external | None | N/A |
| pytest-cov==6.0.0 | external | None | N/A |
| pytest-cov&gt;=4.0.0 | external | None | N/A |
| pytest==8.3.3 | external | None | N/A |
| pytest&gt;=7.0.0 | external | None | N/A |
| python-magic==0.4.27 | external | None | N/A |
| pyyaml&gt;=6.0 | external | None | N/A |
| re | external | None | [src/fluen/analyzer/file_analyzer.py](reference/src_fluen_analyzer_file_analyzer.py.md) |
| rich.console.Console | external | None | [src/fluen/orchestrator.py](reference/src_fluen_orchestrator.py.md) |
| rich.progress.Progress | external | None | [src/fluen/orchestrator.py](reference/src_fluen_orchestrator.py.md) |
| rich==13.9.4 | external | None | N/A |
| rich&gt;=10.0.0 | external | None | N/A |
| script (from ../assets/script.js) | external | None | N/A |
| setuptools | external | None | N/A |
| shutil | external | None | [src/fluen/tests/conftest.py](reference/src_fluen_tests_conftest.py.md) |
| stylesheet (from ../assets/styles.css) | external | None | N/A |
| tempfile | external | None | N/A |
| time | external | None | [src/fluen/orchestrator.py](reference/src_fluen_orchestrator.py.md) |
| tomli==2.0.2 | external | None | N/A |
| typing | external | None | [src/fluen/analyzer/file_analyzer.py](reference/src_fluen_analyzer_file_analyzer.py.md), [src/fluen/cli.py](reference/src_fluen_cli.py.md), [src/fluen/generator/templates/template_manager.py](reference/src_fluen_generator_templates_template_manager.py.md), [src/fluen/git_integration/manager.py](reference/src_fluen_git_integration_manager.py.md), [src/fluen/llm_factory.py](reference/src_fluen_llm_factory.py.md), [src/fluen/llm_providers/base_provider.py](reference/src_fluen_llm_providers_base_provider.py.md), [src/fluen/llm_providers/mistral_ai_provider.py](reference/src_fluen_llm_providers_mistral_ai_provider.py.md), [src/fluen/llm_providers/ollama_provider.py](reference/src_fluen_llm_providers_ollama_provider.py.md), [src/fluen/llm_providers/openai_provider.py](reference/src_fluen_llm_providers_openai_provider.py.md), [src/fluen/models/scan.py](reference/src_fluen_models_scan.py.md), [src/fluen/tests/conftest.py](reference/src_fluen_tests_conftest.py.md) |
| typing.Any | external | None | [src/fluen/generator/manifest.py](reference/src_fluen_generator_manifest.py.md) |
| typing.Callable | external | None | N/A |
| typing.Dict | external | None | [src/fluen/analyzer/project_analyzer.py](reference/src_fluen_analyzer_project_analyzer.py.md), [src/fluen/generator/manifest.py](reference/src_fluen_generator_manifest.py.md), [src/fluen/state/manager.py](reference/src_fluen_state_manager.py.md) |
| typing.List | external | None | [src/fluen/analyzer/project_analyzer.py](reference/src_fluen_analyzer_project_analyzer.py.md), [src/fluen/generator/manifest.py](reference/src_fluen_generator_manifest.py.md) |
| typing.Optional | external | None | [src/fluen/analyzer/project_analyzer.py](reference/src_fluen_analyzer_project_analyzer.py.md), [src/fluen/generator/manifest.py](reference/src_fluen_generator_manifest.py.md), [src/fluen/orchestrator.py](reference/src_fluen_orchestrator.py.md), [src/fluen/state/manager.py](reference/src_fluen_state_manager.py.md) |
| typing.Set | external | None | [src/fluen/analyzer/project_analyzer.py](reference/src_fluen_analyzer_project_analyzer.py.md), [src/fluen/generator/manifest.py](reference/src_fluen_generator_manifest.py.md) |
| typing.Tuple | external | None | N/A |
| typing_extensions==4.12.2 | external | None | N/A |
| unittest.mock | external | None | N/A |
| yaml | external | None | N/A |

## Navigation

- [Summary](SUMMARY.md)
- [Reference Documentation](reference/)