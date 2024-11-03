# src/fluen/analyzer/project_analyzer.py

**Language:** Python  
**Last Modified:** 2024-11-03T10:07:35.327673

## Purpose

The code provides a mechanism for analyzing a software project, performing either a full analysis or an incremental analysis based on recent file changes, and updates the project&#39;s manifest accordingly.

## Public API

- `ProjectAnalyzer` (exposure)
- `ProjectAnalyzer.__init__` (exposure)
- `ProjectAnalyzer.analyze` (exposure)
- `ProjectAnalyzer._analyze_batch` (exposure)
- `ProjectAnalyzer._perform_full_analysis` (exposure)
- `ProjectAnalyzer._perform_incremental_update` (exposure)
- `ProjectAnalyzer._get_analyzable_files` (exposure)
- `ProjectAnalyzer._analyze_file` (exposure)

## Dependencies

- `pathlib.Path` (external)
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

#### `__init__`

**Scope:** ProjectAnalyzer

**Purpose:** No purpose specified

**Documentation:**

No documentation available

#### `_analyze_batch`

**Scope:** ProjectAnalyzer

**Purpose:** No purpose specified

**Documentation:**

No documentation available

#### `_analyze_file`

**Scope:** ProjectAnalyzer

**Purpose:** No purpose specified

**Documentation:**

No documentation available

#### `_get_analyzable_files`

**Scope:** ProjectAnalyzer

**Purpose:** No purpose specified

**Documentation:**

No documentation available

#### `_perform_full_analysis`

**Scope:** ProjectAnalyzer

**Purpose:** No purpose specified

**Documentation:**

No documentation available

#### `_perform_incremental_update`

**Scope:** ProjectAnalyzer

**Purpose:** No purpose specified

**Documentation:**

No documentation available

#### `analyze`

**Scope:** ProjectAnalyzer

**Purpose:** No purpose specified

**Documentation:**

No documentation available

### Variable

#### `batch_delay`

**Scope:** ProjectAnalyzer

**Purpose:** No purpose specified

**Documentation:**

No documentation available

#### `batch_size`

**Scope:** ProjectAnalyzer

**Purpose:** No purpose specified

**Documentation:**

No documentation available


[Back to Index](../README.md)