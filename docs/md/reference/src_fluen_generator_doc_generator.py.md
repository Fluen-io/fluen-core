# src/fluen/generator/doc_generator.py

**Language:** Python  
**Last Modified:** 2024-11-13T17:49:20.875382

## Purpose

The primary purpose of this code is to generate project documentation in HTML and Markdown formats. It uses a templating system to create structured documentation based on project manifests.

## Public API

- `DocumentationGenerator` (exposure)
- `BaseFormatGenerator` (exposure)
- `HTMLGenerator` (exposure)
- `MarkdownGenerator` (exposure)

## Dependencies

- `json` (external)
- `pathlib.Path` (external)
- `shutil` (external)
- `logging` (external)
- `fluen.generator.templates.template_manager.TemplateManager` (external)
- `fluen.generator.manifest.ManifestGenerator` (external)
- `fluen.generator.manifest.ProjectManifest` (external)
- `fluen.generator.manifest.ElementReference` (external)

## Elements

### Class

#### `BaseFormatGenerator`

**Scope:** public

**Purpose:** Abstract base class for format-specific documentation generators.

**Documentation:**

Provides a common interface and shared functionality for HTML and Markdown generators, including manifest management and logging.

#### `DocumentationGenerator`

**Scope:** public

**Purpose:** Coordinates the generation of documentation in various formats.

**Documentation:**

This class initializes with a project manifest, output directory, template manager, and manifest generator and manages the generation process for specified formats.

#### `HTMLGenerator`

**Scope:** public

**Purpose:** Generates HTML documentation.

**Documentation:**

Extends BaseFormatGenerator to implement HTML-specific documentation generation, including creating directory structures and rendering templates.

#### `MarkdownGenerator`

**Scope:** public

**Purpose:** Generates Markdown documentation.

**Documentation:**

Extends BaseFormatGenerator to implement Markdown-specific documentation generation, including creating directory structures and rendering templates.

### Method

#### `__init__`

**Scope:** private

**Purpose:** Constructor for DocumentationGenerator to initialize instance variables.

**Documentation:**

Initializes the documentation generator with given parameters for manifest, output directory, template manager, and manifest generator.

#### `__init__`

**Scope:** private

**Purpose:** Constructor for BaseFormatGenerator to initialize instance variables.

**Documentation:**

Initializes the base generator with given parameters for manifest, output directory, template manager, and optionally, a manifest generator.

#### `_copy_static_assets`

**Scope:** private

**Purpose:** Copies static assets to output directory.

**Documentation:**

Copies CSS and JavaScript assets from the templates directory to the designated HTML assets directory.

#### `_generate_empty_documentation`

**Scope:** private

**Purpose:** Generates documentation for an empty project.

**Documentation:**

Creates an HTML page indicating that there are no files to document, using a default template for empty projects.

#### `_generate_index_page`

**Scope:** private

**Purpose:** Generates the main index HTML page.

**Documentation:**

Renders the main index page template using the manifest and writes it to the output directory as an HTML file.

#### `_generate_readme`

**Scope:** private

**Purpose:** Generates the main Markdown README file.

**Documentation:**

Renders and writes a Markdown README file using template data derived from the project manifest.

#### `_generate_reference_docs`

**Scope:** private

**Purpose:** Generates reference Markdown documents.

**Documentation:**

Creates Markdown files for each file in the manifest, detailing code elements and any additional context data.

#### `_generate_reference_pages`

**Scope:** private

**Purpose:** Generates individual reference HTML pages.

**Documentation:**

Creates specific HTML reference pages for each file in the manifest, rendering templates with relationships and element data.

#### `_generate_summary`

**Scope:** private

**Purpose:** Generates a summary Markdown document.

**Documentation:**

Compiles and writes a SUMMARY.md file to assist in navigation for rendered Markdown documentation.

#### `_get_generator`

**Scope:** private

**Purpose:** Selects the appropriate generator based on the format type.

**Documentation:**

Helper method to return an instance of either HTMLGenerator or MarkdownGenerator based on the specified format type.

#### `_group_elements_by_type`

**Scope:** private

**Purpose:** Groups elements by their type.

**Documentation:**

Organizes code elements by type to facilitate structured documentation and rendering.

#### `_group_files_by_type`

**Scope:** private

**Purpose:** Groups files by their programming language.

**Documentation:**

Organizes files in the manifest by their declared language/type for easier indexing and documentation.

#### `generate`

**Scope:** public

**Purpose:** Generates documentation in the specified format.

**Documentation:**

Asynchronously generates documentation based on the specified format (HTML or Markdown) using the provided manifest and templates.

#### `generate`

**Scope:** public

**Purpose:** Abstract method to generate documentation in specific format.

**Documentation:**

Designed to be overridden by subclasses to implement format-specific documentation generation logic.

#### `generate`

**Scope:** public

**Purpose:** Generates HTML documentation.

**Documentation:**

Asynchronously creates directories, copies assets, and generates index and reference pages using the template manager.

#### `generate`

**Scope:** public

**Purpose:** Generates Markdown documentation.

**Documentation:**

Asynchronously creates directories and generates README, reference documents, and a summary for navigation in Markdown format.


[Back to Index](../README.md)