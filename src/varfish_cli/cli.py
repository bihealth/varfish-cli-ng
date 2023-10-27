import logging
import os
import pathlib
import tomllib
import uuid

import click
import logzero
from pydantic import BaseModel, Field, SecretStr

from varfish_cli import _version


class VarfishGlobalConfig(BaseModel):
    """Entry of ``global`` section in varfish config TOML."""
    varfish_server_url: str | None = None
    varfish_api_token: str | None = None


class VarfishConfig(BaseModel):
    """Configuration as read from varfish config TOML."""
    global_: VarfishGlobalConfig | None = Field(None, alias='global')


class SharedConfig(BaseModel):
    """Shared configuration for all commands."""

    verbose: bool
    api_entrypoint: str
    api_token: SecretStr


@click.group()
@click.version_option(_version.__version__)
@click.option("--verbose/--no-verbose", default=False, help="Enable/disable logging verbosity.")
@click.option(
    "--api-entrypoint",
    type=str,
    help=(
        "Entrypoint for API, can also be set by env VARFISH_API_ENTRYPOINT or read from conf "
        "global/varfish_server_url"
    ),
    default=lambda: os.environ.get("VARFISH_API_ENTRYPOINT", None),
)
@click.option(
    "--api-token",
    type=str,
    help=(
        "Entrypoint for API, can also be set by env VARFISH_API_TOKEN or read from conf "
        "global/varfish_api_token"
    ),
    default=lambda: os.environ.get("VARFISH_API_TOKEN", None),
)
@click.pass_context
def cli_main(ctx: click.Context, verbose: bool, api_entrypoint: str | None, api_token: str | None):
    """Main entry point for CLI via click."""
    varfishrc_path = pathlib.Path.home() / ".varfishrc.toml"
    if varfishrc_path.exists():
        with varfishrc_path.open("rb") as inputf:
            obj = tomllib.load(inputf)
            config = VarfishConfig(**obj)
    else:
        config = VarfishConfig()

    ctx.ensure_object(dict)
    ctx.obj["verbose"] = verbose
    ctx.obj["api_entrypoint"] = api_entrypoint
    if not api_entrypoint and config.global_ and config.global_.varfish_server_url:
        ctx.obj["api_entrypoint"] = config.global_.varfish_server_url
    ctx.obj["api_token"] = api_token
    if not api_token and config.global_ and config.global_.varfish_api_token:
        ctx.obj["api_token"] = config.global_.varfish_api_token
    if verbose:
        logzero.loglevel(logging.DEBUG)
    else:
        logzero.loglevel(logging.INFO)


@cli_main.group("case_imports")
def cli_cases_import():
    """Command group for cases to import."""


@cli_cases_import.command("list")
@click.argument(
    "project_uuid",
    type=str,
)
@click.pass_context
def cli_cases_import_list(ctx: click.Context, project_uuid: str | None = None):
    """Command group for listing case import jobs."""
    config = SharedConfig(**ctx.obj)
    try:
        proj_uuid = uuid.UUID(project_uuid)
    except ValueError:
        raise click.BadParameter("project_uuid must be a UUID")
    print(config, proj_uuid)


if __name__ == "__main__":
    cli_main()
