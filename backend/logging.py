"""Backend logging configuration and request logging middleware."""

import logging
from logging.config import dictConfig
from time import perf_counter

from fastapi import Request

from backend.config import Settings


def configure_logging(settings: Settings) -> None:
    """Configure application and uvicorn loggers from runtime settings."""
    log_level = settings.log_level.upper()

    dictConfig(
        {
            "version": 1,
            "disable_existing_loggers": False,
            "formatters": {
                "standard": {
                    "format": "%(asctime)s %(levelname)s [%(name)s] %(message)s",
                }
            },
            "handlers": {
                "default": {
                    "class": "logging.StreamHandler",
                    "formatter": "standard",
                }
            },
            "root": {
                "level": log_level,
                "handlers": ["default"],
            },
            "loggers": {
                "uvicorn": {
                    "level": log_level,
                },
                "uvicorn.error": {
                    "level": log_level,
                },
                "uvicorn.access": {
                    "level": log_level,
                },
                "pictureme": {
                    "level": log_level,
                    "handlers": ["default"],
                    "propagate": False,
                },
            },
        }
    )


async def log_requests(request: Request, call_next):
    """Log one structured line per request with status and duration."""
    logger = logging.getLogger("pictureme.http")
    started_at = perf_counter()
    response = await call_next(request)
    duration_ms = (perf_counter() - started_at) * 1000

    logger.info(
        '%s %s -> %s in %.2fms',
        request.method,
        request.url.path,
        response.status_code,
        duration_ms,
    )

    return response
