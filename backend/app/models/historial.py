"""
Modelo de Historial de Asignaciones
"""
from sqlalchemy import Column, Integer, String, Text, Date, ForeignKey
from sqlalchemy.orm import relationship
from ..database import Base


class HistorialAsignacion(Base):
    """Modelo de historial de asignaciones"""

    __tablename__ = "historial_asignaciones"

    id = Column(Integer, primary_key=True, index=True)
    equipo_id = Column(Integer, ForeignKey("equipos.id", ondelete="CASCADE"), nullable=False, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id", ondelete="SET NULL"))
    ubicacion_id = Column(Integer, ForeignKey("ubicaciones.id", ondelete="SET NULL"))
    fecha_asignacion = Column(Date, nullable=False)
    fecha_devolucion = Column(Date)
    motivo = Column(Text)
    estado = Column(String(50))

    # Relaciones
    equipo = relationship("Equipo", back_populates="historial_asignaciones")
    usuario = relationship("Usuario", back_populates="historial_asignaciones")
    ubicacion = relationship("Ubicacion", back_populates="historial_asignaciones")
