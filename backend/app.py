"""FastAPI application entrypoint for local runs and Vercel."""

import uvicorn

from backend.config import getSettings
from backend.routers.account import router as accountRouter
from backend.routers.system import createApp, router as systemRouter

app = createApp()
app.include_router(systemRouter)
app.include_router(accountRouter)


def _run() -> None:
    settings = getSettings()
    uvicorn.run(
        "backend.app:app",
        host="0.0.0.0",
        port=settings.port,
        reload=settings.isDevelopment,
    )


if __name__ == "__main__":
    _run()
