"""
Loguru logger configuration for python-app-template.
"""

from loguru import logger

log_format = (
    "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | "
    "<level>{level: <8}</level> | "
    "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - "
    "<level>{message}</level>"
)


def setup_logger(mode="normal"):
    logger.remove()
    if mode == "silent":
        logger.add(
            "app.log",
            format=log_format,
            level="DEBUG",
            rotation="1 MB",
            retention="10 days",
            compression="zip",
        )
    else:
        logger.add(sink=lambda msg: print(msg, end=""), format=log_format, level="INFO")
        logger.add(
            "app.log",
            format=log_format,
            level="DEBUG",
            rotation="1 MB",
            retention="10 days",
            compression="zip",
        )
    return logger
