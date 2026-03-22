import typer
from model import model_app
from config import config_app
from utils import utils_app

app = typer.Typer(help="Vectra CLI - AI Model Management Tool")

# Register subcommands
app.add_typer(model_app, name="model")
app.add_typer(config_app, name="config")
app.add_typer(utils_app)

# Core commands
@app.command()
def run(model: str, prompt: str = None):
    """
    Run a model with optional prompt
    """
    if prompt:
        typer.echo(f"Running model '{model}' with prompt: {prompt}")
    else:
        typer.echo(f"Opening interactive mode for model '{model}'...")


@app.command()
def chat(model: str):
    """
    Start chat session
    """
    typer.echo(f"Starting chat with model '{model}' (Ctrl+D to exit)")


@app.command()
def serve(port: int = 11434):
    """
    Start server
    """
    typer.echo(f"Starting server on port {port}...")


@app.command()
def ps():
    """
    Show running models
    """
    typer.echo("Showing running models...")


@app.command()
def stop(model: str = None):
    """
    Stop model or server
    """
    if model:
        typer.echo(f"Stopping model '{model}'...")
    else:
        typer.echo("Stopping server...")


if __name__ == "__main__":
    app()