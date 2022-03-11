{{cookiecutter.project_slug}}
=========

[![image](https://img.shields.io/pypi/v/{{cookiecutter.project_slug}}.svg)](https://pypi.python.org/pypi/{{cookiecutter.project_slug}})

[![image]({{cookiecutter.repository_url}}/workflows/pytest/badge.svg)]({{cookiecutter.repository_url}}/actions)

[![Documentation Status](https://readthedocs.org/projects/{{cookiecutter.project_slug}}/badge/?version=latest)](https://{{cookiecutter.project_slug}}.readthedocs.io/en/latest/?badge=latest)


{{cookiecutter.short_description}}

-   Free software: BSD license
-   Documentation: <https://{{cookiecutter.project_slug}}.readthedocs.io>.
-   [![Live examples](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/WWU-AMM/{{cookiecutter.project_slug}}/HEAD?filepath=docs%2Fexamples%2F)


Features
--------

-   TODO

After generating your project
-----------------------------

- Setup github secrets for pypi [github project settings]({{cookiecutter.repository_url}}/settings/secrets/actions/new):
   - `PYPI_TOKEN` for "real" deploys on git tags
   - `TEST_PYPI_TOKEN` for deploys to test.pypi.org
- enable project on [readthedocs.org](https://readthedocs.org/dashboard/import/?)
- setup branch protection+automerge in [github project settings]({{cookiecutter.repository_url}}/settings/branches)
- Fix `Live examples` link above


Credits
-------

This package was created with
[Cookiecutter](https://github.com/audreyr/cookiecutter) and the
[WWU-AMM/python_cookiecutter](https://github.com/WWU-AMM/python_cookiecutter)
project template.
