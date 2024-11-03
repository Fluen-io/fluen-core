# Summary

- [{{ project.name|default('Project') }} Documentation](README.md)

## Project Structure

{% if groups.items()|length > 0 %}
{% for language, files in groups.items()|sort %}
### {{ language }} Files

{% for file in files|sort %}
- [{{ file }}](reference/{{ file|replace('/', '_') }}.md)
{% endfor %}

{% endfor %}
{% else %}
No source files found.
{% endif %}

## Quick Links

- [Project Overview](README.md#project-overview)
{% if project.frameworks|default([])|length > 0 %}
- [Frameworks Used](README.md#frameworks)
{% endif %}

## Reference Documentation

{% if files.items()|length > 0 %}
{% for file_path, file_manifest in files.items()|sort %}
### [{{ file_path }}](reference/{{ file_path|replace('/', '_') }}.md)

{% if file_manifest.purpose %}
{{ file_manifest.purpose|truncate(100) }}
{% endif %}

{% if file_manifest.exposures|default([])|length > 0 %}
**Public API:**
{% for exposure in file_manifest.exposures|sort(attribute="name") %}
- `{{ exposure.name }}` ({{ exposure.type }})
{% endfor %}
{% endif %}

{% endfor %}
{% else %}
No documentation available.
{% endif %}

---
Generated on {{ generation_time|default('Unknown date') }}  
Git commit: {{ git_commit[:8]|default('Unknown') }}