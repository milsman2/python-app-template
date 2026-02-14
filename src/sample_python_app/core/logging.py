"""Loguru logger configuration for python-app-template."""

import sys

from loguru import logger

log_format = (
    "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | "
    "<level>{level: <8}</level> | "
    "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - "
    "<level>{message}</level>"
)


def setup_logger(mode="normal"):
    """Configure and return a Loguru logger instance.

    Args:
        mode (str, optional): Logging mode. "normal" for console and file logging,
            "silent" for file logging only. Defaults to "normal".

    Returns:
        logger: Configured Loguru logger instance.

    """
    logger.remove()
    if mode == "silent":
        # Log errors to the console even in silent mode
        logger.add(
            sink=lambda msg: sys.stdout.write(msg), format=log_format, level="ERROR"
        )
        logger.add(
            "app.log",
            format=log_format,
            level="DEBUG",
            rotation="1 MB",
            retention="10 days",
            compression="zip",
        )
    else:
        logger.add(
            sink=lambda msg: sys.stdout.write(msg), format=log_format, level="INFO"
        )
        logger.add(
            "app.log",
            format=log_format,
            level="DEBUG",
            rotation="1 MB",
            retention="10 days",
            compression="zip",
        )
    return logger
