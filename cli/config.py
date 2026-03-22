import typer

config_app = typer.Typer(help="Manage config")


@config_app.command("set")
def set_config(key: str, value: str):
    """
    Set config value
    """
    typer.echo(f"Setting {key} = {value}")


@config_app.command("show")
def show():
    """
    Show config
    """
    typer.echo("Showing all config values...")


@config_app.command("reset")
def reset(key: str = None):
    """
    Reset config
    """
    if key:
        typer.echo(f"Resetting {key}")
    else:
        typer.echo("Resetting all config")