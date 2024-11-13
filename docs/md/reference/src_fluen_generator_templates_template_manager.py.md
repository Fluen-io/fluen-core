# src/fluen/generator/templates/template_manager.py

**Language:** Python  
**Last Modified:** 2024-11-13T17:52:32.533661

## Purpose

The primary purpose of this code is to manage a template system for documentation generation using Jinja2 templates.

## Public API

- `TemplateManager` (exposure)

## Dependencies

- `pathlib` (external)
- `typing` (external)
- `jinja2` (external)
- `logging` (external)

## Elements

### Class

#### `TemplateManager`

**Scope:** public

**Purpose:** Manage the Jinja2 environment and render templates for documentation generation.

**Documentation:**

This class sets up template loaders, registers custom filters, and provides methods to render templates and get default context for template rendering.

### Method

#### `__init__`

**Scope:** private

**Purpose:** Initialize the TemplateManager with custom or default template directory and prepare the Jinja environment.

**Documentation:**

The initializer sets up the template loaders, configures the environment with autoescaping and block trimming options, and registers custom filters for templates.

#### `_detect_language`

**Scope:** private

**Purpose:** Determine the programming language based on the file extension for syntax highlighting.

**Documentation:**

This method uses a mapping of file extensions to language names to detect and return the appropriate language for syntax highlighting in templates.

#### `_register_filters`

**Scope:** private

**Purpose:** Register custom Jinja2 filters for use in templates.

**Documentation:**

This method adds custom filters to the Jinja environment such as &#39;format_type&#39;, &#39;anchor_id&#39;, and &#39;code_language&#39;.

#### `get_default_context`

**Scope:** public

**Purpose:** Provide a default context for templates based on the ProjectManifest.

**Documentation:**

This method generates a default context dictionary using information from the ProjectManifest, including project details, generation time, and git commit.

#### `render_template`

**Scope:** public

**Purpose:** Render a Jinja2 template using the provided context.

**Documentation:**

This method retrieves a template by name, renders it with the provided context, and returns the rendered template as a string. It logs an error and raises an exception if rendering fails.

### Variable

#### `env`

**Scope:** private

**Purpose:** Jinja2 environment instance for managing templates.

**Documentation:**

This instance of jinja2.Environment is configured with custom loaders and filter registrations to manage and render templates.

#### `logger`

**Scope:** private

**Purpose:** Log system for the TemplateManager to record errors and important events.

**Documentation:**

A logging.Logger instance initialized with the module&#39;s name for tracking operations and errors within the TemplateManager.


[Back to Index](../README.md)