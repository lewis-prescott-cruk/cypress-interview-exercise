default:
	@echo "make <target>"
	@echo "	test	run all tests"
	@echo "	doctest	run doctests"
	@echo "	unit	run unit tests in tests/"

test:
	$(MAKE) unit doctest

unit:
	python3 -m unittest discover --verbose --start-directory tests/

doctest:
	python3 exercise/__init__.py

lint:
	flake8
