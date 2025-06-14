
from agent import base_agent_code
from mutate_llm import mutate_agent_code
from benchmark import evaluate
from verifier import prove_output_utility_improves
from versioning import save_version
from cli_approval import ask_user_to_approve

def evolve_agent(max_cycles=5, llm_func=None):
    current_code = base_agent_code
    current_score = evaluate(current_code, llm_func)
    print(f"Current score: {round(current_score, 4)}")

    for cycle in range(max_cycles):
        print(f"\n=== Evolution Cycle {cycle + 1} ===")
        candidate = mutate_agent_code(current_code)
        candidate_score = evaluate(candidate, llm_func)
        print(f"Candidate score: {round(candidate_score, 4)}")

        # lowered threshold for acceptance
        if candidate_score >= current_score + 0.001:
            if prove_output_utility_improves(current_code, candidate):
                approved = ask_user_to_approve(candidate)
                if approved:
                    current_code = candidate
                    current_score = candidate_score
                    save_version(candidate, candidate_score, is_accepted=True)
                    print("Mutation accepted.")
                    continue
                else:
                    save_version(candidate, candidate_score, is_accepted=False)
                    print("Mutation rejected by user.")
            else:
                print("Rejected: Proof of utility improvement failed.")
        else:
            print("Rejected: Score did not improve enough.")
