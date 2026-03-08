"""Lifecycle management for metrics server.

Handles Prometheus metrics server startup and port checks.
"""

import socket

from loguru import logger
from prometheus_client import start_http_server


def start_metrics_server(port: int) -> None:
    """Start the Prometheus metrics server on the specified port."""
    if _port_in_use(port):
        logger.error("Port {} already in use; metrics disabled", port)
        return

    logger.info("Starting Prometheus metrics on 0.0.0.0:{}", port)
    start_http_server(port, addr="0.0.0.0")


def _port_in_use(port: int) -> bool:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        try:
            sock.bind(("localhost", port))
        except OSError:
            return True
    return False
