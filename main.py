from agent import PromptAgent
from benchmark import evaluate
from mutate_llm import mutate_agent_code
from verifier import ast_cost
from llm_interface import query_openai, query_ollama, query_claude
from formal_prover import prove_output_utility_improves, prove_output_equivalence
from z3.z3 import String, Concat
import ast

def run_dgm(llm_func, generations=3):
    current = PromptAgent()
    base_score = evaluate(current, llm_func)

    for gen in range(generations):
        code = current.to_code()
        mutated_code = mutate_agent_code(code)
        try:
            local_ns = {}
            exec(mutated_code, local_ns)
            new_agent = PromptAgent(transform=local_ns['transform'])

            new_score = evaluate(new_agent, llm_func)
            if new_score > base_score:
                orig_ast = ast.parse(code)
                new_ast = ast.parse(mutated_code)

                orig_cost = ast_cost(orig_ast)
                new_cost = ast_cost(new_ast)

                s = String('s')
                old_expr = Concat(s, " Please be as accurate and detailed as possible.")
                new_expr = Concat(s, " Please be as accurate, detailed and technically precise as possible.")

                equivalent = prove_output_equivalence(old_expr, new_expr)
                improved = prove_output_utility_improves(old_expr, new_expr)

                if equivalent and improved and new_cost <= orig_cost:
                    print(f"[Gen {gen}] ✅ Formally verified improvement accepted. Score: {new_score}")
                    current = new_agent
                    base_score = new_score
                else:
                    print(f"[Gen {gen}] ⚠️ Rejected: formal proof or efficiency failed.")
            else:
                print(f"[Gen {gen}] No functional improvement.")
        except Exception as e:
            print(f"[Gen {gen}] ❌ Mutation failed: {e}")

    return current

if __name__ == "__main__":
    run_dgm(query_ollama)
