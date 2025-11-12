"""
Schemas para componentes de Hardware
"""
from pydantic import BaseModel
from typing import Optional


class ProcesadorCreate(BaseModel):
    """Schema para crear procesador"""
    equipo_id: int
    marca: Optional[str] = None
    modelo: Optional[str] = None
    nucleos: Optional[int] = None
    hilos: Optional[int] = None
    frecuencia_base: Optional[str] = None
    frecuencia_turbo: Optional[str] = None
    socket: Optional[str] = None
    cache: Optional[str] = None


class MemoriaRAMCreate(BaseModel):
    """Schema para crear memoria RAM"""
    equipo_id: int
    tipo: Optional[str] = None
    capacidad_gb: Optional[int] = None
    velocidad_mhz: Optional[int] = None
    marca: Optional[str] = None
    modelo: Optional[str] = None
    slots_ocupados: Optional[int] = None
    slots_totales: Optional[int] = None


class AlmacenamientoCreate(BaseModel):
    """Schema para crear almacenamiento"""
    equipo_id: int
    tipo: Optional[str] = None
    capacidad_gb: Optional[int] = None
    marca: Optional[str] = None
    modelo: Optional[str] = None
    numero_serie: Optional[str] = None
    interfaz: Optional[str] = None
    es_principal: bool = False


class TarjetaGraficaCreate(BaseModel):
    """Schema para crear tarjeta gráfica"""
    equipo_id: int
    tipo: Optional[str] = None
    marca: Optional[str] = None
    modelo: Optional[str] = None
    memoria_gb: Optional[int] = None
    tipo_memoria: Optional[str] = None


class PlacaBaseCreate(BaseModel):
    """Schema para crear placa base"""
    equipo_id: int
    marca: Optional[str] = None
    modelo: Optional[str] = None
    chipset: Optional[str] = None
    socket: Optional[str] = None
    factor_forma: Optional[str] = None


class FuenteAlimentacionCreate(BaseModel):
    """Schema para crear fuente de alimentación"""
    equipo_id: int
    marca: Optional[str] = None
    modelo: Optional[str] = None
    potencia_watts: Optional[int] = None
    certificacion: Optional[str] = None


class ComponenteRedCreate(BaseModel):
    """Schema para crear componente de red"""
    equipo_id: int
    tipo: Optional[str] = None
    marca: Optional[str] = None
    modelo: Optional[str] = None
    velocidad: Optional[str] = None
    mac_address: Optional[str] = None


class PerifericoCreate(BaseModel):
    """Schema para crear periférico"""
    equipo_id: Optional[int] = None
    tipo: Optional[str] = None
    marca: Optional[str] = None
    modelo: Optional[str] = None
    numero_serie: Optional[str] = None
    especificaciones: Optional[str] = None
    estado: str = "Operativo"
