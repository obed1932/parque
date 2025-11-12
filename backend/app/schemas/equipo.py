"""
Schemas para Equipos
"""
from pydantic import BaseModel, ConfigDict
from typing import Optional, List
from datetime import date, datetime
from decimal import Decimal


class EquipoBase(BaseModel):
    """Schema base de equipo"""
    codigo_inventario: str
    nombre_equipo: Optional[str] = None
    tipo_equipo: str = "Desktop"
    marca: Optional[str] = None
    modelo: Optional[str] = None
    numero_serie: Optional[str] = None
    fecha_adquisicion: Optional[date] = None
    fecha_garantia: Optional[date] = None
    proveedor: Optional[str] = None
    precio_compra: Optional[Decimal] = None
    estado: str = "Operativo"
    sistema_operativo: Optional[str] = None
    version_so: Optional[str] = None
    licencia_so: Optional[str] = None
    observaciones: Optional[str] = None
    ubicacion_id: Optional[int] = None
    usuario_id: Optional[int] = None


class EquipoCreate(EquipoBase):
    """Schema para crear equipo"""
    pass


class EquipoUpdate(BaseModel):
    """Schema para actualizar equipo"""
    codigo_inventario: Optional[str] = None
    nombre_equipo: Optional[str] = None
    tipo_equipo: Optional[str] = None
    marca: Optional[str] = None
    modelo: Optional[str] = None
    numero_serie: Optional[str] = None
    fecha_adquisicion: Optional[date] = None
    fecha_garantia: Optional[date] = None
    proveedor: Optional[str] = None
    precio_compra: Optional[Decimal] = None
    estado: Optional[str] = None
    sistema_operativo: Optional[str] = None
    version_so: Optional[str] = None
    licencia_so: Optional[str] = None
    observaciones: Optional[str] = None
    ubicacion_id: Optional[int] = None
    usuario_id: Optional[int] = None


class EquipoResponse(EquipoBase):
    """Schema de respuesta de equipo"""
    id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


# Para respuestas con información detallada
class ProcesadorResponse(BaseModel):
    id: int
    marca: Optional[str] = None
    modelo: Optional[str] = None
    nucleos: Optional[int] = None
    hilos: Optional[int] = None
    frecuencia_base: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)


class MemoriaRAMResponse(BaseModel):
    id: int
    tipo: Optional[str] = None
    capacidad_gb: Optional[int] = None
    velocidad_mhz: Optional[int] = None
    marca: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)


class AlmacenamientoResponse(BaseModel):
    id: int
    tipo: Optional[str] = None
    capacidad_gb: Optional[int] = None
    marca: Optional[str] = None
    modelo: Optional[str] = None
    es_principal: bool = False

    model_config = ConfigDict(from_attributes=True)


class TarjetaGraficaResponse(BaseModel):
    id: int
    tipo: Optional[str] = None
    marca: Optional[str] = None
    modelo: Optional[str] = None
    memoria_gb: Optional[int] = None

    model_config = ConfigDict(from_attributes=True)


class EquipoDetailResponse(EquipoResponse):
    """Schema de respuesta detallada de equipo con hardware"""
    procesadores: List[ProcesadorResponse] = []
    memorias_ram: List[MemoriaRAMResponse] = []
    almacenamientos: List[AlmacenamientoResponse] = []
    tarjetas_graficas: List[TarjetaGraficaResponse] = []

    model_config = ConfigDict(from_attributes=True)
