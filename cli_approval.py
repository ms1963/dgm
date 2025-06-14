import readline

def ask_user_to_approve(code):
    print("\n=== Candidate Mutated Agent ===\n")
    print(code)
    print("\n=== End of Candidate ===")
    response = input("Approve this mutation? [y/N]: ").strip().lower()
    return response == "y"
