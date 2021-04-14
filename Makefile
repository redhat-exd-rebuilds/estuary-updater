.PHONY: test dependencies

pin_dependencies:
		tox -e pin-dependencies

test:
		tox -r

dependencies:
		python -m pip install --upgrade pip
		pip install tox
