# Snippets from AC-IT Monorepo

PATH_ARG ?= aoc

# Setup development environment
.PHONY: setup
setup:
	uv sync
	uv run pre-commit install


# Format code with optional path
.PHONY: format
format:
	uv run ruff format $(PATH_ARG)

# Lint code with optional path
.PHONY: lint
lint:
	uv run ruff check --fix $(PATH_ARG)

# Lint code with optional path
.PHONY: lint-unsafe
lint-unsafe:
	uv run ruff check --unsafe-fixes --fix $(PATH_ARG)


# Clean temporary files
.PHONY: clean
clean:
	find . -name "__pycache__" -exec rm -rf {} +
	rm -rf .pytest_cache .mypy_cache .ruff_cache

# Run type checking with optional path
.PHONY: typecheck
typecheck:
	uv run mypy $(PATH_ARG) --explicit-package-bases || true
