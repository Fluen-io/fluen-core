# {{ project.name|default('Project') }} Documentation

## Project Overview

- **Primary Language:** {{ project.primary_language|default('Not specified') }}
- **Frameworks:** {{ project.frameworks|default([])|join(', ')|default('None specified') }}
- **Last Updated:** {{ generation_time|default('Not specified') }}
- **Git Commit:** {{ git_commit[:8]|default('Unknown') }}

## Project Structure

{% if files_by_type.items()|length > 0 %}
{% for type, files in files_by_type.items()|sort %}
### {{ type }} Files

{% for file in files|sort %}
- [{{ file }}](reference/{{ file|replace('/', '_') }}.md)
{% endfor %}

{% endfor %}
{% else %}
No source files found.
{% endif %}

## Dependencies

{% if dependencies.items()|length > 0 %}
| Name | Type | Version | Used By |
|------|------|---------|---------|
{% for name, dep in dependencies.items()|sort %}
| {{ name }} | {{ dep.type|default('Unknown') }} | {{ dep.version|default('N/A') }} | {% if dep.used_by %}{% for file in dep.used_by|sort %}[{{ file }}](reference/{{ file|replace('/', '_') }}.md){% if not loop.last %}, {% endif %}{% endfor %}{% else %}N/A{% endif %} |
{% endfor %}
{% else %}
No dependencies found.
{% endif %}

## Navigation

- [Summary](SUMMARY.md)
- [Reference Documentation](reference/)