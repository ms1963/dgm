import requests
import os

def query_openai(prompt):
    import openai
    openai.api_key = os.getenv("OPENAI_API_KEY")
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.4
    )
    return response.choices[0].message.content.strip()

def query_claude(prompt):
    import anthropic
    client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
    response = client.messages.create(
        model="claude-3-opus-20240229",
        max_tokens=1024,
        temperature=0.4,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.content[0].text.strip()

def query_ollama(prompt, model="llama3"):
    response = requests.post("http://localhost:11434/api/generate", json={
        "model": model,
        "prompt": prompt,
        "stream": False
    })
    if response.ok:
        return response.json()["response"].strip()
    raise RuntimeError("Ollama LLM failed: " + response.text)
