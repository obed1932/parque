"""
Modelos de la base de datos
"""
from .ubicacion import Ubicacion
from .usuario import Usuario
from .equipo import Equipo
from .hardware import (
    Procesador,
    MemoriaRAM,
    Almacenamiento,
    TarjetaGrafica,
    PlacaBase,
    FuenteAlimentacion,
    ComponenteRed,
    Periferico
)
from .mantenimiento import Mantenimiento
from .software import Software
from .historial import HistorialAsignacion

__all__ = [
    "Ubicacion",
    "Usuario",
    "Equipo",
    "Procesador",
    "MemoriaRAM",
    "Almacenamiento",
    "TarjetaGrafica",
    "PlacaBase",
    "FuenteAlimentacion",
    "ComponenteRed",
    "Periferico",
    "Mantenimiento",
    "Software",
    "HistorialAsignacion"
]
