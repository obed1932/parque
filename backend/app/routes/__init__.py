"""
Rutas de la API
"""
from .equipos import router as equipos_router
from .usuarios import router as usuarios_router
from .ubicaciones import router as ubicaciones_router
from .hardware import router as hardware_router
from .mantenimientos import router as mantenimientos_router
from .stats import router as stats_router

__all__ = [
    "equipos_router",
    "usuarios_router",
    "ubicaciones_router",
    "hardware_router",
    "mantenimientos_router",
    "stats_router",
]
