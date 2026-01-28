"""
Docstring for tests.test_main
"""

from src.main import main


def test_main_runs(capfd):
    main()
    out, _ = capfd.readouterr()
    assert "Hello from python-app-template!" in out
