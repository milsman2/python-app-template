#!/usr/bin/env bash
# Run project linting, formatting and tests using `uv` as in this repo.
set -euo pipefail

# Change to repo root (script placed in scripts/)
cd "$(dirname "$0")/.."

echo "⚡ Running ruff (auto-fix where possible)"
uv run ruff check . --fix

echo "⚡ Running isort"
uv run isort .

echo "⚡ Running black"
uv run black .

echo "⚡ Re-running ruff to catch any remaining issues"
uv run ruff check .

echo "⚡ Running tests"
uv run -- coverage run -m pytest

echo "All checks completed."
