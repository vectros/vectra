import typer
from vectra.core.model_manager import download_model

app = typer.Typer()

@app.command()
def model(name: str):
    path = download_model(name)
    print(f"Downloaded to {path}")