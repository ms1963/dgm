# Darwin–Gödel Machine (DGM)

The Darwin–Gödel Machine is a self-improving, formally verifiable AI system that mutates its own agents, proves improvements, and evolves toward higher utility.

## Features

- ✅ Uses LLMs (OpenAI, Claude, Ollama) to mutate agent code.
- ✅ Evaluates semantic utility using smarter benchmark prompts.
- ✅ Formally proves that changes improve utility using Z3.
- ✅ Static analysis rejects hallucinated or dangerous code.
- ✅ Human-in-the-loop approval before mutation acceptance.
- ✅ Persistent versioning of all generated agents.
- ✅ Supports both CLI and GUI integration (optional).
- ✅ Modular architecture and extensible design.

## Installation

Install all dependencies:

```bash
make install


Ensure you have a valid OpenAI/Antrophic API key or an Ollama-compatible LLM installed. Per default Ollama (Mistral) is used. If you need to use OpenAI or Antrophic APIs instead, you need to change this in the code.

**Running the Evolution Loop**

make run


This command launches the evolution loop with:
	•	5 cycles of agent self-improvement
	•	Formal utility checks
	•	CLI-based human approval prompts
	•	Version storage in the agents/ directory

Project Structure
	•	agent.py – contains the base agent definition
	•	mutate_llm.py – LLM-based agent mutation logic
	•	benchmark.py – smart scoring of agent behavior
	•	verifier.py – formal logic proofs using Z3
	•	versioning.py – persistent version archiving
	•	evolution_loop.py – mutation-evaluation-approval loop
	•	static_analyzer.py – hallucination and safety checks
	•	cli_approval.py – CLI review interface

License

MIT – See LICENSE.md

Authors

This is an experimental project inspired by the theoretical Darwin–Gödel Machine proposed by Jürgen Schmidhuber and others.

📘 How It Works – Darwin–Gödel Machine Explained

This project is a sophisticated implementation of a Darwin–Gödel Machine (DGM) — a theoretical construct that combines evolutionary improvement (Darwin) with formal self-verification (Gödel) to create provably self-improving software.

🔁 Overview: What Does the Program Do?

The Darwin–Gödel Machine begins with a baseline agent that performs a simple task — in this case, it defines a transform(prompt) function which processes text prompts. Over a sequence of evolution cycles, the program:
	1.	Mutates the agent code using an integrated LLM (e.g. via Ollama or OpenAI).
	2.	Evaluates how good the new version is at transforming prompts.
	3.	Proves whether the new version is better and still correct.
	4.	Asks a human for final approval before accepting the mutation.
	5.	Saves the improved agent version for versioning.

The machine repeats this loop, evolving smarter and more detailed agents over time.

🧠 Components and Workflow
	•	agent.py: Contains the base agent’s transform function.
	•	mutate_llm.py: Sends the agent to the LLM to create mutations.
	•	benchmark.py: Evaluates each mutation by scoring prompt responses.
	•	verifier.py: Proves that a mutation is an improvement and correct.
	•	cli_approval.py: Asks a human to approve the mutation.
	•	versioning.py: Saves accepted or rejected mutations for tracking.
	•	evolution_loop.py: Orchestrates the full evolution process.
	•	Makefile: Automates installation, running, and cleaning.

✅ Why It Is a DGM
	•	Darwinian Evolution: Mutations are scored and selected based on fitness.
	•	Gödelian Reasoning: Only provably beneficial changes are accepted.
	•	Self-Reference: The agent updates its own behavior iteratively.
	•	Formal Guarantees: Verifier modules prove correctness and safety.

This implementation can be extended to train intelligent systems for dialog, summarization, or code generation — with provable improvements.

