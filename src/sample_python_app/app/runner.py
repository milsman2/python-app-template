"""Runner module for the sample Python app.

Handles fetching, validation, and display of astronomical data.
"""

# app/runner.py
import json
import time

import httpx
from pydantic import ValidationError

from sample_python_app.core import (
    FETCH_COUNTER,
    FETCH_DURATION,
    FETCH_ERRORS,
    display_astronomical_data,
    setup_logger,
    weather_settings,
)
from sample_python_app.exceptions import AppError
from sample_python_app.services import fetch_astronomical_data_from_api

logger = setup_logger("normal")


def fetch_astro_data(*, exit_on_error: bool = True) -> None:
    """Fetch and display astronomical data once, with error handling."""
    lat = weather_settings.LOCATION.latitude
    lon = weather_settings.LOCATION.longitude
    logger.info(f"Using latitude={lat} longitude={lon}")

    start = time.time()

    try:
        astro = fetch_astronomical_data_from_api(lat, lon)
        FETCH_COUNTER.inc()
    except httpx.HTTPStatusError as exc:
        _handle_fetch_error(exc, exit_on_error)
        return
    except httpx.RequestError as exc:
        _handle_fetch_error(exc, exit_on_error)
        return
    except ValidationError as exc:
        _handle_fetch_error(exc, exit_on_error)
        return
    except json.JSONDecodeError as exc:
        _handle_fetch_error(exc, exit_on_error)
        return
    except AppError as exc:
        _handle_fetch_error(exc, exit_on_error)
        return
    finally:
        FETCH_DURATION.observe(time.time() - start)

    display_astronomical_data(astro)


def _handle_fetch_error(exc: Exception, exit_on_error: bool) -> None:
    """Handle errors during the fetch operation.

    Log appropriately and update metrics.
    """
    FETCH_ERRORS.inc()
    if isinstance(exc, httpx.HTTPStatusError):
        logger.error("HTTP status error: %s", exc)
    elif isinstance(exc, httpx.RequestError):
        logger.error("Network error: %s", exc)
    elif isinstance(exc, ValidationError):
        logger.error("Validation error: %s", exc)
    elif isinstance(exc, json.JSONDecodeError):
        logger.error("JSON decode error: %s", exc)
    else:
        logger.exception("Unexpected error")

    if exit_on_error:
        raise SystemExit(1) from exc

    raise AppError(str(exc)) from exc
