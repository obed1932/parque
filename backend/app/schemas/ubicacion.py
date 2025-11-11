"""
Schemas para Ubicaciones
"""
from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime


class UbicacionBase(BaseModel):
    """Schema base de ubicación"""
    nombre: str
    departamento: Optional[str] = None
    edificio: Optional[str] = None
    piso: Optional[str] = None
    descripcion: Optional[str] = None
    responsable: Optional[str] = None
    telefono: Optional[str] = None


class UbicacionCreate(UbicacionBase):
    """Schema para crear ubicación"""
    pass


class UbicacionUpdate(BaseModel):
    """Schema para actualizar ubicación"""
    nombre: Optional[str] = None
    departamento: Optional[str] = None
    edificio: Optional[str] = None
    piso: Optional[str] = None
    descripcion: Optional[str] = None
    responsable: Optional[str] = None
    telefono: Optional[str] = None


class UbicacionResponse(UbicacionBase):
    """Schema de respuesta de ubicación"""
    id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)
