{{cookiecutter.project_slug}}
=========


[![image]({{cookiecutter.repository_url}}/workflows/pytest/badge.svg)]({{cookiecutter.repository_url}}/actions)


{{cookiecutter.short_description}}


Features
--------

-   TODO

After generating your project
-----------------------------

- Setup github secrets for pypi [github project settings]({{cookiecutter.repository_url}}/settings/secrets/actions/new):
   - `PYPI_TOKEN` for "real" deploys on git tags
   - `TEST_PYPI_TOKEN` for deploys to test.pypi.org
- setup branch protection+automerge in [github project settings]({{cookiecutter.repository_url}}/settings/branches)
-


Credits
-------

This package was created with
[Cookiecutter](https://github.com/audreyr/cookiecutter) and the
[renefritze/python_cookiecutter](https://github.com/renefritze/python_cookiecutter)
project template.
