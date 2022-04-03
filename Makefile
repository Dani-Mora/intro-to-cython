export PYTHONPATH := ${PWD}

setup: requirements.txt
	pip install -r requirements.txt
	pre-commit install

time_original:
	python original/test.py