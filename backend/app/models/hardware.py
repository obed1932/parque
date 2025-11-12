"""
Modelos de componentes de hardware
"""
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from ..database import Base


class Procesador(Base):
    """Modelo de procesadores"""

    __tablename__ = "procesadores"

    id = Column(Integer, primary_key=True, index=True)
    equipo_id = Column(Integer, ForeignKey("equipos.id", ondelete="CASCADE"), nullable=False)
    marca = Column(String(50))
    modelo = Column(String(100))
    nucleos = Column(Integer)
    hilos = Column(Integer)
    frecuencia_base = Column(String(20))
    frecuencia_turbo = Column(String(20))
    socket = Column(String(50))
    cache = Column(String(50))

    # Relación
    equipo = relationship("Equipo", back_populates="procesadores")


class MemoriaRAM(Base):
    """Modelo de memoria RAM"""

    __tablename__ = "memoria_ram"

    id = Column(Integer, primary_key=True, index=True)
    equipo_id = Column(Integer, ForeignKey("equipos.id", ondelete="CASCADE"), nullable=False)
    tipo = Column(String(20))
    capacidad_gb = Column(Integer)
    velocidad_mhz = Column(Integer)
    marca = Column(String(50))
    modelo = Column(String(100))
    slots_ocupados = Column(Integer)
    slots_totales = Column(Integer)

    # Relación
    equipo = relationship("Equipo", back_populates="memorias_ram")


class Almacenamiento(Base):
    """Modelo de dispositivos de almacenamiento"""

    __tablename__ = "almacenamiento"

    id = Column(Integer, primary_key=True, index=True)
    equipo_id = Column(Integer, ForeignKey("equipos.id", ondelete="CASCADE"), nullable=False)
    tipo = Column(String(20))
    capacidad_gb = Column(Integer)
    marca = Column(String(50))
    modelo = Column(String(100))
    numero_serie = Column(String(100))
    interfaz = Column(String(20))
    es_principal = Column(Boolean, default=False)

    # Relación
    equipo = relationship("Equipo", back_populates="almacenamientos")


class TarjetaGrafica(Base):
    """Modelo de tarjetas gráficas"""

    __tablename__ = "tarjetas_graficas"

    id = Column(Integer, primary_key=True, index=True)
    equipo_id = Column(Integer, ForeignKey("equipos.id", ondelete="CASCADE"), nullable=False)
    tipo = Column(String(20))
    marca = Column(String(50))
    modelo = Column(String(100))
    memoria_gb = Column(Integer)
    tipo_memoria = Column(String(20))

    # Relación
    equipo = relationship("Equipo", back_populates="tarjetas_graficas")


class PlacaBase(Base):
    """Modelo de placas base"""

    __tablename__ = "placas_base"

    id = Column(Integer, primary_key=True, index=True)
    equipo_id = Column(Integer, ForeignKey("equipos.id", ondelete="CASCADE"), nullable=False)
    marca = Column(String(50))
    modelo = Column(String(100))
    chipset = Column(String(50))
    socket = Column(String(50))
    factor_forma = Column(String(20))

    # Relación
    equipo = relationship("Equipo", back_populates="placas_base")


class FuenteAlimentacion(Base):
    """Modelo de fuentes de alimentación"""

    __tablename__ = "fuentes_alimentacion"

    id = Column(Integer, primary_key=True, index=True)
    equipo_id = Column(Integer, ForeignKey("equipos.id", ondelete="CASCADE"), nullable=False)
    marca = Column(String(50))
    modelo = Column(String(100))
    potencia_watts = Column(Integer)
    certificacion = Column(String(50))

    # Relación
    equipo = relationship("Equipo", back_populates="fuentes_alimentacion")


class ComponenteRed(Base):
    """Modelo de componentes de red"""

    __tablename__ = "componentes_red"

    id = Column(Integer, primary_key=True, index=True)
    equipo_id = Column(Integer, ForeignKey("equipos.id", ondelete="CASCADE"), nullable=False)
    tipo = Column(String(50))
    marca = Column(String(50))
    modelo = Column(String(100))
    velocidad = Column(String(50))
    mac_address = Column(String(17))

    # Relación
    equipo = relationship("Equipo", back_populates="componentes_red")


class Periferico(Base):
    """Modelo de periféricos"""

    __tablename__ = "perifericos"

    id = Column(Integer, primary_key=True, index=True)
    equipo_id = Column(Integer, ForeignKey("equipos.id", ondelete="SET NULL"))
    tipo = Column(String(50))
    marca = Column(String(50))
    modelo = Column(String(100))
    numero_serie = Column(String(100))
    especificaciones = Column(String)
    estado = Column(String(50), default="Operativo")

    # Relación
    equipo = relationship("Equipo", back_populates="perifericos")
