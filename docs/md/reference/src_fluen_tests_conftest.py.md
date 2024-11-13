# src/fluen/tests/conftest.py

**Language:** Python  
**Last Modified:** 2024-11-13T17:54:34.183543

## Purpose

This code provides PyTest fixtures for setting up testing environments such as temporary file systems, sample Git repositories, and mock configurations.

## Public API

- `temp_dir` (exposure)
- `sample_repo` (exposure)
- `mock_config` (exposure)

## Dependencies

- `pytest` (external)
- `pathlib` (external)
- `tempfile` (external)
- `shutil` (external)
- `git` (external)
- `typing` (external)
- `config` (external)

## Elements

### Class

#### `FluenConfig`

**Scope:** external dependency

**Purpose:** Configuration class used within the mock_config fixture.

**Documentation:**

Represents application configurations, presumably imported from the config module.

#### `LLMConfig`

**Scope:** external dependency

**Purpose:** Configuration class for LLM provider details used within mock_config.

**Documentation:**

Holds details about the LLM service provider and model information, imported from the config module.

### Function

#### `mock_config`

**Scope:** module-level

**Purpose:** Creates a mock configuration object for testing.

**Documentation:**

This fixture returns a FluenConfig instance initialized with a mock LLMConfig and various directory paths.

#### `sample_repo`

**Scope:** module-level

**Purpose:** Creates a sample Git repository within a temporary directory for testing purposes.

**Documentation:**

This fixture initializes a Git repository, populates it with sample files and commits, then yields the directory Path.

#### `temp_dir`

**Scope:** module-level

**Purpose:** Provides a temporary directory for tests.

**Documentation:**

This fixture sets up a temporary directory using Python&#39;s tempfile module and yields the Path object of the directory, ensuring cleanup afterwards.


[Back to Index](../README.md)