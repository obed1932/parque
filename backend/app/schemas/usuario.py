"""
Schemas para Usuarios
"""
from pydantic import BaseModel, EmailStr, ConfigDict
from typing import Optional
from datetime import datetime


class UsuarioBase(BaseModel):
    """Schema base de usuario"""
    nombre: str
    apellido: str
    email: Optional[EmailStr] = None
    telefono: Optional[str] = None
    cargo: Optional[str] = None
    departamento: Optional[str] = None
    activo: bool = True


class UsuarioCreate(UsuarioBase):
    """Schema para crear usuario"""
    pass


class UsuarioUpdate(BaseModel):
    """Schema para actualizar usuario"""
    nombre: Optional[str] = None
    apellido: Optional[str] = None
    email: Optional[EmailStr] = None
    telefono: Optional[str] = None
    cargo: Optional[str] = None
    departamento: Optional[str] = None
    activo: Optional[bool] = None


class UsuarioResponse(UsuarioBase):
    """Schema de respuesta de usuario"""
    id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)
