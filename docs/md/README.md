# fluen-core Documentation

## Project Overview

- **Primary Language:** Python
- **Frameworks:** dataclasses - use of @dataclass decorator, logging - for logging purposes, asyncio, OpenAI API client, pytest, Jinja2, aiohttp (for async HTTP requests), setuptools, Jinja2 or similar templating engine, jinja2, Click, Rich, dataclasses, rich, detected_frameworks_based_on_analysis, logging, asyncio for asynchronous operations, logging for error and process logging, GitPython, yaml, YAML format for configuration, None, Asyncio, Click - for CLI interaction, Rich - for enhanced console output and progress indicators, Asyncio - for asynchronous execution within command functions, click, pathlib, Python logging, possibly custom-framework (fluen), asyncio framework for asynchronous programming in Python, Python standard library features such as abstract base classes and type hints, openai-py, Python typing, aiohttp
- **Last Updated:** 2024-11-12T20:10:07.635990
- **Git Commit:** c529b8f6

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


## Dependencies

| Name | Type | Version | Used By |
|------|------|---------|---------|
| .base_provider | internal | None | [src/fluen/llm_providers/mistral_ai_provider.py](reference/src_fluen_llm_providers_mistral_ai_provider.py.md), [src/fluen/llm_providers/ollama_provider.py](reference/src_fluen_llm_providers_ollama_provider.py.md) |
| .base_provider.BaseLLMProvider | internal | None | N/A |
| DOM API | external | None | N/A |
| Jinja2 | external | None | N/A |
| MarkupSafe | external | None | N/A |
| PyYAML | external | None | N/A |
| Pygments | external | None | N/A |
| abc | external | None | [src/fluen/llm_providers/base_provider.py](reference/src_fluen_llm_providers_base_provider.py.md) |
| aiohttp | external | None | [src/fluen/llm_providers/ollama_provider.py](reference/src_fluen_llm_providers_ollama_provider.py.md) |
| aiohttp&gt;=3.8.0 | external | None | N/A |
| analyzer.file_analyzer.CodeElement | external | None | N/A |
| analyzer.file_analyzer.FileAnalysis | external | None | N/A |
| analyzer.file_analyzer.FileAnalyzer | external | None | N/A |
| asdict | external | None | N/A |
| assets/script.js | external | None | N/A |
| assets/styles.css | external | None | N/A |
| asyncio | external | None | [src/fluen/analyzer/file_analyzer.py](reference/src_fluen_analyzer_file_analyzer.py.md), [src/fluen/analyzer/project_analyzer.py](reference/src_fluen_analyzer_project_analyzer.py.md), [src/fluen/cli.py](reference/src_fluen_cli.py.md), [src/fluen/orchestrator.py](reference/src_fluen_orchestrator.py.md) |
| base_provider | external | None | N/A |
| base_provider.BaseLLMProvider | external | None | N/A |
| black&gt;=23.0.0 | external | None | N/A |
| click | external | None | [src/fluen/cli.py](reference/src_fluen_cli.py.md) |
| click&gt;=8.0.0 | external | None | N/A |
| config | external | None | N/A |
| coverage | external | None | N/A |
| dataclasses | external | None | [src/fluen/analyzer/file_analyzer.py](reference/src_fluen_analyzer_file_analyzer.py.md), [src/fluen/config.py](reference/src_fluen_config.py.md), [src/fluen/git_integration/manager.py](reference/src_fluen_git_integration_manager.py.md), [src/fluen/state/manager.py](reference/src_fluen_state_manager.py.md) |
| dataclasses.asdict | external | None | N/A |
| dataclasses.dataclass | external | None | N/A |
| datetime.datetime | external | None | N/A |
| dev dependencies: pytest&gt;=7.0.0 | external | None | N/A |
| exceptiongroup | external | None | N/A |
| fetch API | external | None | N/A |
| flake8&gt;=6.0.0 | external | None | N/A |
| fluen | external | None | [src/fluen/analyzer/file_analyzer.py](reference/src_fluen_analyzer_file_analyzer.py.md) |
| fluen.analyzer.file_analyzer.FileAnalysis | external | None | [src/fluen/analyzer/project_analyzer.py](reference/src_fluen_analyzer_project_analyzer.py.md) |
| fluen.analyzer.file_analyzer.FileAnalyzer | external | None | [src/fluen/analyzer/project_analyzer.py](reference/src_fluen_analyzer_project_analyzer.py.md) |
| fluen.analyzer.project_analyzer.ProjectAnalyzer | external | None | N/A |
| fluen.config | external | None | N/A |
| fluen.config - FluenConfig | external | None | N/A |
| fluen.config.FluenConfig | external | None | [src/fluen/cli.py](reference/src_fluen_cli.py.md), [src/fluen/orchestrator.py](reference/src_fluen_orchestrator.py.md) |
| fluen.generator.cross_referencer.CrossReferenceResolver | external | None | N/A |
| fluen.generator.doc_generator.DocumentationGenerator | external | None | N/A |
| fluen.generator.manifest | external | None | N/A |
| fluen.generator.manifest.ElementReference | external | None | N/A |
| fluen.generator.manifest.ManifestGenerator | external | None | [src/fluen/analyzer/project_analyzer.py](reference/src_fluen_analyzer_project_analyzer.py.md) |
| fluen.generator.manifest.ProjectManifest | external | None | [src/fluen/generator/doc_generator.py](reference/src_fluen_generator_doc_generator.py.md) |
| fluen.generator.templates.template_manager.TemplateManager | external | None | [src/fluen/generator/doc_generator.py](reference/src_fluen_generator_doc_generator.py.md) |
| fluen.git_integration.manager.GitManager | external | None | [src/fluen/analyzer/project_analyzer.py](reference/src_fluen_analyzer_project_analyzer.py.md) |
| fluen.llm_providers.base_provider.BaseLLMProvider | external | None | [src/fluen/orchestrator.py](reference/src_fluen_orchestrator.py.md) |
| fluen.llm_providers.mistral_ai_provider.MistralAIProvider | external | None | N/A |
| fluen.llm_providers.ollama_provider.OllamaProvider | external | None | N/A |
| fluen.llm_providers.openai_provider.OpenAIProvider | external | None | N/A |
| fluen.models.scan | external | None | N/A |
| fluen.models.scan - ScanSelector, ScanOptions | external | None | N/A |
| fluen.models.scan.ScanOptions | external | None | [src/fluen/cli.py](reference/src_fluen_cli.py.md) |
| fluen.models.scan.ScanSelector | external | None | [src/fluen/cli.py](reference/src_fluen_cli.py.md) |
| fluen.orchestrator | external | None | N/A |
| fluen.orchestrator - Orchestrator | external | None | N/A |
| fluen.orchestrator.Orchestrator | external | None | [src/fluen/cli.py](reference/src_fluen_cli.py.md) |
| fluen.state.manager.StateManager | external | None | [src/fluen/analyzer/project_analyzer.py](reference/src_fluen_analyzer_project_analyzer.py.md) |
| generator.doc_generator | external | None | N/A |
| generator.manifest | external | None | N/A |
| generator.templates.template_manager | external | None | N/A |
| git | external | None | [src/fluen/analyzer/file_analyzer.py](reference/src_fluen_analyzer_file_analyzer.py.md) |
| git (from GitPython) | external | None | N/A |
| git_integration.manager.GitDiff | external | None | N/A |
| git_integration.manager.GitManager | external | None | N/A |
| gitpython&gt;=3.1.0 | external | None | N/A |
| iniconfig | external | None | N/A |
| jinja2.ChoiceLoader | external | None | N/A |
| jinja2.Environment | external | None | N/A |
| jinja2.FileSystemLoader | external | None | N/A |
| jinja2.PackageLoader | external | None | N/A |
| jinja2&gt;=3.0.0 | external | None | N/A |
| json | external | None | [src/fluen/analyzer/file_analyzer.py](reference/src_fluen_analyzer_file_analyzer.py.md), [src/fluen/generator/manifest.py](reference/src_fluen_generator_manifest.py.md), [src/fluen/llm_providers/ollama_provider.py](reference/src_fluen_llm_providers_ollama_provider.py.md), [src/fluen/state/manager.py](reference/src_fluen_state_manager.py.md) |
| logging | external | None | [src/fluen/analyzer/file_analyzer.py](reference/src_fluen_analyzer_file_analyzer.py.md), [src/fluen/analyzer/project_analyzer.py](reference/src_fluen_analyzer_project_analyzer.py.md), [src/fluen/generator/doc_generator.py](reference/src_fluen_generator_doc_generator.py.md), [src/fluen/generator/manifest.py](reference/src_fluen_generator_manifest.py.md), [src/fluen/generator/templates/template_manager.py](reference/src_fluen_generator_templates_template_manager.py.md), [src/fluen/git_integration/manager.py](reference/src_fluen_git_integration_manager.py.md), [src/fluen/orchestrator.py](reference/src_fluen_orchestrator.py.md), [src/fluen/state/manager.py](reference/src_fluen_state_manager.py.md) |
| markdown-it-py | external | None | N/A |
| mdurl | external | None | N/A |
| mimetypes | external | None | [src/fluen/analyzer/file_analyzer.py](reference/src_fluen_analyzer_file_analyzer.py.md) |
| mistralai | external | None | [src/fluen/llm_providers/mistral_ai_provider.py](reference/src_fluen_llm_providers_mistral_ai_provider.py.md) |
| mistralai&gt;=0.0.7 | external | None | N/A |
| mypy&gt;=1.0.0 | external | None | N/A |
| openai | external | None | N/A |
| openai.AsyncOpenAI | external | None | N/A |
| openai&gt;=1.0.0 | external | None | N/A |
| os | external | None | N/A |
| packaging | external | None | N/A |
| pathlib | external | None | [src/fluen/analyzer/file_analyzer.py](reference/src_fluen_analyzer_file_analyzer.py.md), [src/fluen/analyzer/project_analyzer.py](reference/src_fluen_analyzer_project_analyzer.py.md), [src/fluen/cli.py](reference/src_fluen_cli.py.md), [src/fluen/config.py](reference/src_fluen_config.py.md), [src/fluen/generator/doc_generator.py](reference/src_fluen_generator_doc_generator.py.md), [src/fluen/git_integration/manager.py](reference/src_fluen_git_integration_manager.py.md), [src/fluen/tests/conftest.py](reference/src_fluen_tests_conftest.py.md) |
| pathlib.Path | external | None | [src/fluen/analyzer/project_analyzer.py](reference/src_fluen_analyzer_project_analyzer.py.md), [src/fluen/cli.py](reference/src_fluen_cli.py.md), [src/fluen/generator/manifest.py](reference/src_fluen_generator_manifest.py.md), [src/fluen/orchestrator.py](reference/src_fluen_orchestrator.py.md), [src/fluen/state/manager.py](reference/src_fluen_state_manager.py.md), [src/fluen/tests/test_file_analyzer.py](reference/src_fluen_tests_test_file_analyzer.py.md), [src/fluen/tests/test_git_manager.py](reference/src_fluen_tests_test_git_manager.py.md) |
| pluggy | external | None | N/A |
| pytest | external | None | [src/fluen/tests/conftest.py](reference/src_fluen_tests_conftest.py.md), [src/fluen/tests/test_file_analyzer.py](reference/src_fluen_tests_test_file_analyzer.py.md), [src/fluen/tests/test_git_manager.py](reference/src_fluen_tests_test_git_manager.py.md) |
| pytest-asyncio | external | None | N/A |
| pytest-asyncio&gt;=0.21.0 | external | None | N/A |
| pytest-cov | external | None | N/A |
| pytest-cov&gt;=4.0.0 | external | None | N/A |
| python-magic | external | None | N/A |
| pyyaml&gt;=6.0 | external | None | N/A |
| re | external | None | [src/fluen/analyzer/file_analyzer.py](reference/src_fluen_analyzer_file_analyzer.py.md) |
| rich | external | None | N/A |
| rich.console | external | None | N/A |
| rich.console - Console | external | None | N/A |
| rich.console.Console | external | None | [src/fluen/cli.py](reference/src_fluen_cli.py.md), [src/fluen/orchestrator.py](reference/src_fluen_orchestrator.py.md) |
| rich.progress | external | None | N/A |
| rich.progress - Progress, SpinnerColumn, TextColumn, BarColumn | external | None | N/A |
| rich.progress.BarColumn | external | None | [src/fluen/cli.py](reference/src_fluen_cli.py.md), [src/fluen/orchestrator.py](reference/src_fluen_orchestrator.py.md) |
| rich.progress.Progress | external | None | [src/fluen/cli.py](reference/src_fluen_cli.py.md), [src/fluen/orchestrator.py](reference/src_fluen_orchestrator.py.md) |
| rich.progress.SpinnerColumn | external | None | [src/fluen/cli.py](reference/src_fluen_cli.py.md), [src/fluen/orchestrator.py](reference/src_fluen_orchestrator.py.md) |
| rich.progress.TaskID | external | None | N/A |
| rich.progress.TextColumn | external | None | [src/fluen/cli.py](reference/src_fluen_cli.py.md), [src/fluen/orchestrator.py](reference/src_fluen_orchestrator.py.md) |
| rich&gt;=10.0.0 | external | None | N/A |
| shutil | external | None | [src/fluen/generator/doc_generator.py](reference/src_fluen_generator_doc_generator.py.md) |
| tempfile | external | None | N/A |
| time | external | None | [src/fluen/analyzer/file_analyzer.py](reference/src_fluen_analyzer_file_analyzer.py.md) |
| tomli | external | None | N/A |
| typing | external | None | [src/fluen/analyzer/file_analyzer.py](reference/src_fluen_analyzer_file_analyzer.py.md), [src/fluen/cli.py](reference/src_fluen_cli.py.md), [src/fluen/config.py](reference/src_fluen_config.py.md), [src/fluen/generator/doc_generator.py](reference/src_fluen_generator_doc_generator.py.md), [src/fluen/git_integration/manager.py](reference/src_fluen_git_integration_manager.py.md), [src/fluen/llm_providers/base_provider.py](reference/src_fluen_llm_providers_base_provider.py.md), [src/fluen/llm_providers/mistral_ai_provider.py](reference/src_fluen_llm_providers_mistral_ai_provider.py.md), [src/fluen/llm_providers/ollama_provider.py](reference/src_fluen_llm_providers_ollama_provider.py.md), [src/fluen/llm_providers/openai_provider.py](reference/src_fluen_llm_providers_openai_provider.py.md), [src/fluen/tests/conftest.py](reference/src_fluen_tests_conftest.py.md) |
| typing - Optional | external | None | N/A |
| typing.Any | external | None | [src/fluen/generator/manifest.py](reference/src_fluen_generator_manifest.py.md), [src/fluen/generator/templates/template_manager.py](reference/src_fluen_generator_templates_template_manager.py.md), [src/fluen/llm_providers/openai_provider.py](reference/src_fluen_llm_providers_openai_provider.py.md), [src/fluen/state/manager.py](reference/src_fluen_state_manager.py.md) |
| typing.Callable | external | None | [src/fluen/analyzer/project_analyzer.py](reference/src_fluen_analyzer_project_analyzer.py.md) |
| typing.Dict | external | None | [src/fluen/analyzer/project_analyzer.py](reference/src_fluen_analyzer_project_analyzer.py.md), [src/fluen/generator/manifest.py](reference/src_fluen_generator_manifest.py.md), [src/fluen/generator/templates/template_manager.py](reference/src_fluen_generator_templates_template_manager.py.md), [src/fluen/llm_providers/openai_provider.py](reference/src_fluen_llm_providers_openai_provider.py.md), [src/fluen/state/manager.py](reference/src_fluen_state_manager.py.md) |
| typing.List | external | None | [src/fluen/analyzer/project_analyzer.py](reference/src_fluen_analyzer_project_analyzer.py.md), [src/fluen/llm_providers/openai_provider.py](reference/src_fluen_llm_providers_openai_provider.py.md) |
| typing.Optional | external | None | [src/fluen/analyzer/project_analyzer.py](reference/src_fluen_analyzer_project_analyzer.py.md), [src/fluen/cli.py](reference/src_fluen_cli.py.md), [src/fluen/generator/manifest.py](reference/src_fluen_generator_manifest.py.md), [src/fluen/orchestrator.py](reference/src_fluen_orchestrator.py.md), [src/fluen/state/manager.py](reference/src_fluen_state_manager.py.md) |
| typing.Set | external | None | [src/fluen/analyzer/project_analyzer.py](reference/src_fluen_analyzer_project_analyzer.py.md) |
| typing_extensions | external | None | N/A |
| unittest.mock.AsyncMock | external | None | N/A |
| unittest.mock.Mock | external | None | N/A |
| yaml | external | None | N/A |
| {{ dep.name }} | external | None | N/A |

## Navigation

- [Summary](SUMMARY.md)
- [Reference Documentation](reference/)