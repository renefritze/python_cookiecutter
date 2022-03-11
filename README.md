# Using this cookiecutter

There are two prerequisites:
 1. Git needs to be available on your system
 2. You need to have cookiecutter installed. General instructions are 
 [here](https://cookiecutter.readthedocs.io/en/latest/installation.html), 
 but `pip install cookiecutter` should be enough in most cases.

Then do this in a terminal:

```
cd /where/you/store/your/projects
cookiecutter https://github.com/WWU-AMM/python_cookiecutter
```

Answer the prompts and cookiecutter generates a new directory
with the given name.

# Features

- CI setup with github actions
  - linting
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
- cli package with typer
- dependency via `dependencies.py`
- pre-commit config (tries install+run automatically)