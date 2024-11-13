# src/fluen/cli.py

**Language:** Python  
**Last Modified:** 2024-11-13T17:52:16.642966

## Purpose

This code defines a command-line interface (CLI) application using Click, designed to handle documentation generation and export tasks for a codebase, leveraging configuration data and interacting with a progression-enabled console output.

## Public API

- `cli` (exposure)
- `docs` (exposure)
- `generate` (exposure)
- `export` (exposure)

## Dependencies

- `click` (external)
- `pathlib` (external)
- `typing` (external)
- `fluen.config.FluenConfig` (external)
- `rich.console.Console` (external)
- `rich.progress.Progress` (external)
- `fluen.orchestrator.Orchestrator` (external)
- `fluen.models.scan.ScanSelector` (external)
- `fluen.models.scan.ScanOptions` (external)
- `asyncio` (external)
- `fluen.generator.doc_generator.DocumentationGenerator` (external)
- `fluen.generator.templates.template_manager.TemplateManager` (external)
- `fluen.generator.manifest.ManifestGenerator` (external)

## Elements

### Class

#### `FluenContext`

**Scope:** global

**Purpose:** Stores the configuration, console, and scan options relevant to the Fluen CLI commands.

**Documentation:**

A context object used in Click to maintain state across CLI commands. It initializes with a configuration file path, a console for rich text output, and optional scan options.

### Function

#### `cli`

**Scope:** global

**Purpose:** Root command group for the CLI tool.

**Documentation:**

Defines the main command group for the CLI application. It sets up the configuration based on user input or default values.

#### `docs`

**Scope:** cli

**Purpose:** Sub-command group for documentation related commands.

**Documentation:**

Serves as a parent group for documentation commands like &#39;generate&#39; and &#39;export&#39;.

#### `export`

**Scope:** docs

**Purpose:** Exports generated documentation into specified formats like HTML or Markdown.

**Documentation:**

Manages the exportation of documentation based on a manifest, using a progress bar to indicate stages such as manifest loading, template initialization, and export generation.

#### `generate`

**Scope:** docs

**Purpose:** Generates documentation for the provided codebase and outputs progress.

**Documentation:**

Handles the generation of documentation, managing repository and scan options. Utilizes an orchestrator for the generation process and provides progress updates via rich console.

### Variable

#### `pass_fluen_context`

**Scope:** global

**Purpose:** Decorator to pass FluenContext instance to Click command functions.

**Documentation:**

This Click decorator passes a FluenContext object to functions, ensuring an instance is available for command operations.


[Back to Index](../README.md)