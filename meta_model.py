class FormalAgentModel:
    def __init__(self, code: str, utility_name: str = "informational_gain"):
        self.code = code
        self.utility_name = utility_name

    def evaluate_utility(self, output: str) -> float:
        if self.utility_name == "informational_gain":
            return self._informational_gain(output)
        return 0.0

    def _informational_gain(self, text: str) -> float:
        informative_keywords = [
            "compressor", "turbine", "photosynthesis", "glucose",
            "sunlight", "chemical", "energy", "reaction", "fuel", "combustion"
        ]
        return sum(1.0 for word in informative_keywords if word.lower() in text.lower())

    def to_axioms(self) -> str:
        return f"(define-agent \"{self.code[:60].replace(chr(10), ' ')}...\" with-utility {self.utility_name})"
