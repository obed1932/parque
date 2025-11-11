"""
Modelo de Equipo
"""
from sqlalchemy import Column, Integer, String, Text, Date, Numeric, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from ..database import Base


class Equipo(Base):
    """Modelo de equipos/PCs"""

    __tablename__ = "equipos"

    id = Column(Integer, primary_key=True, index=True)
    codigo_inventario = Column(String(50), unique=True, nullable=False, index=True)
    nombre_equipo = Column(String(100))
    tipo_equipo = Column(String(50), default="Desktop")
    marca = Column(String(50))
    modelo = Column(String(100))
    numero_serie = Column(String(100), unique=True)
    fecha_adquisicion = Column(Date)
    fecha_garantia = Column(Date)
    proveedor = Column(String(100))
    precio_compra = Column(Numeric(10, 2))
    estado = Column(String(50), default="Operativo", index=True)
    sistema_operativo = Column(String(100))
    version_so = Column(String(50))
    licencia_so = Column(String(100))
    observaciones = Column(Text)
    ubicacion_id = Column(Integer, ForeignKey("ubicaciones.id", ondelete="SET NULL"))
    usuario_id = Column(Integer, ForeignKey("usuarios.id", ondelete="SET NULL"))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # Relaciones
    ubicacion = relationship("Ubicacion", back_populates="equipos")
    usuario = relationship("Usuario", back_populates="equipos")
    procesadores = relationship("Procesador", back_populates="equipo", cascade="all, delete-orphan")
    memorias_ram = relationship("MemoriaRAM", back_populates="equipo", cascade="all, delete-orphan")
    almacenamientos = relationship("Almacenamiento", back_populates="equipo", cascade="all, delete-orphan")
    tarjetas_graficas = relationship("TarjetaGrafica", back_populates="equipo", cascade="all, delete-orphan")
    placas_base = relationship("PlacaBase", back_populates="equipo", cascade="all, delete-orphan")
    fuentes_alimentacion = relationship("FuenteAlimentacion", back_populates="equipo", cascade="all, delete-orphan")
    componentes_red = relationship("ComponenteRed", back_populates="equipo", cascade="all, delete-orphan")
    perifericos = relationship("Periferico", back_populates="equipo")
    mantenimientos = relationship("Mantenimiento", back_populates="equipo", cascade="all, delete-orphan")
    software = relationship("Software", back_populates="equipo", cascade="all, delete-orphan")
    historial_asignaciones = relationship("HistorialAsignacion", back_populates="equipo", cascade="all, delete-orphan")
