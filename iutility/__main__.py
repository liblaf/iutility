import logging

import click
from ishutils import config
from ishutils.log import install as log_install

from . import __version__
from .clean import cmd as cmd_clean
from .git import cmd as cmd_git
from .key import cmd as cmd_key
from .update import cmd as cmd_update


@click.group(name="iutility", context_settings={"show_default": True})
@click.version_option(version=__version__)
@click.option(
    "--log-level",
    type=click.Choice(
        choices=["OFF", "CRITICAL", "ERROR", "WARN", "INFO", "DEBUG", "NOTSET"],
        case_sensitive=False,
    ),
    default="INFO",
)
@click.option("-y", "--yes", is_flag=True)
def main(log_level: str, yes: bool) -> None:
    log_level = log_level.upper()
    if log_level == "OFF":
        log_install(level=77)
    else:
        log_install(level=logging.getLevelName(level=log_level))
    config.confirm = not yes


main.add_command(cmd=cmd_clean)
main.add_command(cmd=cmd_git)
main.add_command(cmd=cmd_key)
main.add_command(cmd=cmd_update)


if __name__ == "__main__":
    main(prog_name="iutility")
