# {{ project.name }} Documentation

## Project Overview

- **Primary Language:** {{ project.primary_language }}
- **Frameworks:** {{ project.frameworks|join(', ') }}
- **Last Updated:** {{ generation_time }}
- **Git Commit:** {{ git_commit[:8] }}

## Project Structure

{% for type, files in files_by_type.items() %}
### {{ type }} Files

{% for file in files %}
- [{{ file }}](reference/{{ file|replace('/', '_') }}.md)
{% endfor %}

{% endfor %}

## Dependencies

| Name | Type | Version | Used By |
|------|------|---------|---------|
{% for name, dep in dependencies.items() %}
| {{ name }} | {{ dep.type }} | {{ dep.version or 'N/A' }} | {% for file in dep.used_by %}[{{ file }}](reference/{{ file|replace('/', '_') }}.md){% if not loop.last %}, {% endif %}{% endfor %} |
{% endfor %}

## Navigation

- [Summary](SUMMARY.md)
- [Reference Documentation](reference/)