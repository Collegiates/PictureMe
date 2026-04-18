"""Minimal verification routes for auth and internal backend protections."""

from fastapi import APIRouter, Depends, Query

from backend.dependencies.auth import AuthenticatedUser, require_authenticated_user
from backend.dependencies.internal import require_internal_secret

router = APIRouter(tags=["verification"])


@router.get("/api/test/authenticated-user")
async def authenticated_user_check(
    current_user: AuthenticatedUser = Depends(require_authenticated_user),
    version: int | None = Query(default=None, ge=1),
):
    """Return the authenticated user context after Supabase token verification."""
    payload = current_user.to_response()
    if version is not None:
        payload["version"] = version
    return payload


@router.get("/api/internal/verify", dependencies=[Depends(require_internal_secret)])
async def internal_verify():
    """Return a simple payload proving the internal secret dependency passed."""
    return {"status": "ok", "scope": "internal"}
