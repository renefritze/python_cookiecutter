#!/usr/bin/env python

"""Tests for `{{cookiecutter.project_slug}}` package."""
import pickle
import numpy as np
from functools import partial
from tempfile import TemporaryFile

from click.testing import CliRunner

from {{cookiecutter.project_slug}} import cli



def test_version():
    assert {{cookiecutter.project_slug}}.__version__


def test_import(timings_object):
    from {{cookiecutter.project_slug}} import *

def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert '{{cookiecutter.project_slug}}.cli.main' in result.output
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert '--help  Show this message and exit.' in help_result.output
