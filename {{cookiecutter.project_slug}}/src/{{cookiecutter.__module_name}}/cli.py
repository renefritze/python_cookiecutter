"""Console script for {{cookiecutter.project_slug}}."""
import sys
import click


@click.command()
def main(args=None):
    """Console script for {{cookiecutter.project_slug}}."""
    click.echo(
        "Replace this message by putting your code into "
        "{{cookiecutter.__module_name}}.cli.main"
    )
    click.echo("See click documentation at https://click.palletsprojects.com/")
    print(f"Gotta use the args: {args}") # noqa: T201
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
