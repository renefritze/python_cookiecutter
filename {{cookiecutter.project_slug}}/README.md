{{cookiecutter.project_slug}}
=========
[![image]({{cookiecutter.repository_url}}/workflows/pytest/badge.svg)]({{cookiecutter.repository_url}}/actions)

{{cookiecutter.short_description}}

Installation and Development
-------------------------
This project uses [uv](https://github.com/astral-sh/uv) for fast, reliable Python package management. To get started:

1. Install uv: 

2. Install the package with development dependencies:
```bash
uv sync
```

3. Run tests:
```bash
uv run pytest
```

4. Run linting:
```bash
uv run ruff check .
```

Features
--------
-   TODO

After generating your project
-----------------------------
- setup branch protection+automerge in [github project settings]({{cookiecutter.repository_url}}/settings/branches)
- request install for the codecov.io app in [github project settings]({{cookiecutter.repository_url}}/settings/installations)
- configure codecov.io in [codecov.io settings](https://codecov.io/gh/arup-group/cookiecutter.project_slug}}/settings)
- add the `CODECOV_TOKEN` secret in [github project settings]({{cookiecutter.repository_url}}/settings/secrets/actions)

Credits
-------
This package was created with
[Cookiecutter](https://github.com/audreyr/cookiecutter) and the
[renefritze/python_cookiecutter](https://github.com/renefritze/python_cookiecutter)
project template.
