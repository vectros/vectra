import typer
from vectra.core.runner import LlamaRunner
from vectra.core.model_manager import get_model_path

app = typer.Typer()

@app.command()
def model(name: str):
    path = get_model_path(name)

    if not path:
        print("Model not found. Run pull first.")
        raise typer.Exit()

    runner = LlamaRunner(str(path))

    print(f"Running {name}. Type 'exit' to quit.")

    while True:
        prompt = input(">>> ")

        if prompt.lower() == "exit":
            break

        output = runner.generate(prompt)
        print(output)