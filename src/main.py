"""
Main entry point for the python-app-template project.
"""

from src.core import settings, setup_logger


def main():
    logger = setup_logger()
    logger.info(f"Starting {settings.APP_NAME}...")
    logger.info("Hello from python-app-template!")


if __name__ == "__main__":
    main()
