import itertools

def generate_mutations(base_code: str, primitives: list, max_variants=5):
    mutations = set()
    for p in primitives:
        mutated = base_code.replace("prompt", f"{p}(prompt)" if '(' not in p else f"{p}")
        mutations.add(mutated)
        if len(mutations) >= max_variants:
            break
    return list(mutations)
