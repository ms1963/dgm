def detect_hallucination(output: str, references: list):
    for ref in references:
        if ref.lower() in output.lower():
            return False
    return True
