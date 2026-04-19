"""Account and face-profile API routes."""

from fastapi import APIRouter, Depends, File, Form, UploadFile

from backend.deps import requireAuthenticatedUser
from backend.schemas import AccountResponse, FaceProfileStatus
from backend.services.account import (
    deleteFaceProfile,
    getAccount,
    replaceFaceProfile,
    updateAccountProfile,
)

router = APIRouter(tags=["account"])


@router.get("/api/account", response_model=AccountResponse)
async def getAccountRoute(
    authenticatedUser: dict[str, object] = Depends(requireAuthenticatedUser),
) -> AccountResponse:
    return getAccount(str(authenticatedUser["userId"]))


@router.patch("/api/account/profile", response_model=AccountResponse)
async def patchAccountProfileRoute(
    name: str = Form(...),
    avatar: UploadFile | None = File(default=None),
    authenticatedUser: dict[str, object] = Depends(requireAuthenticatedUser),
) -> AccountResponse:
    return updateAccountProfile(
        userId=str(authenticatedUser["userId"]),
        name=name,
        avatar=avatar,
    )


@router.post("/api/account/face-profile", response_model=FaceProfileStatus)
async def postFaceProfileRoute(
    face: UploadFile | None = File(default=None),
    authenticatedUser: dict[str, object] = Depends(requireAuthenticatedUser),
) -> FaceProfileStatus:
    files = [face] if face is not None else []
    return await replaceFaceProfile(
        userId=str(authenticatedUser["userId"]),
        files=files,
    )


@router.delete("/api/account/face-profile", response_model=FaceProfileStatus)
async def deleteFaceProfileRoute(
    authenticatedUser: dict[str, object] = Depends(requireAuthenticatedUser),
) -> FaceProfileStatus:
    return await deleteFaceProfile(str(authenticatedUser["userId"]))
