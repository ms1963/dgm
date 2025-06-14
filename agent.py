base_agent_code = """
def transform(prompt):
    prompt = prompt.capitalize()
    if not prompt:
        return "Please provide a valid prompt."
    if len(prompt) > 250:
        return "The prompt is too long. Please shorten it to 250 characters or less."
    return f"Here's my understanding of your prompt: {prompt} Please be as accurate and detailed as possible."
"""
