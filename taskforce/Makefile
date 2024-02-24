install-poetry:
	pip install poetry

install-deps:
	poetry install --no-root

install:
	poetry install --no-root

install-deps-prod:
	poetry install --no-dev --no-root

run-app:
	poetry run python main.py

run:
	poetry run python main.py

lint:
	ruff format
	ruff --fix

run-tests:
	poetry run pytest run_tests.py --emoji
