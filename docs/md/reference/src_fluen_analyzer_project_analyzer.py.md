# src/fluen/analyzer/project_analyzer.py

**Language:** Python  
**Last Modified:** 2024-11-12T20:03:09.037153

## Purpose

The code provides functionality for analyzing a software project at a project level. It handles both full project analysis and incremental updates using Git changes, coordinating file level analysis and manifest updating.

## Public API

- `ProjectAnalyzer.__init__` (exposure)
- `ProjectAnalyzer.analyze` (exposure)
- `ProjectAnalyzer.analyze_path` (exposure)

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

**Scope:** global

**Purpose:** No purpose specified

**Documentation:**

No documentation available

### Method

#### `ProjectAnalyzer.__init__`

**Scope:** class

**Purpose:** No purpose specified

**Documentation:**

No documentation available

#### `ProjectAnalyzer._analyze_batch`

**Scope:** private

**Purpose:** No purpose specified

**Documentation:**

No documentation available

#### `ProjectAnalyzer._analyze_file`

**Scope:** private

**Purpose:** No purpose specified

**Documentation:**

No documentation available

#### `ProjectAnalyzer._get_analyzable_files`

**Scope:** private

**Purpose:** No purpose specified

**Documentation:**

No documentation available

#### `ProjectAnalyzer._perform_full_analysis`

**Scope:** private

**Purpose:** No purpose specified

**Documentation:**

No documentation available

#### `ProjectAnalyzer._perform_incremental_update`

**Scope:** private

**Purpose:** No purpose specified

**Documentation:**

No documentation available

#### `ProjectAnalyzer.analyze`

**Scope:** class

**Purpose:** No purpose specified

**Documentation:**

No documentation available

#### `ProjectAnalyzer.analyze_path`

**Scope:** class

**Purpose:** No purpose specified

**Documentation:**

No documentation available


[Back to Index](../README.md)