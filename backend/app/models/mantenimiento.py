"""
Modelo de Mantenimiento
"""
from sqlalchemy import Column, Integer, String, Text, Date, Numeric, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from ..database import Base


class Mantenimiento(Base):
    """Modelo de mantenimientos"""

    __tablename__ = "mantenimientos"

    id = Column(Integer, primary_key=True, index=True)
    equipo_id = Column(Integer, ForeignKey("equipos.id", ondelete="CASCADE"), nullable=False, index=True)
    tipo_mantenimiento = Column(String(50))
    descripcion = Column(Text)
    fecha_mantenimiento = Column(Date, nullable=False, index=True)
    tecnico_responsable = Column(String(100))
    costo = Column(Numeric(10, 2))
    tiempo_inactividad_horas = Column(Integer)
    proximo_mantenimiento = Column(Date)
    observaciones = Column(Text)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Relación
    equipo = relationship("Equipo", back_populates="mantenimientos")
