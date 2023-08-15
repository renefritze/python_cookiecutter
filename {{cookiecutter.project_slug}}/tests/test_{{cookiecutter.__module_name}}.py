"""Tests for `{{cookiecutter.project_slug}}` package."""
from click.testing import CliRunner


def test_version():
    import {{cookiecutter.__module_name}}
    assert {{cookiecutter.__module_name}}.__version__


def test_import():
    import {{cookiecutter.__module_name}}


def test_command_line_interface():
    """Test the CLI."""
    from {{cookiecutter.__module_name}} import cli
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert '{{cookiecutter.__module_name}}.cli.main' in result.output
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert '--help  Show this message and exit.' in help_result.output
