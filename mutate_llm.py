import subprocess
import re

def mutate_agent_code(agent_code):
    prompt = (
        "You are an AI agent mutator.\n"
        "Given the following agent code, return a better version that improves its detail and correctness.\n\n"
        f"{agent_code}\n\n"
        "Make sure to return only a Python function named 'transform'. Do not include explanations or markdown.\n"
    )

    result = subprocess.run(
        ["ollama", "run", "mistral"],
        input=prompt.encode("utf-8"),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

    output = result.stdout.decode("utf-8")

    # extract only the transform function
    match = re.search(r"(?s)^def transform\(.*?\):.*?(?=^\\S|\\Z)", output, re.MULTILINE)
    if match:
        return match.group().strip()
    else:
        return ""  # fallback if no valid function is found
