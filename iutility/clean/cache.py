from pathlib import Path

import click
from ishutils import remove


@click.command(name="cache")
def cmd() -> None:
    remove(path=Path.home() / ".cache")
