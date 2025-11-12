"""
Modelo de Software
"""
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from ..database import Base


class Software(Base):
    """Modelo de software instalado"""

    __tablename__ = "software"

    id = Column(Integer, primary_key=True, index=True)
    equipo_id = Column(Integer, ForeignKey("equipos.id", ondelete="CASCADE"), nullable=False, index=True)
    nombre = Column(String(100), nullable=False)
    version = Column(String(50))
    fabricante = Column(String(100))
    tipo = Column(String(50))
    licencia = Column(String(100))
    fecha_instalacion = Column(Date)
    fecha_expiracion_licencia = Column(Date)

    # Relación
    equipo = relationship("Equipo", back_populates="software")
