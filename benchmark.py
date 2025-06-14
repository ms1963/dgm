import difflib
import traceback

def evaluate(agent_code, llm_func=None):
    prompts = [
        "Explain the theory of evolution.",
        "Summarize quantum entanglement.",
        "Translate 'Hello World' to French.",
        "What is the difference between classical and quantum computing?",
        "Describe the concept of entropy in thermodynamics.",
        "Explain recursion in programming.",
        "How do LLMs differ from symbolic AI?",
        "What are edge cases in prompt interpretation?",
        "Give an example of a metaphor and explain it.",
        "Describe how a neural network learns."
    ]
    expectations = [
        "theory of evolution explains how species change over time",
        "quantum entanglement links particles no matter the distance",
        "Bonjour le monde",
        "quantum uses superposition and entanglement, classical does not",
        "entropy is a measure of disorder",
        "recursion is when a function calls itself",
        "LLMs use statistical learning, symbolic AI uses rules",
        "edge cases are unexpected inputs or rare conditions",
        "a metaphor is a figure of speech comparing two things",
        "a neural network adjusts weights to minimize error"
    ]
    score = 0
    try:
        local_ns = {}
        exec(agent_code, local_ns)
        transform = local_ns.get("transform")
        if not transform:
            return 0.0

        for prompt, expected in zip(prompts, expectations):
            try:
                output = transform(prompt)
                ratio = difflib.SequenceMatcher(None, output.lower(), expected.lower()).ratio()
                score += ratio
            except Exception:
                score += 0.0
    except Exception as e:
        traceback.print_exc()
        return 0.0

    return score / len(prompts)
