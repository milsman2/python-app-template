"""Main entry point for the sample Python app.

Starts the Prometheus metrics server and the scheduler.
"""

from sample_python_app.app import start_metrics_server, start_scheduler
from sample_python_app.core import settings, setup_logger

setup_logger(settings.LOG_LEVEL)


def run_app() -> None:
    """Start the metrics server and scheduler."""
    import os

    test_mode = settings.TEST_MODE or os.environ.get("TEST_MODE", "0") in (
        "1",
        "true",
        "True",
    )
    if test_mode:
        # In test mode, do not start servers or infinite loops
        return
    start_metrics_server(port=settings.PROMETHEUS_METRICS_PORT)
    start_scheduler()


if __name__ == "__main__":
    run_app()
