export PYTHONPATH := ${PWD}

setup: requirements.txt
	pip install -r requirements.txt
	pre-commit install

time_original:
	python original/test.py

time_dir:
	cd ${FOLDER} && python setup.py build_ext --inplace
	cd ${FOLDER} && python test.py

time_compile:
	$(MAKE) time_dir FOLDER=compile

time_ctypes:
	$(MAKE) time_dir FOLDER=ctypes

time_memview:
	$(MAKE) time_dir FOLDER=memview