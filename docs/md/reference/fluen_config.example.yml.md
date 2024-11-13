# fluen_config.example.yml

**Language:** Unknown  
**Last Modified:** 2024-11-13T17:47:28.482281

## Purpose

Configuration file for the Fluen code documentation generator, allowing users to specify settings related to LLM provider selection, documentation output formats, caching, and project-specific configurations.

## Public API

- `llm:provider` (exposure)
- `llm:api_key` (exposure)
- `llm:model` (exposure)
- `output_dir` (exposure)
- `cache_dir` (exposure)
- `temp_dir` (exposure)
- `default_export_type` (exposure)
- `project:name` (exposure)
- `project:description` (exposure)
- `project:ignore_patterns` (exposure)

## Dependencies

- `OpenAI API` (external)
- `Mistral API` (external)
- `Ollama API` (external)

## Elements

### Variable

#### `api_key`

**Scope:** llm

**Purpose:** Holds the API key for authentication with the chosen LLM provider.

**Documentation:**

Users are required to enter their API key for the selected provider to enable access to the LLM services.

#### `cache_dir`

**Scope:** global

**Purpose:** Defines the directory for storing cache files.

**Documentation:**

Used to store intermediate analysis results to speed up subsequent operations.

#### `default_export_type`

**Scope:** global

**Purpose:** Sets the default format for documentation output.

**Documentation:**

Users can choose between &#39;html&#39; and &#39;md&#39; formats based on their needs for documentation presentation.

#### `description`

**Scope:** project

**Purpose:** Provides a brief description of the project.

**Documentation:**

Descriptive text about the project to give context to users or integrators.

#### `ignore_patterns`

**Scope:** project

**Purpose:** Lists files and directories to ignore during processing.

**Documentation:**

Patterns matching files or directories that should be excluded from analysis, useful for ignoring build artifacts or configuration files.

#### `llm`

**Scope:** global

**Purpose:** Configuration object for specifying LLM provider details.

**Documentation:**

This object holds specific configurations for different LLM providers such as OpenAI, Mistral, or Ollama, including provider type, API keys, and model selections.

#### `model`

**Scope:** llm

**Purpose:** Defines the model to be used with the selected LLM provider.

**Documentation:**

Different models can be specified based on provider and use case needs. Possible values include &#39;gpt-3.5-turbo&#39;, &#39;gpt-4&#39;, &#39;mistral-small-latest&#39;, etc.

#### `name`

**Scope:** project

**Purpose:** Defines the name of the project.

**Documentation:**

Serves as an identifier for the project within the Fluen tool.

#### `output_dir`

**Scope:** global

**Purpose:** Specifies the directory for documentation output files.

**Documentation:**

The path where generated documentation will be stored. Users can customize this to match their project structure.

#### `project`

**Scope:** global

**Purpose:** Encapsulates project-specific settings.

**Documentation:**

Contains metadata about the project including name, description, and ignore patterns to exclude certain files/directories from processing.

#### `provider`

**Scope:** llm

**Purpose:** Specifies the LLM provider to be used.

**Documentation:**

Allows selection among &#39;openai&#39;, &#39;mistral&#39;, or &#39;ollama&#39;. Users should uncomment the relevant lines based on the chosen provider.

#### `temp_dir`

**Scope:** global

**Purpose:** Defines the directory for storing temporary files.

**Documentation:**

Temporary processing files are stored here and can be cleaned regularly to free up space.


[Back to Index](../README.md)