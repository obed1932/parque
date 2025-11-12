"""
Aplicación principal FastAPI
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .config import settings
from .database import engine, Base
from .routes import (
    equipos_router,
    usuarios_router,
    ubicaciones_router,
    hardware_router,
    mantenimientos_router,
    stats_router
)

# Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)

# Crear aplicación FastAPI
app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="API REST para gestión de parque informático de PCs",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Registrar rutas
app.include_router(equipos_router, prefix=settings.API_PREFIX)
app.include_router(usuarios_router, prefix=settings.API_PREFIX)
app.include_router(ubicaciones_router, prefix=settings.API_PREFIX)
app.include_router(hardware_router, prefix=settings.API_PREFIX)
app.include_router(mantenimientos_router, prefix=settings.API_PREFIX)
app.include_router(stats_router, prefix=settings.API_PREFIX)


@app.get("/")
def root():
    """Endpoint raíz"""
    return {
        "message": "API de Sistema de Gestión de Parque Informático",
        "version": settings.APP_VERSION,
        "docs": "/docs",
        "redoc": "/redoc"
    }


@app.get("/health")
def health_check():
    """Health check"""
    return {"status": "ok"}
