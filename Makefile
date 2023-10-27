DIRS_PYTHON := src tests

.PHONY: default
default: lint test

.PHONY: test
test:
	pipenv run pytest

.PHONY: format
format: format-isort format-black

.PHONY: format-isort
format-isort:
	pipenv run isort --profile=black $(DIRS_PYTHON)

.PHONY: format-black
format-black:
	pipenv run black --line-length 100 $(DIRS_PYTHON)

.PHONY: format-smithy
format-smithy:
	smithy format model/*

.PHONY: lint
lint: lint-isort lint-black lint-flake8 lint-smithy

.PHONY: lint-isort
lint-isort:
	pipenv run isort --profile=black --check-only --diff $(DIRS_PYTHON)

.PHONY: lint-black
lint-black:
	pipenv run black --line-length 100 $(DIRS_PYTHON)

.PHONY: lint-flake8
lint-flake8:
	pipenv run flake8 --max-line-length 100 $(DIRS_PYTHON)

.PHONY: lint-smithy
lint-smithy:
	smithy validate model/*

.PHONY: install-deps
install-deps:
	pipenv install --categories=packages,dev-packages

.PHONY: smithy-build
smithy-build:
	# generate client package
	smithy build
	# install generated client package
	pip install -e build/smithy/client/python-client-codegen
