# src/fluen/git_integration/manager.py

**Language:** Python  
**Last Modified:** 2024-11-13T17:47:58.174156

## Purpose

The primary purpose of this code is to provide functionality for managing and analyzing Git repositories, including initialization, cloning, and retrieving changes between commits.

## Public API

- `GitManager` (exposure)
- `GitDiff` (exposure)

## Dependencies

- `git` (external)
- `pathlib` (external)
- `typing` (external)
- `dataclasses` (external)
- `logging` (external)

## Elements

### Class

#### `GitDiff`

**Scope:** global

**Purpose:** Represents changes between commits in a Git repository.

**Documentation:**

GitDiff is a data class that stores lists of added, modified, and deleted files, as well as the raw diff string for Git commit comparisons.

#### `GitManager`

**Scope:** global

**Purpose:** Manages Git repository operations such as initialization, cloning, and fetching commit differences.

**Documentation:**

GitManager provides methods to initialize a repository, clone it, get the current commit hash, retrieve changes since a given commit, and fetch file contents at specific commits.

### Method

#### `__init__`

**Scope:** GitManager

**Purpose:** Initializes a GitManager instance with an optional repository path.

**Documentation:**

Sets up the GitManager with a specified or current directory as the repository path and initializes logging.

#### `clone`

**Scope:** GitManager

**Purpose:** Clones a remote Git repository to a specified path.

**Documentation:**

Clones the repository from a given URL to the target path. Logs errors if the operation fails.

#### `get_changes_since_commit`

**Scope:** GitManager

**Purpose:** Retrieves changes between the current HEAD and a specified commit.

**Documentation:**

Compares the current HEAD with a given commit hash, returning lists of added, modified, and deleted files along with the raw diff.

#### `get_current_commit`

**Scope:** GitManager

**Purpose:** Fetches the hash of the current commit in the repository.

**Documentation:**

Returns the hexadecimal hash of the current commit from the HEAD of the repository.

#### `get_file_content`

**Scope:** GitManager

**Purpose:** Retrieves the contents of a file at a specific commit.

**Documentation:**

Returns the content of a specified file either at the current HEAD or a specific commit. Logs errors if the file cannot be read.

#### `initialize`

**Scope:** GitManager

**Purpose:** Establishes a connection to a Git repository.

**Documentation:**

Attempts to open a Git repository at the given path. Logs an error if the repository is invalid.


[Back to Index](../README.md)