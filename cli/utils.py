import typer

utils_app = typer.Typer(help="Utility commands")


@utils_app.command()
def version():
    typer.echo("Vectra version 0.1.0")


@utils_app.command()
def doctor():
    typer.echo("Running system checks...")


@utils_app.command()
def logs(tail: bool = False, level: str = "info"):
    typer.echo(f"Showing logs | tail={tail} | level={level}")