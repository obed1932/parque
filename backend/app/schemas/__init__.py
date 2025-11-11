"""
Schemas Pydantic para validación
"""
from .ubicacion import UbicacionCreate, UbicacionUpdate, UbicacionResponse
from .usuario import UsuarioCreate, UsuarioUpdate, UsuarioResponse
from .equipo import EquipoCreate, EquipoUpdate, EquipoResponse, EquipoDetailResponse
from .hardware import (
    ProcesadorCreate,
    MemoriaRAMCreate,
    AlmacenamientoCreate,
    TarjetaGraficaCreate,
    PlacaBaseCreate,
    FuenteAlimentacionCreate,
    ComponenteRedCreate,
    PerifericoCreate
)
from .mantenimiento import MantenimientoCreate, MantenimientoResponse

__all__ = [
    "UbicacionCreate",
    "UbicacionUpdate",
    "UbicacionResponse",
    "UsuarioCreate",
    "UsuarioUpdate",
    "UsuarioResponse",
    "EquipoCreate",
    "EquipoUpdate",
    "EquipoResponse",
    "EquipoDetailResponse",
    "ProcesadorCreate",
    "MemoriaRAMCreate",
    "AlmacenamientoCreate",
    "TarjetaGraficaCreate",
    "PlacaBaseCreate",
    "FuenteAlimentacionCreate",
    "ComponenteRedCreate",
    "PerifericoCreate",
    "MantenimientoCreate",
    "MantenimientoResponse",
]
