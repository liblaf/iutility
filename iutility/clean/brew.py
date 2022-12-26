import click

from ..utils import execute


@click.command(name="brew")
def cmd() -> None:
    execute("brew", "autoremove")
    execute("brew", "cleanup")
