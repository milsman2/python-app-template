"""Scheduler module to fetch astronomical data every 24 hours."""

import signal
import sys
from datetime import UTC, datetime

from apscheduler.schedulers.blocking import BlockingScheduler
from loguru import logger

from sample_python_app.app.runner import fetcher
from sample_python_app.core.logging import setup_logger


def start_scheduler(test_mode: bool = False) -> None:
    """Start the scheduler to fetch astronomical data every 24 hours."""
    setup_logger("normal")
    scheduler_logger = logger.bind(component="scheduler")

    if test_mode:
        fetcher.fetch(exit_on_error=False)
        return

    scheduler = BlockingScheduler(timezone="UTC")

    def shutdown(signum, frame):
        del frame
        scheduler_logger.debug("Shutdown signal received", signal=signum)
        scheduler.shutdown(wait=True)
        sys.exit(0)

    signal.signal(signal.SIGTERM, shutdown)
    signal.signal(signal.SIGINT, shutdown)

    scheduler.add_job(
        fetcher.fetch,
        trigger="interval",
        hours=24,
        next_run_time=datetime.now(UTC),
        misfire_grace_time=3600,
        coalesce=True,
        max_instances=1,
    )

    scheduler_logger.info("Scheduler started")
    scheduler.start()
