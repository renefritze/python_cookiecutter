"""Top-level package for {{cookiecutter.project_slug}}."""

__author__ = """ {{cookiecutter.author}}"""
__email__ = " {{cookiecutter.email}}"

try:
    from . import _version
    __version__ = _version.__version__
except ImportError as e:
    print(f"version file could not be imported: {e}") #  noqa: T201
    __version__ = "unknown"
