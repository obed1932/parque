"""
Schemas para Mantenimientos
"""
from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import date, datetime
from decimal import Decimal


class MantenimientoBase(BaseModel):
    """Schema base de mantenimiento"""
    equipo_id: int
    tipo_mantenimiento: Optional[str] = None
    descripcion: Optional[str] = None
    fecha_mantenimiento: date
    tecnico_responsable: Optional[str] = None
    costo: Optional[Decimal] = None
    tiempo_inactividad_horas: Optional[int] = None
    proximo_mantenimiento: Optional[date] = None
    observaciones: Optional[str] = None


class MantenimientoCreate(MantenimientoBase):
    """Schema para crear mantenimiento"""
    pass


class MantenimientoResponse(MantenimientoBase):
    """Schema de respuesta de mantenimiento"""
    id: int
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)
