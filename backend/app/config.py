"""
Configuración de la aplicación
"""
from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    """Configuración de la aplicación"""

    # Aplicación
    APP_NAME: str = "Sistema de Gestión de Parque Informático"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = True

    # Base de datos
    DATABASE_URL: str = "sqlite:///./parque_informatico.db"

    # CORS
    CORS_ORIGINS: list = [
        "http://localhost:5173",
        "http://localhost:3000",
        "http://127.0.0.1:5173",
        "http://127.0.0.1:3000",
    ]

    # API
    API_PREFIX: str = "/api"

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
