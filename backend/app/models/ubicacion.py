"""
Modelo de Ubicación
"""
from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from ..database import Base


class Ubicacion(Base):
    """Modelo de ubicaciones/servicios"""

    __tablename__ = "ubicaciones"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    departamento = Column(String(100))
    edificio = Column(String(50))
    piso = Column(String(20))
    descripcion = Column(Text)
    responsable = Column(String(100))
    telefono = Column(String(20))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # Relaciones
    equipos = relationship("Equipo", back_populates="ubicacion")
    historial_asignaciones = relationship("HistorialAsignacion", back_populates="ubicacion")
