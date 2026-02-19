"""Scheduler module for periodic astronomical data fetch.

Initializes and runs the APScheduler job every 24 hours.
"""

from datetime import datetime

from apscheduler.schedulers.blocking import BlockingScheduler

from sample_python_app.app.runner import fetch_astro_data
from sample_python_app.core.logging import setup_logger

logger = setup_logger("normal")


def start_scheduler(test_mode: bool = False) -> None:
    """Start the scheduler to run the astronomical data fetch every 24 hours.

    In test_mode, run the scheduled job once and do not block.
    """
    scheduler = BlockingScheduler()
    scheduler.add_job(
        fetch_astro_data,
        trigger="interval",
        hours=24,
        next_run_time=datetime.now(),
    )
    logger.info("Scheduled astronomical fetch every 24 hours")
    if test_mode:
        # Run the job once for testing, do not block
        job = scheduler.get_jobs()[0]
        job.func()
        logger.info("Ran scheduled job once in test mode")
        return
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        logger.info("Scheduler stopped")
        scheduler.shutdown()
