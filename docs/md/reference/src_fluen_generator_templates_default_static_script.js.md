# src/fluen/generator/templates/default/static/script.js

**Language:** JavaScript  
**Last Modified:** 2024-11-13T17:50:33.634786

## Purpose

The code provides functionality for searching documentation and visualizing data through a lineage graph on a web page.

## Public API

- `DocumentationSearch` (exposure)
- `LineageGraph` (exposure)

## Dependencies

- `d3` (external)

## Elements

### Class

#### `DocumentationSearch`

**Scope:** global

**Purpose:** Handles the documentation search functionality, including loading the search index, managing user input, and displaying search results.

**Documentation:**

The class initializes search input elements, sets up keyboard shortcuts, and handles search index loading and user interactions for search functionality.

#### `LineageGraph`

**Scope:** global

**Purpose:** Renders a lineage graph to visualize relationships between data nodes.

**Documentation:**

The class uses D3.js to render an interactive graph in a specified container, handling node and link interactions through event listeners.

### Method

#### `_escapeHtml`

**Scope:** DocumentationSearch

**Purpose:** Escapes HTML characters for safe insertion into the result display.

**Documentation:**

Converts a string to a safe HTML format to prevent potential HTML injection vulnerabilities.

#### `_getManifestPath`

**Scope:** DocumentationSearch

**Purpose:** Determines the path to the documentation manifest file.

**Documentation:**

Checks the current page path to correctly set the relative path to the manifest, depending on the context (reference page or index).

#### `buildSearchIndex`

**Scope:** DocumentationSearch

**Purpose:** Builds the search index from the loaded manifest.

**Documentation:**

Processes the manifest data to create an index that facilitates quick searching by path and elements.

#### `clearResults`

**Scope:** DocumentationSearch

**Purpose:** Clears the current search results.

**Documentation:**

Empties the search results container and updates the UI state to reflect that no results are active.

#### `displayResults`

**Scope:** DocumentationSearch

**Purpose:** Displays the search results in the UI.

**Documentation:**

Generates and injects HTML to present the search results and sets event handlers for result item clicks.

#### `dragended`

**Scope:** LineageGraph

**Purpose:** Ends the dragging interaction on a graph node.

**Documentation:**

Releases the node to its final position, removing fixed coordinates and resetting the simulation state.

#### `dragged`

**Scope:** LineageGraph

**Purpose:** Updates node position during dragging interaction.

**Documentation:**

Updates the position of a node as it is dragged across the graph. Adjusts fixed positions dynamically.

#### `dragstarted`

**Scope:** LineageGraph

**Purpose:** Starts the dragging interaction on a graph node.

**Documentation:**

Fixes position properties and restarts the simulation to allow a node to be freely moved using the mouse.

#### `getNodeColor`

**Scope:** LineageGraph

**Purpose:** Determines the color for graph nodes based on their type.

**Documentation:**

Returns a specific color code according to the type attribute of a node to visually differentiate node types.

#### `handleNodeHover`

**Scope:** LineageGraph

**Purpose:** Handles hover interaction on a graph node.

**Documentation:**

Enlarges the node size on hover to emphasize focus, creating a visual effect to enhance UX.

#### `handleNodeHoverEnd`

**Scope:** LineageGraph

**Purpose:** Handles the end of a hover interaction on a graph node.

**Documentation:**

Reduces the node size when hover ends, reverting it back to its original size.

#### `handleResultClick`

**Scope:** DocumentationSearch

**Purpose:** Handles clicks on search result items.

**Documentation:**

Navigates to the appropriate page or element in the documentation when a user clicks a search result.

#### `handleSearch`

**Scope:** DocumentationSearch

**Purpose:** Processes the search input and displays results.

**Documentation:**

Reads the search query and displays filtered search results based on the query entered by the user.

#### `initializeGraph`

**Scope:** LineageGraph

**Purpose:** Sets up the graph using D3 to create nodes and links.

**Documentation:**

Initializes an SVG graph area and sets up D3 force and drag simulations along with link and node definitions. Handles interactions like hover and drag.

#### `initializeSearch`

**Scope:** DocumentationSearch

**Purpose:** Initializes the search index by loading a manifest file dynamically.

**Documentation:**

Asynchronously loads a manifest file and builds a search index from it. Sets up event listeners for search input interactions.

#### `performSearch`

**Scope:** DocumentationSearch

**Purpose:** Executes the search operation on the index.

**Documentation:**

Matches the query against paths, purposes, and elements in the search index to find relevant results, limiting to 10.

#### `setupEventListeners`

**Scope:** DocumentationSearch

**Purpose:** Sets up event listeners for search input focus and document click events.

**Documentation:**

Handles input events to trigger search operations and manages document clicks to hide search results when clicking outside the search area.

#### `setupKeyboardShortcuts`

**Scope:** DocumentationSearch

**Purpose:** Manages keyboard shortcuts for search operations.

**Documentation:**

Listens for &#39;/&#39; to focus the search input and &#39;Escape&#39; to clear search results and blur input.


[Back to Index](../README.md)