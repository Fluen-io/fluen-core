# src/fluen/models/scan.py

**Language:** Python  
**Last Modified:** 2024-11-13T17:53:21.469450

## Purpose

The code provides functionality for parsing, validating, and handling selectors for a scanning operation with options for selective scanning and forced execution.

## Public API

- `ScanSelector` (exposure)
- `ScanOptions` (exposure)
- `ScanSelector.is_path_selector` (exposure)
- `ScanSelector.is_element_selector` (exposure)
- `ScanOptions.is_selective_scan` (exposure)

## Dependencies

- `pathlib` (external)
- `typing` (external)

## Elements

### Class

#### `ScanOptions`

**Scope:** public

**Purpose:** Container for scan options, including selector and force flag.

**Documentation:**

This class wraps scan options and provides a mechanism to manage an optional selector and a force flag for scan operations.

#### `ScanSelector`

**Scope:** public

**Purpose:** Handles parsing and validation of scan selectors.

**Documentation:**

This class parses a selector string into type and value, validates it, and provides properties to query the selector type.

### Method

#### `ScanOptions.__init__`

**Scope:** public

**Purpose:** Initializes a ScanOptions instance with optional selector and force flag.

**Documentation:**

Constructor that initializes the selector object if provided and sets the force flag.

#### `ScanSelector.__init__`

**Scope:** public

**Purpose:** Initializes a ScanSelector instance with parsing.

**Documentation:**

Constructor that takes a raw selector string, initializes attributes, and triggers parsing and validation.

#### `ScanSelector._parse_selector`

**Scope:** private

**Purpose:** Parses the selector string into type and value components.

**Documentation:**

Internal method that splits the selector string by &#39;:&#39; and assigns the type and value. Raises ValueError on invalid format.

#### `ScanSelector._validate`

**Scope:** private

**Purpose:** Validates the parsed selector type.

**Documentation:**

Checks if the selector type is within the set of valid types (e.g., &#39;path&#39;, &#39;element&#39;). Returns True if valid, otherwise False.

### Property

#### `ScanOptions.is_selective_scan`

**Scope:** public

**Purpose:** Determines if the scan is selective based on selector presence.

**Documentation:**

Property that returns True if a selector is present, indicating a selective scan.

#### `ScanSelector.is_element_selector`

**Scope:** public

**Purpose:** Checks if the selector is of type &#39;element&#39;.

**Documentation:**

Property that returns True if the selector type is &#39;element&#39;.

#### `ScanSelector.is_path_selector`

**Scope:** public

**Purpose:** Checks if the selector is of type &#39;path&#39;.

**Documentation:**

Property that returns True if the selector type is &#39;path&#39;.


[Back to Index](../README.md)