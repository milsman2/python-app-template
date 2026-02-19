"""App module for the sample Python application.

This module contains the main components for running the application, including
the metrics server, scheduler, and the main application runner.
"""

from sample_python_app.app.lifecycle import start_metrics_server
from sample_python_app.app.runner import fetch_astro_data
from sample_python_app.app.scheduler import start_scheduler

__all__ = ["start_metrics_server", "start_scheduler", "fetch_astro_data"]
