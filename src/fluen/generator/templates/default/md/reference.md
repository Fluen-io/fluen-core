# {{ file.path }}

**Language:** {{ file.language }}  
**Last Modified:** {{ file.last_modified }}

## Purpose

{{ file.purpose }}

{% if file.exposures %}
## Public API

{% for exposure in file.exposures %}
- `{{ exposure.name }}` ({{ exposure.type }})
{% endfor %}
{% endif %}

{% if file.dependencies %}
## Dependencies

{% for dep in file.dependencies %}
- `{{ dep.name }}` ({{ dep.type }}{% if dep.version %}, version: {{ dep.version }}{% endif %})
{% endfor %}
{% endif %}

## Elements

{% for type, elements in elements_by_type.items() %}
### {{ type|format_type }}

{% for element in elements %}
#### `{{ element.name }}`

{% if element.scope %}
**Scope:** {{ element.scope }}
{% endif %}

**Purpose:** {{ element.purpose }}

**Documentation:**

{{ element.documentation }}

{% endfor %}
{% endfor %}

[Back to Index](../README.md)