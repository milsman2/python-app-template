"""Tests for sample_python_app.core.logging."""

import time

from loguru import logger as loguru_logger

from sample_python_app.core.logging import setup_logger


def test_logger_normal_mode_stdout(capsys):
    """Test logger normal mode outputs to stdout."""
    logger = setup_logger("normal")
    logger.info("Test normal mode log")
    out, _ = capsys.readouterr()
    assert "Test normal mode log" in out


def test_logger_silent_mode_no_stdout(capsys):
    """Test logger silent mode does not output to stdout."""
    logger = setup_logger("silent")
    logger.info("Test silent mode log")
    out, _ = capsys.readouterr()
    assert "Test silent mode log" not in out


def test_logger_file_logging(tmp_path):
    """Test logger file logging to app.log."""
    log_path = tmp_path / "app.log"
    loguru_logger.remove()
    loguru_logger.add(str(log_path), format="{message}", level="DEBUG")
    loguru_logger.info("File log test")
    time.sleep(0.1)
    with open(log_path, encoding="utf-8") as f:
        contents = f.read()
    assert "File log test" in contents
