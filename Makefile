export PYTHONPATH := ${PWD}

setup: requirements.txt
	pip install -r requirements.txt
	pre-commit install

time_original:
	python original/test.py

COMPILE_DIR=compile
time_compile:
	cd ${COMPILE_DIR} && python setup.py build_ext --inplace
	cd ${COMPILE_DIR} && python test.py
