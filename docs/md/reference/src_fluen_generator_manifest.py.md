# src/fluen/generator/manifest.py

**Language:** Python  
**Last Modified:** 2024-11-13T17:54:26.635081

## Purpose

The primary purpose of this code is to generate a manifest file for a project, which includes detailed information about files, their dependencies, relationships, and other metadata. This manifest can be saved in both JSON and JSONP formats.

## Public API

- `ManifestGenerator` (exposure)
- `DependencyInfo` (exposure)
- `ElementReference` (exposure)
- `FileRelationships` (exposure)
- `FileManifest` (exposure)
- `ProjectManifest` (exposure)

## Dependencies

- `pathlib.Path` (external)
- `typing.Dict` (external)
- `typing.List` (external)
- `typing.Any` (external)
- `typing.Optional` (external)
- `typing.Set` (external)
- `dataclasses.dataclass` (external)
- `dataclasses.asdict` (external)
- `json` (external)
- `logging` (external)
- `datetime.datetime` (external)
- `fluen.analyzer.file_analyzer.FileAnalysis` (external)

## Elements

### Class

#### `DependencyInfo`

**Scope:** global

**Purpose:** Represents a dependency with information such as name, type, version, and usage across files.

**Documentation:**

Stores the details of a dependency, including which files use it.

#### `ElementReference`

**Scope:** global

**Purpose:** Represents a code element reference, including details like name, type, file path, line number, etc.

**Documentation:**

Used to track different elements within the files such as functions, classes, or variables.

#### `FileManifest`

**Scope:** global

**Purpose:** Represents metadata about a file, including its path, language, purpose, dependencies, and relationships with other files.

**Documentation:**

Holds detailed information about a single file in the context of the project.

#### `FileRelationships`

**Scope:** global

**Purpose:** Tracks the relationships of a file with other files, including which files it depends on and which files depend on it.

**Documentation:**

Maintains a record of imports and dependencies for each file.

#### `ManifestGenerator`

**Scope:** global

**Purpose:** Handles the creation, updating, and saving of project manifests.

**Documentation:**

This is the core class responsible for managing the project manifest lifecycle, including initialization, updates, and saving.

#### `ProjectManifest`

**Scope:** global

**Purpose:** Stores the entire project metadata, including language, frameworks, files, dependencies, and more.

**Documentation:**

Collects comprehensive data about the project, combining individual file manifests.

### Method

#### `__init__`

**Scope:** ManifestGenerator

**Purpose:** Initializes the ManifestGenerator with project and output directories.

**Documentation:**

Sets up paths and logger for managing the manifest.

#### `_get_display_name`

**Scope:** ManifestGenerator

**Purpose:** Provides a shortened display name for a file path.

**Documentation:**

Transforms full file paths into simpler, more readable strings for display purposes.

#### `_resolve_dependencies`

**Scope:** ManifestGenerator

**Purpose:** Resolves file dependencies, especially relative imports, into concrete file paths.

**Documentation:**

Converts relative import paths into absolute ones that can be mapped within the project structure.

#### `_update_project_information`

**Scope:** ManifestGenerator

**Purpose:** Updates project-level metadata based on file manifest information.

**Documentation:**

Adjusts overarching project details such as primary language and framework usage with new file data.

#### `_update_relationships`

**Scope:** ManifestGenerator

**Purpose:** Maintains the file dependency graph by updating dependencies for a given file path.

**Documentation:**

Updates the internal relationship graph to reflect dependencies and dependents for a file.

#### `add_file_analysis`

**Scope:** ManifestGenerator

**Purpose:** Adds or updates the analysis of a file in the project manifest and tracks relationships.

**Documentation:**

Incorporates file analysis results into the project manifest, updating file and project-level metadata.

#### `get_file_relationships`

**Scope:** ManifestGenerator

**Purpose:** Retrieves relationship data for a specific file.

**Documentation:**

Returns a structured representation of how a file relates to others in terms of dependencies and dependents.

#### `initialize_manifest`

**Scope:** ManifestGenerator

**Purpose:** Creates a new ProjectManifest instance with given project name and git commit.

**Documentation:**

Sets up the initial manifest structure for a project to start adding files and dependencies.

#### `load_existing_manifest`

**Scope:** ManifestGenerator

**Purpose:** Attempts to load an existing manifest from disk.

**Documentation:**

Checks for an existing manifest file and loads its content into the ProjectManifest instance.

#### `save`

**Scope:** ManifestGenerator

**Purpose:** Saves the current project manifest in both JSON and JSONP formats.

**Documentation:**

Writes the manifest to disk, ensuring directories are present and formats are correctly structured.


[Back to Index](../README.md)