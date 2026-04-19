"""Shared backend dependencies and Supabase helpers."""

import secrets
from functools import lru_cache
from typing import Annotated

from fastapi import Depends, Header, Request
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from supabase import Client, create_client

from backend.config import getSettings
from backend.errors import AppError

bearerScheme = HTTPBearer(auto_error=False)


@lru_cache
def getSupabaseAdminClient() -> Client:
    settings = getSettings()
    return create_client(settings.supabaseUrl, settings.supabaseSecretKeyValue)


async def requireAuthenticatedUser(
    request: Request,
    credentials: HTTPAuthorizationCredentials | None = Depends(bearerScheme),
) -> dict[str, object]:
    if credentials is None or not credentials.credentials:
        raise AppError(
            "A valid bearer token is required.",
            code="AUTH_REQUIRED",
            status=401,
        )

    token = credentials.credentials
    try:
        userResponse = getSupabaseAdminClient().auth.get_user(token)
    except Exception as exc:
        raise AppError(
            "The supplied bearer token is invalid.",
            code="AUTH_INVALID",
            status=401,
        ) from exc

    user = getattr(userResponse, "user", None)
    if user is None:
        raise AppError(
            "The supplied bearer token is invalid.",
            code="AUTH_INVALID",
            status=401,
        )

    authenticatedUser = {
        "email": getattr(user, "email", None),
        "token": token,
        "userId": str(getattr(user, "id")),
    }
    request.state.authenticatedUser = authenticatedUser
    return authenticatedUser


async def requireInternalSecret(
    internalApiSecret: Annotated[str | None, Header(alias="x-internal-api-secret")] = None,
) -> None:
    settings = getSettings()
    if internalApiSecret is None or not secrets.compare_digest(
        internalApiSecret,
        settings.internalApiSecretValue,
    ):
        raise AppError(
            "This route is restricted to internal callers.",
            code="INTERNAL_ONLY",
            status=403,
        )
