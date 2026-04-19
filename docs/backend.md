# Backend

## Purpose

The backend in [backend](/Users/tervin23/Documents/AG/PictureMe/backend) remains a FastAPI service. It owns API routing, Supabase JWT validation, browser-safe runtime configuration, and the orchestration layer for account, event, gallery, upload, matching, and cleanup workflows.

## Simplified Structure

- [backend/app.py](/Users/tervin23/Documents/AG/PictureMe/backend/app.py): Single FastAPI application entrypoint for local runs and Vercel.
- [backend/config.py](/Users/tervin23/Documents/AG/PictureMe/backend/config.py): Typed environment loading and browser-safe runtime config.
- [backend/deps.py](/Users/tervin23/Documents/AG/PictureMe/backend/deps.py): Shared auth, internal-secret, and Supabase admin helpers.
- [backend/errors.py](/Users/tervin23/Documents/AG/PictureMe/backend/errors.py): Stable API error contract and exception handlers.
- [backend/schemas.py](/Users/tervin23/Documents/AG/PictureMe/backend/schemas.py): Shared Pydantic response models.
- [backend/routers](/Users/tervin23/Documents/AG/PictureMe/backend/routers): Route groups split into `system.py` and `account.py`.
- [backend/services](/Users/tervin23/Documents/AG/PictureMe/backend/services): Business logic grouped by feature, starting with `account.py`.
- [api/app.py](/Users/tervin23/Documents/AG/PictureMe/api/app.py): Vercel Python function entrypoint.

## Routing Logic

- `backend/app.py` creates the FastAPI app once and mounts route groups.
- `backend/routers/system.py` contains health, runtime-config, and validation routes.
- `backend/routers/account.py` contains Stage 2 account and face-profile routes.
- Feature logic stays out of route files and moves into `backend/services/*`, which keeps future stages easier to extend.

## Extensibility Notes

- New backend stages can add one router file and one matching service file per domain area instead of creating new dependency or middleware layers.
- Secrets remain backend-only.
- The face-profile upload service already contains an explicit comment where AWS Rekognition API keys and indexing logic will be required later.
