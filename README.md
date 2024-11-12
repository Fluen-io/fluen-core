# Fluen: AI-Powered Code Documentation Generator

[![Build Status](https://github.com/Fluen-io/fluen-core/actions/workflows/build.yml/badge.svg)](https://github.com/Fluen-io/fluen-core/actions)
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)

Fluen is a modern, LLM-powered documentation generator that understands your code. Point it at any git repository, and it will create comprehensive, intelligent documentation that captures not just the structure, but the intent and relationships within your codebase.

## ✨ Features

- **Language Agnostic**: Works with any programming language - understands patterns, idioms, and best practices across different languages
- **Intelligent Analysis**: Uses LLMs to understand code purpose, relationships, and architectural patterns
- **Git Integration**: Works with any git repository, tracks changes, and updates documentation incrementally
- **Rich Documentation**: Generates both HTML and Markdown documentation with:
  - Cross-referenced code elements
  - Dependency graphs
  - Public API documentation
  - Code purpose analysis
  - Framework detection

## 🚀 Quick Start

1. Install Fluen:
```bash
pip install fluen
```

2. Create a configuration file:
```bash
# Copy the example config
cp fluen_config.example.yml fluen_config.yml

# Edit the config file with your LLM provider settings
vim fluen_config.yml
```

3. Generate documentation:
The generate command analyzes the project and generates a code manifest.json file. We recommend you to first clone a repository and then run fluen from the root of your local repository.

```bash
# For local repository
fluen docs generate

# For remote repository
fluen docs generate --repo https://github.com/username/repo.git
```

Once the manifest.json generation succeeds, run the export command to export in html or markdown format

```bash
# Default export type configured in fluen_config.yml
fluen docs export

# Explicitly tell the export format type html/md
fluen docs export --type md
```

4. View your documentation:
```bash
# Documentation will be available in ./docs directory
open docs/html/index.html
```

5. Update your documentation
Fluen is designed to update documentation incrementally with git commits. However there might be scenarios where you need to fore an update. Simply use the `--force` flag
```bash
fluen docs generate --force
```

6. Selective scanning (of sub directories)
In case you want Fluen to look at only a specific sub-directory, then use the `--scan` flag
```bash
fluen docs generate --scan path:<your_sub_path>
```
You may use the `--force` flag to force updates
## 📖 Use Cases

### 1. Project Onboarding
Help new team members understand your codebase quickly with AI-generated documentation that explains not just what the code does, but why it does it.

### 2. Code Audits
Get a comprehensive view of your project's architecture, dependencies, and exposed APIs. Perfect for security audits and architectural reviews.

### 3. Technical Documentation
Generate and maintain up-to-date technical documentation without manual effort. Fluen tracks changes and updates only what's needed.

### 4. Legacy Code Understanding
Make sense of legacy codebases by letting Fluen analyze patterns, dependencies, and architectural decisions embedded in the code.

## ⚙️ Configuration

Fluen uses a YAML configuration file (`fluen_config.yml`) for customization. Here's a minimal configuration:

```yaml
llm:
  # Choose your provider: 'openai' or 'mistral' or 'ollama' for local use
  provider: openai
  api_key: your-api-key-here
  model: gpt-3.5-turbo  # or 'gpt-4o' for better results

# Output directory for generated documentation
output_dir: docs

# Documentation format
default_export_type: html  # or 'md' for markdown
```

See `fluen_config.example.yml` for a complete configuration example with all available options.

## 🔧 Requirements

- Python 3.9 or higher
- Git
- An API key from OpenAI or Mistral AI (recommended providers)

## 🚧 Roadmap

Exciting features coming soon:
- Interactive code chat interface with project-wide search
- Enhanced code element descriptions and relationships
- PDF export
- Custom template support
- Plugin system
- CI/CD integration

## 🤝 Contributing

We welcome contributions! Whether it's bug reports, feature requests, or code contributions, please feel free to contribute.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Install development dependencies:
```bash
pip install -e ".[dev]"
```
4. Make your changes
5. Run tests:
```bash
pytest
```
6. Submit a Pull Request

## 📄 License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

## 🙋‍♂️ Support

- 📄 [Documentation](https://github.com/Fluen-io/fluen-core/wiki)
- 🐛 [Issue Tracker](https://github.com/Fluen-io/fluen-core/issues)
- 💬 [Discussions](https://github.com/Fluen-io/fluen-core/discussions)

## 🌟 Show your support

Give a ⭐️ if this project helped you!

---
Made with ❤️ by [Fluen](https://github.com/Fluen-io) using the [Jiva Framework](https://github.com/KarmaloopAI/Jiva) and Claude by [Anthropic](https://www.anthropic.com/)