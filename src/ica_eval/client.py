"""Sends chat requests to a local model through Ollama's HTTP API."""
import requests

OLLAMA_URL = "http://127.0.0.1:11434"


def chat(model, messages, url=OLLAMA_URL, timeout=120):
    # temperature 0 and a fixed seed, so the same prompt gives the same answer on every run
    response = requests.post(
        f"{url}/api/chat",
        json={
            "model": model,
            "messages": messages,
            "stream": False,
            "options": {"temperature": 0, "seed": 42},
        },
        timeout=timeout,
    )
    response.raise_for_status()
    return response.json()["message"]["content"]
