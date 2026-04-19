"""Backend configuration for FastAPI and Vercel runtime usage."""

from functools import lru_cache
from pathlib import Path
from typing import Literal

from pydantic import AliasChoices, Field, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Typed settings loaded from the backend environment file."""

    model_config = SettingsConfigDict(
        env_file=str(Path(__file__).resolve().parent / ".env"),
        env_file_encoding="utf-8",
        extra="ignore",
    )

    appEnv: Literal["development", "test", "production"] = Field(
        default="development",
        validation_alias=AliasChoices("APP_ENV", "NODE_ENV"),
    )
    appOrigin: str = Field(default="http://localhost:3000", alias="APP_ORIGIN")
    faceProfileBucket: str = Field(
        default="face-profile-images",
        alias="SUPABASE_FACE_PROFILE_BUCKET",
    )
    frontendOrigin: str = Field(default="http://localhost:3000", alias="FRONTEND_ORIGIN")
    googleOAuthEnabled: bool = Field(default=True, alias="GOOGLE_OAUTH_ENABLED")
    internalApiSecret: SecretStr = Field(alias="INTERNAL_API_SECRET")
    logLevel: Literal["debug", "info", "warning", "error", "critical"] = Field(
        default="info",
        alias="LOG_LEVEL",
    )
    port: int = Field(default=8000, alias="PORT")
    supabaseSecretKey: SecretStr = Field(
        validation_alias=AliasChoices("SUPABASE_SERVICE_ROLE_KEY", "SUPABASE_SECRET_KEY"),
    )
    supabaseUrl: str = Field(alias="SUPABASE_URL")

    @property
    def internalApiSecretValue(self) -> str:
        return self.internalApiSecret.get_secret_value()

    @property
    def isDevelopment(self) -> bool:
        return self.appEnv == "development"

    @property
    def publicConfig(self) -> dict[str, object]:
        return {
            "apiBaseUrl": self.appOrigin,
            "appOrigin": self.appOrigin,
            "frontendOrigin": self.frontendOrigin,
            "googleOAuthEnabled": self.googleOAuthEnabled,
        }

    @property
    def supabaseSecretKeyValue(self) -> str:
        return self.supabaseSecretKey.get_secret_value()


@lru_cache
def getSettings() -> Settings:
    return Settings()
