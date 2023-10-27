import logging

import click
import logzero

from varfish_cli import _version


@click.group()
@click.version_option(_version.__version__)
@click.option("--verbose/--no-verbose", default=False, help="Enable/disable logging verbosity.")
@click.pass_context
def cli_main(ctx: click.Context, verbose: bool):
    """Main entry point for CLI via click."""
    ctx.ensure_object(dict)
    ctx.obj["verbose"] = verbose
    if verbose:
        logzero.loglevel(logging.DEBUG)
    else:
        logzero.loglevel(logging.INFO)


if __name__ == "__main__":
    cli_main()
