import argparse
from dgm.agent import PromptAgent
from llm_interface import query_openai

def run_cli():
    parser = argparse.ArgumentParser(description="Darwin-Gödel CLI")
    parser.add_argument("prompt", type=str, help="Input prompt")
    args = parser.parse_args()

    agent = PromptAgent()
    transformed = agent.act(args.prompt)
    result = query_openai(transformed)
    print("Transformed Prompt:", transformed)
    print("LLM Completion:", result)
