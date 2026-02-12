"""
Docstring for tests.test_main
"""

import subprocess
import sys

from sample_python_app import main


def test_main_subprocess():
    result = subprocess.run(
        [sys.executable, "-m", "src.sample_python_app.main"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.returncode == 0


def test_main_runs(capfd):
    main.run_app()
    out, _ = capfd.readouterr()
    assert "Sunrise" in out
    assert "Sunset" in out
    assert "Astronomical Twilight Begin" in out
