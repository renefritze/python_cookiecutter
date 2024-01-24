# Using this cookiecutter

There are two prerequisites:
1. Git needs to be available on your system
2. You need to have cookiecutter installed. General instructions are
[here](https://cookiecutter.readthedocs.io/en/latest/installation.html),
but `pip install cookiecutter` should be enough in most cases.

Then do this in a terminal:

```
cd /where/you/store/your/projects
cookiecutter https://github.com/arup-group/ana-python-cookiecutter
```

Answer the prompts and cookiecutter generates a new directory
with the given name.

# Features

- hatch buildsystem via pyproject.toml
- CI setup with github actions
    - linting with Ruff
    - deployment to pypi on git tags
    - test deployment to test.pypi on each push
    - coverage upload to codecov.io
    - dependabot for action updates
    - auto black
- documentation with sphinx
    - markdown as default
    - uses autoapi to generate docs for all (sub) modules
    - need to enable the project on readthedocs.io
- package version determined from git tags like "v0.0.1"
- tests with pytest
- cli scripts with typer
- pre-commit config (tries install+run automatically)
    - ruff
    - yamlfmt
    - ...

# Post-Generation

Let's say you used 'ScoobySnacks` as the project name. Then you need to do the following:

1. `cd ScoobySnacks`
2. `gh repo create ScoobySnacks` Select from local repo, same name and then push
3. In the repo settings:
    - add OasysAutomation as a collaborator with automationWrite role
    - add teams with write access
    - configure branch protection at least for main
3. Have a github admin:
    - enable `OASYS_REPO_SCOPE_PAT` for ScoobySnacks both as action and dependabot secret
    - install the codecov app for ScoobySnacks
4. log in to codecov.io, go to ScoobySnacks and copy the token to a new action + dependabot secret\
in the repo settings
