"""System and foundation routes."""

import logging
from datetime import datetime, timezone
from time import perf_counter
from typing import Awaitable, Callable

from fastapi import APIRouter, Depends, FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware

from backend.config import getSettings
from backend.deps import requireAuthenticatedUser, requireInternalSecret
from backend.errors import registerErrorHandlers

router = APIRouter(tags=["system"])
logger = logging.getLogger("pictureme-backend")


class RequestLoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(
        self,
        request: Request,
        callNext: Callable[[Request], Awaitable[Response]],
    ) -> Response:
        startTime = perf_counter()
        response = await callNext(request)
        durationMs = round((perf_counter() - startTime) * 1000, 2)
        logger.info(
            "%s %s -> %s in %sms",
            request.method,
            request.url.path,
            response.status_code,
            durationMs,
        )
        return response


@router.get("/api/health")
async def healthCheck() -> dict[str, str]:
    return {
        "service": "pictureme-backend",
        "status": "ok",
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }


@router.get("/api/runtime-config")
async def runtimeConfig() -> dict[str, object]:
    return getSettings().publicConfig


@router.get("/api/debug/auth-check")
async def authCheck(
    authenticatedUser: dict[str, object] = Depends(requireAuthenticatedUser),
) -> dict[str, object]:
    return {
        "email": authenticatedUser.get("email"),
        "userId": authenticatedUser.get("userId"),
    }


@router.get("/api/debug/internal-check")
async def internalCheck(
    _internalAccess: None = Depends(requireInternalSecret),
) -> dict[str, str]:
    return {"status": "ok"}


def createApp() -> FastAPI:
    settings = getSettings()

    logging.basicConfig(
        format="%(asctime)s %(levelname)s %(name)s %(message)s",
        level=getattr(logging, settings.logLevel.upper(), logging.INFO),
    )

    app = FastAPI(
        title="PictureMe API",
        version="0.2.0",
        docs_url="/api/docs" if settings.isDevelopment else None,
        redoc_url="/api/redoc" if settings.isDevelopment else None,
    )
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[settings.frontendOrigin, settings.appOrigin],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.add_middleware(RequestLoggingMiddleware)
    registerErrorHandlers(app)
    return app
