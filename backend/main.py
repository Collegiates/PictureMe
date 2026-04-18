from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum

from backend.config import getSettings
from backend.errors import register_error_handlers
from backend.logging import configure_logging, log_requests
from backend.routes.health import router as health_router
from backend.routes.runtime_config import router as config_router
from backend.routes.verification import router as verification_router

settings = getSettings()
configure_logging(settings)

app = FastAPI(
    title="PictureMe API",
    version="0.1.0",
    docs_url="/api/docs" if settings.is_development else None,
    redoc_url="/api/redoc" if settings.is_development else None,
)

# Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.frontend_origin, settings.app_origin],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.middleware("http")(log_requests)

# Errors
register_error_handlers(app)

# Routes
app.include_router(health_router)
app.include_router(config_router)
app.include_router(verification_router)

# ✅ Vercel uses THIS
handler = Mangum(app)

# ✅ Local dev uses THIS
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "backend.main:app",
        host="0.0.0.0",
        port=settings.port,
        reload=settings.is_development,
    )