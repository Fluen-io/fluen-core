# {{ file.path }}

**Language:** {{ file.language }}  
**Last Modified:** {{ file.last_modified }}

## Purpose

{{ file.purpose }}

{% if file.exposures|default([])|length > 0 %}
## Public API

{% for exposure in file.exposures %}
- `{{ exposure.name }}` ({{ exposure.type }})
{% endfor %}
{% endif %}

{% if file.dependencies|default([])|length > 0 %}
## Dependencies

{% for dep in file.dependencies %}
- `{{ dep.name }}` ({{ dep.type }}{% if dep.version %}, version: {{ dep.version }}{% endif %})
{% endfor %}
{% endif %}

## Elements

{% if elements_by_type.items()|length > 0 %}
{% for type, elements in elements_by_type.items()|sort %}
### {{ type|format_type }}

{% for element in elements|sort(attribute="name") %}
#### `{{ element.name }}`

{% if element.scope %}
**Scope:** {{ element.scope }}
{% endif %}

**Purpose:** {{ element.purpose|default('No purpose specified') }}

**Documentation:**

{{ element.documentation|default('No documentation available') }}

{% endfor %}
{% endfor %}
{% else %}
No documented elements found.
{% endif %}

[Back to Index](../README.md)