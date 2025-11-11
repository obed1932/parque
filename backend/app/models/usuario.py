"""
Modelo de Usuario
"""
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from ..database import Base


class Usuario(Base):
    """Modelo de usuarios/empleados"""

    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    apellido = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, index=True)
    telefono = Column(String(20))
    cargo = Column(String(100))
    departamento = Column(String(100))
    activo = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # Relaciones
    equipos = relationship("Equipo", back_populates="usuario")
    historial_asignaciones = relationship("HistorialAsignacion", back_populates="usuario")

    @property
    def nombre_completo(self):
        """Retorna el nombre completo del usuario"""
        return f"{self.nombre} {self.apellido}"
