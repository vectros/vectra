import json
import requests
from pathlib import Path

MODEL_DIR = Path("models")
MODEL_DIR.mkdir(exist_ok=True)

REGISTRY_PATH = MODEL_DIR / "registry.json"

_DEFAULT_REGISTRY = {
    "mistral": "https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.1-GGUF/resolve/main/mistral-7b-instruct-v0.1.Q4_K_M.gguf",
    "phi": "https://huggingface.co/TheBloke/phi-2-GGUF/resolve/main/phi-2.Q4_K_M.gguf",
}


class Registry:
    def __init__(self, path: Path = REGISTRY_PATH):
        self.path = path
        if not self.path.exists():
            self._save(_DEFAULT_REGISTRY)

    def _load(self) -> dict:
        with open(self.path, "r") as f:
            return json.load(f)

    def _save(self, data: dict):
        with open(self.path, "w") as f:
            json.dump(data, f, indent=2)

    def list(self) -> dict:
        return self._load()

    def get(self, name: str) -> str | None:
        return self._load().get(name)

    def add(self, name: str, url: str):
        data = self._load()
        data[name] = url
        self._save(data)

    def remove(self, name: str):
        data = self._load()
        if name not in data:
            raise KeyError(f"Model '{name}' not in registry")
        del data[name]
        self._save(data)


registry = Registry()


def list_models():
    return [f.name for f in MODEL_DIR.glob("*.gguf")]

def get_model_path(name: str):
    path = MODEL_DIR / f"{name}.gguf"
    return path if path.exists() else None


def download_model(name: str):
    url = registry.get(name)
    if not url:
        raise ValueError(f"Model '{name}' not in registry. Add it with: vectra registry add {name} <url>")

    path = MODEL_DIR / f"{name}.gguf"

    if path.exists():
        return path

    print(f"Downloading {name}...")

    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(path, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)

    return path