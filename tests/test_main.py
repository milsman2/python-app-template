"""
Docstring for tests.test_main
"""

import subprocess
import sys

from src.main import main


def test_main_subprocess():
    result = subprocess.run(
        [sys.executable, "-m", "src.main"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.returncode == 0


def test_main_runs(capfd):
    main()
    out, _ = capfd.readouterr()
    assert "Hello from python-app-template!" in out
