"""Utility scripts exposed via pyproject `project.scripts`.

Provides `run_checks()` which runs linters, formatters and tests.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

from loguru import logger

from sample_python_app.core.logging import setup_logger

ROOT = Path(__file__).resolve().parents[2]

setup_logger("DEBUG")


def _run(cmd: list[str]) -> None:
    logger.info(f"Running: {' '.join(cmd)}")
    subprocess.check_call(cmd, cwd=str(ROOT))


def run_checks() -> None:
    """Run ruff, isort, black and tests (coverage+pytest).

    This is intended to be invoked via the project script entrypoint, e.g.:
    `uv run checks` or `python -m sample_python_app.scripts run_checks` when installed.
    """
    py = sys.executable
    _run([py, "-m", "ruff", "check", ".", "--fix", "--exit-zero"])
    _run([py, "-m", "isort", "."])
    _run([py, "-m", "black", "."])
    _run([py, "-m", "ruff", "check", ".", "--exit-zero"])
    _run([py, "-m", "coverage", "run", "-m", "pytest"])

    logger.info("All checks completed.")
