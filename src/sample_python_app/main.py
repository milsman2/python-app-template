"""Main entry point for the sample Python app.

Starts the Prometheus metrics server and the scheduler.
"""

from sample_python_app.app import start_metrics_server, start_scheduler
from sample_python_app.core import settings


def run_app() -> None:
    """Start the metrics server and scheduler."""
    if settings.TEST_MODE:
        return
    start_metrics_server(port=settings.PROMETHEUS_METRICS_PORT)
    start_scheduler()


if __name__ == "__main__":
    run_app()
