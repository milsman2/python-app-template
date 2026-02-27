"""Docstring for tests.test_main."""

import subprocess
import sys

from sample_python_app.app.runner import fetcher


def test_main_subprocess():
    """Test main subprocess execution."""
    import os

    env = os.environ.copy()
    env["TEST_MODE"] = "1"
    result = subprocess.run(
        [sys.executable, "-m", "src.sample_python_app.main"],
        capture_output=True,
        text=True,
        check=True,
        env=env,
    )
    assert result.returncode == 0


def test_main_runs(capfd):
    """Test main run_app output."""
    # Call fetch_astro_data directly to test output
    # Ensure display will occur during test
    if hasattr(fetcher, "reset_display"):
        fetcher.reset_display()
    fetcher.fetch()
    out, _ = capfd.readouterr()
    assert "Sunrise" in out
    assert "Sunset" in out
    assert "Astronomical Twilight Begin" in out
