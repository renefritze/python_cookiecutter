"""Top-level package for {{cookiecutter.project_slug}}."""

__author__ = """ {{cookiecutter.author}}"""
__email__ = " {{cookiecutter.email}}"

from ._version import get_versions

__version__ = get_versions()["version"]
del get_versions
