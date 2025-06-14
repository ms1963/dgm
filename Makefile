.PHONY: install run clean

install:
	pip install -r requirements.txt

run:
	python -c "from evolution_loop import evolve_agent; evolve_agent(max_cycles=5)"

clean:
	rm -rf __pycache__ agents/*.py
