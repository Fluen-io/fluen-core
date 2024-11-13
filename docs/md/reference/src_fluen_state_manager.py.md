# src/fluen/state/manager.py

**Language:** Python  
**Last Modified:** 2024-11-13T17:51:57.210903

## Purpose

This module manages the state of a documentation generation process, allowing for saving, loading, and updating the state related to documentation tasks.

## Public API

- `DocumentationState` (exposure)
- `StateManager` (exposure)
- `load` (exposure)
- `save` (exposure)
- `update_progress` (exposure)
- `update_commit` (exposure)
- `set_manifest_path` (exposure)

## Dependencies

- `json` (external)
- `pathlib.Path` (external)
- `dataclasses.dataclass` (external)
- `dataclasses.asdict` (external)
- `typing.Optional` (external)
- `typing.Dict` (external)
- `typing.Any` (external)
- `logging` (external)

## Elements

### Class

#### `DocumentationState`

**Scope:** global

**Purpose:** Represents the state of the documentation process.

**Documentation:**

A dataclass to store state attributes like commit hash, timestamp of last run, number of files processed, total files, and manifest path.

#### `StateManager`

**Scope:** global

**Purpose:** Responsible for managing and persisting documentation process state.

**Documentation:**

Provides functionality to load and save the documentation state, and update various pieces of state data like files processed, commit hash, and manifest path.

### Method

#### `__init__`

**Scope:** StateManager

**Purpose:** Initializes a StateManager instance.

**Documentation:**

Initializes the StateManager with a given state directory, sets up logging, and creates a default DocumentationState object.

#### `load`

**Scope:** StateManager

**Purpose:** Loads state from a file.

**Documentation:**

Attempts to load state data from the &#39;state.json&#39; file into the current_state. If loading fails, returns a fresh DocumentationState object.

#### `save`

**Scope:** StateManager

**Purpose:** Saves the current state to a file.

**Documentation:**

Dumps the current state data as a JSON object into the &#39;state.json&#39; file, creating necessary directories if missing.

#### `set_manifest_path`

**Scope:** StateManager

**Purpose:** Sets the manifest file path.

**Documentation:**

Updates the manifest_path field with the given path and saves the current state.

#### `update_commit`

**Scope:** StateManager

**Purpose:** Updates the last commit processed.

**Documentation:**

Sets the last_commit field in the current state and saves it.

#### `update_progress`

**Scope:** StateManager

**Purpose:** Updates the file processing progress.

**Documentation:**

Updates the number of files processed and the total number of files in the current state, then saves the state.

### Variable

#### `current_state`

**Scope:** StateManager

**Purpose:** Stores the current documentation state.

**Documentation:**

An instance of DocumentationState holding the state data currently in use.

#### `files_processed`

**Scope:** DocumentationState

**Purpose:** Tracks the number of files processed.

**Documentation:**

An integer to count how many files have been processed in the documentation run.

#### `last_commit`

**Scope:** DocumentationState

**Purpose:** Stores the last commit hash processed.

**Documentation:**

An optional string to track the last processed commit hash in the documentation process.

#### `last_run_timestamp`

**Scope:** DocumentationState

**Purpose:** Stores the timestamp of the last run.

**Documentation:**

An optional float that captures the timestamp of the last run of the documentation process.

#### `logger`

**Scope:** StateManager

**Purpose:** Handles logging for the StateManager.

**Documentation:**

A logger object used for logging debug and error information within the StateManager.

#### `manifest_path`

**Scope:** DocumentationState

**Purpose:** Stores path to the generated manifest file.

**Documentation:**

An optional string that holds the path to the manifest file created during documentation generation.

#### `state_file`

**Scope:** StateManager

**Purpose:** Stores the path to the state file.

**Documentation:**

A Path object representing the location of the state file within the state directory.

#### `total_files`

**Scope:** DocumentationState

**Purpose:** Stores the total number of files to process.

**Documentation:**

An integer indicating the total number of files expected in the documentation process.


[Back to Index](../README.md)