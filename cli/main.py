import typer
from vectra.cli.commands import pull, run, registry

app = typer.Typer()

app.add_typer(run.app, name="run")
app.add_typer(pull.app, name="pull")
app.add_typer(registry.app, name="registry")

if __name__ == "__main__":
    app()