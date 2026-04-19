"""Shared error handling for the FastAPI backend."""

import logging

from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

logger = logging.getLogger("pictureme-backend")


class AppError(Exception):
    """Application-level error with a stable JSON response shape."""

    def __init__(
        self,
        message: str,
        code: str = "INTERNAL_ERROR",
        status: int = 500,
        details: dict[str, object] | None = None,
    ) -> None:
        super().__init__(message)
        self.code = code
        self.details = details
        self.message = message
        self.status = status


def buildErrorResponse(
    message: str,
    code: str,
    status: int,
    details: dict[str, object] | None = None,
) -> JSONResponse:
    payload: dict[str, object] = {"message": message, "code": code}
    if details is not None:
        payload["details"] = details
    return JSONResponse(status_code=status, content=payload)


def registerErrorHandlers(app: FastAPI) -> None:
    @app.exception_handler(AppError)
    async def appErrorHandler(_request: Request, exc: AppError) -> JSONResponse:
        return buildErrorResponse(exc.message, exc.code, exc.status, exc.details)

    @app.exception_handler(RequestValidationError)
    async def validationErrorHandler(
        _request: Request,
        exc: RequestValidationError,
    ) -> JSONResponse:
        return buildErrorResponse(
            "The request payload is invalid.",
            "VALIDATION_ERROR",
            422,
            {"errors": exc.errors()},
        )

    @app.exception_handler(404)
    async def notFoundHandler(_request: Request, _exc: Exception) -> JSONResponse:
        return buildErrorResponse("Not found", "NOT_FOUND", 404)

    @app.exception_handler(Exception)
    async def genericErrorHandler(_request: Request, exc: Exception) -> JSONResponse:
        logger.exception("Unhandled backend error", exc_info=exc)
        return buildErrorResponse(
            "PictureMe could not complete the request.",
            "INTERNAL_SERVER_ERROR",
            500,
        )
