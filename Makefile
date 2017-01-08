bootstrap:
	pip install -r requirements.txt

lint:
	flake8 **/*.py

test:
	PYTHONPATH=src python -m unittest discover -s test -v

cover:
	PYTHONPATH=src coverage run --source=src -m unittest discover -s test -v
	coverage report -m

serve:
	PYTHONPATH=src python src/wekan_api.py


.PHONY: bootstrap lint test
