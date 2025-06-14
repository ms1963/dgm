from z3.z3 import Solver, String, Concat, Length, Not, sat

class SymbolicInterpreter:
    def __init__(self, func_symbol, logic_expression):
        self.func_symbol = func_symbol
        self.logic_expression = logic_expression

    def prove_equivalence(self, func1_expr, func2_expr):
        s = Solver()
        s.add(Not(func1_expr == func2_expr))
        return s.check() != sat

    def prove_utility_improvement(self, utility1_expr, utility2_expr):
        s = Solver()
        s.add(Not(utility2_expr > utility1_expr))
        return s.check() != sat

    def simulate_string_reverse(self, var_name='s'):
        s = String(var_name)
        reversed_expr = Concat(s[3:4], s[2:3], s[1:2], s[0:1])
        return s, reversed_expr

    def simulate_suffix_append(self, suffix):
        s = String('s')
        extended = Concat(s, suffix)
        return s, extended
