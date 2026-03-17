from llama_cpp import Llama
from pathlib import Path

class LlamaRunner:
    def __init__(self, model_path: str):
        if not Path(model_path).exists():
            raise FileNotFoundError(f"Model not found: {model_path}")

        self.llm = Llama(
            model_path=model_path,
            n_ctx=2048,
            n_threads=4
        )

    def generate(self, prompt: str):
        output = self.llm(
            prompt,
            max_tokens=512,
            stop=["</s>"]
        )
        return output["choices"][0]["text"]