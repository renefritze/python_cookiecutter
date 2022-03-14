```{highlight} shell

```

# Installation

## Stable release

To install {{cookiecutter.project_slug}}, run this command in your terminal:

```{code-block} console

$ pip install {{cookiecutter.project_slug}}

```

This is the preferred method to install {{cookiecutter.project_slug}}, as it will always install the most recent stable release.

If you don't have [pip][pip] installed, this [Python installation guide][python installation guide] can guide
you through the process.

[pip]: https://pip.pypa.io

[python installation guide]: http://docs.python-guide.org/en/latest/starting/installation/

## From sources

The sources for {{cookiecutter.project_slug}} can be downloaded from the [Github repo][github repo].

You can either clone the public repository:

```{code-block} console

$ git clone {{cookiecutter.repository_url}}.git

```

Or download the [tarball][tarball]:

```{code-block} console

$ curl -OJL {{cookiecutter.repository_url}}/tarball/main

```

Once you have a copy of the source, you can install it with:

```{code-block} console

$ pip install .

```

[github repo]: {{cookiecutter.repository_url}}

[tarball]: {{cookiecutter.repository_url}}/tarball/main
