import typer

model_app = typer.Typer(help="Manage models")


@model_app.command("pull")
def pull(name: str):
    """
    Download a model
    """
    typer.echo(f"Downloading model '{name}'...")


@model_app.command("list")
def list_models():
    """
    List all models
    """
    typer.echo("Listing all models...")


@model_app.command("info")
def info(name: str):
    """
    Show model info
    """
    typer.echo(f"Showing info for model '{name}'")


@model_app.command("remove")
def remove(name: str, force: bool = False):
    """
    Delete a model
    """
    if force:
        typer.echo(f"Force deleting model '{name}'")
    else:
        confirm = typer.confirm(f"Delete model '{name}'?")
        if confirm:
            typer.echo(f"Deleted '{name}'")
        else:
            typer.echo("Cancelled")


@model_app.command("copy")
def copy(src: str, dest: str):
    """
    Copy model
    """
    typer.echo(f"Copying model from '{src}' to '{dest}'")