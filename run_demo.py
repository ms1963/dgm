"""
Run a demonstration of the Darwin–Gödel Machine.
Performs one generation of evolution and prints results.
"""

from agent import PromptAgent
from benchmark import evaluate
from mutate_llm import mutate_agent_code
from formal_prover import prove_output_equivalence, prove_output_utility_improves
from verifier import ast_cost
from z3.z3 import String, Concat
import ast

def run_demo():
    current = PromptAgent()
    base_score = evaluate(current, lambda prompt: "Photosynthesis converts sunlight into glucose.")

    print("Base agent code:")
    print(current.to_code())
    print("Base score:", base_score)

    code = current.to_code()
    mutated_code = mutate_agent_code(code)
    local_ns = {}
    exec(mutated_code, local_ns)
    new_agent = PromptAgent(transform=local_ns['transform'])

    new_score = evaluate(new_agent, lambda prompt: "Photosynthesis converts sunlight into glucose.")

    print("\nMutated agent code:")
    print(mutated_code)
    print("New score:", new_score)

    old_expr = Concat(String('s'), " Please be as accurate and detailed as possible.")
    new_expr = Concat(String('s'), " Please be as accurate, detailed and technically precise as possible.")

    equivalent = prove_output_equivalence(old_expr, new_expr)
    improved = prove_output_utility_improves(old_expr, new_expr)

    print("\nProofs:")
    print("Equivalence proven:", equivalent)
    print("Utility improvement proven:", improved)

if __name__ == "__main__":
    run_demo()
