"""
Main entry point for the python-app-template project.
"""

from sample_python_app.core import settings, setup_logger


def run_app():
    logger = setup_logger()
    logger.info(f"Starting {settings.APP_NAME}...")
    logger.info("Hello from python-app-template!")


if __name__ == "__main__":  # pragma: no cover
    run_app()
