# README.md

**Language:** Unknown  
**Last Modified:** 2024-11-13T17:48:10.548287

## Purpose

Fluen is a documentation generator powered by LLMs (Large Language Models). It creates intelligent documentation by analyzing git repositories to capture the structure, intent, and relationships within the codebase.

## Public API

- `fluen.docs.generate` (exposure)
- `fluen.docs.export` (exposure)
- `fluen_config.yml` (exposure)

## Dependencies

- `Python 3.9+` (external)
- `Git` (external)
- `An API key from OpenAI or Mistral AI` (external)
- `Jiva Framework` (external)
- `Claude by Anthropic` (external)

## Elements

### Command

#### `fluen docs export`

**Scope:** CLI Command

**Purpose:** Exports generated documentation in the specified format.

**Documentation:**

Translates the manifest.json into documentation formats like HTML or Markdown. The format can be specified directly via command line arguments.

#### `fluen docs generate`

**Scope:** CLI Command

**Purpose:** Analyzes the project and generates a code manifest.json file.

**Documentation:**

This command is used to scan a git repository and create a comprehensive manifest describing the project&#39;s code structure, purpose, and relationships.

### Configuration File

#### `fluen_config.yml`

**Scope:** Configuration

**Purpose:** Configures the Fluen tool, specifying LLM provider settings and output preferences.

**Documentation:**

This YAML file includes settings such as the LLM provider, API key, model, and output directory for generated documentation.


[Back to Index](../README.md)