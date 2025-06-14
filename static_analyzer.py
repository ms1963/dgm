import ast

UNSAFE_PATTERNS = {"eval", "exec", "os.system", "subprocess", "open", "__import__", "compile"}

def is_safe_code(code):
    try:
        tree = ast.parse(code)
        for node in ast.walk(tree):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
                if node.func.id in UNSAFE_PATTERNS:
                    return False
            elif isinstance(node, ast.Attribute):
                full_name = f"{getattr(node.value, 'id', '')}.{node.attr}"
                if full_name in UNSAFE_PATTERNS:
                    return False
    except SyntaxError:
        return False
    return True
