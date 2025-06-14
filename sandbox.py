import io
import contextlib

class SandboxedExecutor:
    def __init__(self, timeout=2):
        self.timeout = timeout

    def safe_exec(self, code: str, func_name: str, test_input: str):
        local_env = {}
        stdout_capture = io.StringIO()
        try:
            with contextlib.redirect_stdout(stdout_capture):
                exec(code, {}, local_env)
                result = local_env[func_name](test_input)
            return result
        except Exception as e:
            return f"Error during execution: {str(e)}"
