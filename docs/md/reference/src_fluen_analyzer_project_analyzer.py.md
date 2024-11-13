# src/fluen/analyzer/project_analyzer.py

**Language:** Python  
**Last Modified:** 2024-11-13T17:59:05.370177

## Purpose

Analyzes project files and manages full or incremental analysis based on git changes and state management.

## Public API

- `ProjectAnalyzer` (exposure)

## Dependencies

- `pathlib.Path` (external)
- `typing.Callable` (external)
- `typing.Dict` (external)
- `typing.List` (external)
- `typing.Optional` (external)
- `typing.Set` (external)
- `asyncio` (external)
- `logging` (external)
- `fluen.git_integration.manager.GitManager` (external)
- `fluen.state.manager.StateManager` (external)
- `fluen.analyzer.file_analyzer.FileAnalysis` (external)
- `fluen.analyzer.file_analyzer.FileAnalyzer` (external)
- `fluen.generator.manifest.ManifestGenerator` (external)

## Elements

### Class

#### `ProjectAnalyzer`

**Scope:** module

**Purpose:** Handles project-level analysis, including both full and incremental, based on file changes detected through git.

**Documentation:**

This class coordinates analysis of files in a project directory, utilizing git to identify change sets and state management for tracking progress. It uses batching and asyncio for efficient analysis operations.

### Method

#### `__init__`

**Scope:** class

**Purpose:** Initializes the ProjectAnalyzer with required managers and settings.

**Documentation:**

Sets up the initial state for ProjectAnalyzer, including the project root path and several manager instances for git management, state management, file analysis, and manifest generation. Optionally takes a callback for progress updates.

#### `_analyze_batch`

**Scope:** class

**Purpose:** Analyzes a batch of files asynchronously with rate limiting.

**Documentation:**

Handles analysis of a batch of files, potentially using async rate limiting to manage performance, and returns analysis results for each file.

#### `_analyze_file`

**Scope:** class

**Purpose:** Analyzes a single file and returns the analysis result.

**Documentation:**

Asynchronously analyzes a given file path and returns the analysis outcome if successful, while handling exceptions.

#### `_get_analyzable_files`

**Scope:** class

**Purpose:** Retrieves a set of files to analyze from the project directory, excluding certain patterns.

**Documentation:**

Scans the project directory and returns files suitable for analysis, ignoring certain patterns like cache files, git directories, and virtual environments.

#### `_get_changed_files`

**Scope:** class

**Purpose:** Determines which files have changed since the last commit.

**Documentation:**

Uses git history to identify files that changed since the last stored commit and only returns these for analysis, unless errors occur.

#### `_perform_full_analysis`

**Scope:** class

**Purpose:** Executes a full analysis of the entire project directory.

**Documentation:**

Collects all relevant project files and performs a thorough analysis in batches, updating the manifest and progress state accordingly. Handles the main entry point for a full scan.

#### `_perform_incremental_update`

**Scope:** class

**Purpose:** Updates analysis results incrementally based on detected git changes.

**Documentation:**

Focuses on files added or modified since the last successful analysis commit and updates the manifest with updated analysis information.

#### `analyze`

**Scope:** class

**Purpose:** Performs full project analysis or an incremental update based on git status.

**Documentation:**

This asynchronous method determines if a full analysis of the project is needed or if an incremental update suffices based on changes detected since the last analysis.

#### `analyze_path`

**Scope:** class

**Purpose:** Analyzes a specific path, either a file or directory, with git-based change detection.

**Documentation:**

This method allows analyzing specific paths, adhering to git changes for optimization unless forced, and updates analysis results accordingly.


[Back to Index](../README.md)