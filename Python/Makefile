default:
	@echo "make <target>"
	@echo "	test	run all tests"
	@echo "	doctest	run doctests"
	@echo "	unit	run unit tests in tests/"

test:
	$(MAKE) unit doctest

unit:
	pipenv run python3 -m unittest discover --verbose --start-directory tests/

doctest:
	pipenv run python3 exercise/__init__.py

lint:
	pipenv run flake8
