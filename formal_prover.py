from symbolic_interpreter import SymbolicInterpreter
from z3.z3 import String, Length, Concat

def prove_output_utility_improves(old_output, new_output):
    s = String('s')
    old_len = Length(old_output)
    new_len = Length(new_output)
    prover = SymbolicInterpreter("f", "string")
    return prover.prove_utility_improvement(old_len, new_len)

def prove_output_equivalence(old_expr, new_expr):
    prover = SymbolicInterpreter("f", "string")
    return prover.prove_equivalence(old_expr, new_expr)
