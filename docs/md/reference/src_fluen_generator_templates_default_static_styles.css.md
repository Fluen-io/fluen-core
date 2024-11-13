# src/fluen/generator/templates/default/static/styles.css

**Language:** Unknown  
**Last Modified:** 2024-11-13T17:58:42.874315

## Purpose

This CSS stylesheet is designed to provide a consistent and responsive layout for a web application, including a sidebar navigation, main content area, and various interactive UI features.

## Public API

- `:root` (exposure)
- `*` (exposure)
- `body` (exposure)
- `.sidebar` (exposure)
- `.sidebar-header` (exposure)
- `.sidebar-header h1` (exposure)
- `.sidebar-header h1 a` (exposure)
- `.sidebar-content` (exposure)
- `.main-content` (exposure)
- `.main-header` (exposure)
- `.content` (exposure)
- `.search-container` (exposure)
- `.search-input` (exposure)
- `.search-results` (exposure)
- `.search-active .search-results` (exposure)
- `.search-result-item` (exposure)
- `.lineage-graph` (exposure)
- `.element` (exposure)
- `.element-header` (exposure)
- `.element-header code` (exposure)
- `.type-badge` (exposure)
- `.scope-badge` (exposure)
- `@media (max-width: 768px)` (exposure)


## Elements

### Class

#### `.content`

**Scope:** component

**Purpose:** Styles the inner content area.

**Documentation:**

Applies top margin and padding to shift below the fixed header.

#### `.element`

**Scope:** component

**Purpose:** Styles generic UI elements.

**Documentation:**

Sets appearance, borders, spacing, and hover effects for reusable elements.

#### `.element-header`

**Scope:** component

**Purpose:** Styles headers within elements.

**Documentation:**

Aligns header content and sets spacing.

#### `.lineage-graph`

**Scope:** component

**Purpose:** Styles a lineage graph element.

**Documentation:**

Configures layout, borders, and dimensions for a graphical element, presumably a graph or chart.

#### `.main-content`

**Scope:** component

**Purpose:** Styles the main content area.

**Documentation:**

Adjusts the layout to account for the fixed sidebar width.

#### `.main-header`

**Scope:** component

**Purpose:** Styles the fixed-position main header.

**Documentation:**

Configures positioning, background, border, alignment, and z-index of the main header.

#### `.scope-badge`

**Scope:** component

**Purpose:** Styles a scope badge element.

**Documentation:**

Applies appearance settings to scope badges, distinct from type badges.

#### `.search-container`

**Scope:** component

**Purpose:** Defines the layout for a search container.

**Documentation:**

Positions a search input with relative positioning to accommodate absolute-positioned results.

#### `.search-input`

**Scope:** component

**Purpose:** Styles the search input field.

**Documentation:**

Configures padding, border, font size, and transition effects for focus states.

#### `.search-result-item`

**Scope:** component

**Purpose:** Styles individual search results.

**Documentation:**

Sets padding, border, and hover background effects for items in search results.

#### `.search-results`

**Scope:** component

**Purpose:** Styles the dropdown search results.

**Documentation:**

Configures dropdown styling, including positioning, borders, shadow, and display properties.

#### `.sidebar`

**Scope:** component

**Purpose:** Styles a fixed-position sidebar.

**Documentation:**

Configures position, dimensions, background, and layout for a sidebar element.

#### `.sidebar-content`

**Scope:** component

**Purpose:** Styles the sidebar&#39;s scrollable content area.

**Documentation:**

Sets the sidebar&#39;s main content area with padding and scroll overflow.

#### `.sidebar-header`

**Scope:** component

**Purpose:** Styles the header section within the sidebar.

**Documentation:**

Adds padding and a bottom border to distinguish the header section in the sidebar.

#### `.type-badge`

**Scope:** component

**Purpose:** Styles a type badge element.

**Documentation:**

Configures the appearance of type badges with color and size properties.

### Class Selector

#### `.search-active .search-results`

**Scope:** component

**Purpose:** Toggles display of search results when active.

**Documentation:**

Changes the display property to block when the parent has the search-active class.

### Element

#### `body`

**Scope:** global

**Purpose:** Sets base styles for the body element.

**Documentation:**

Configures default font, color, alignment, and background for the document body.

### Element Selector

#### `.element-header code`

**Scope:** component

**Purpose:** Styles code elements within headers.

**Documentation:**

Sets font size and color for inline code in element headers.

#### `.sidebar-header h1`

**Scope:** component

**Purpose:** Styles h1 elements within the sidebar header.

**Documentation:**

Configures font size and bottom margin for h1 elements, typically used for sidebar titles.

#### `.sidebar-header h1 a`

**Scope:** component

**Purpose:** Styles links within the sidebar header h1.

**Documentation:**

Ensures links within the sidebar header h1 have the primary color and no text decoration.

### Media Query

#### `@media (max-width: 768px)`

**Scope:** responsive

**Purpose:** Applies styles for devices with width up to 768px.

**Documentation:**

Adjusts sidebar and main content to be responsive on smaller screens.

### Universal Selector

#### `*`

**Scope:** global

**Purpose:** Applies a reset style to all elements.

**Documentation:**

This selector removes default margin, padding, and changes box-sizing to border-box for all elements, ensuring a consistent starting point for styling.

### Variable

#### `:root`

**Scope:** global

**Purpose:** Defines CSS variables for colors, dimensions, and reusable values.

**Documentation:**

CSS variables (custom properties) are defined for use throughout the stylesheet, providing a centralized way to manage theme and layout values.


[Back to Index](../README.md)