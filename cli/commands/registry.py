import typer
from rich.table import Table
from rich.console import Console
from vectra.core.model_manager import registry

app = typer.Typer(help="Manage the model registry.")
console = Console()


@app.command("list")
def list_models():
    """List all models in the registry."""
    models = registry.list()
    if not models:
        console.print("[yellow]Registry is empty.[/yellow]")
        return

    table = Table(title="Model Registry")
    table.add_column("Name", style="cyan", no_wrap=True)
    table.add_column("URL", style="dim")

    for name, url in models.items():
        table.add_row(name, url)

    console.print(table)


@app.command("add")
def add_model(name: str, url: str):
    """Add a model to the registry."""
    registry.add(name, url)
    console.print(f"[green]Added[/green] '{name}' → {url}")


@app.command("remove")
def remove_model(name: str):
    """Remove a model from the registry."""
    try:
        registry.remove(name)
        console.print(f"[red]Removed[/red] '{name}' from registry.")
    except KeyError as e:
        console.print(f"[bold red]Error:[/bold red] {e}")
        raise typer.Exit(1)

