"""
Inicialización de la base de datos
"""
from .connection import engine, Base
from ..models import (
    Ubicacion,
    Usuario,
    Equipo,
    Procesador,
    MemoriaRAM,
    Almacenamiento,
    TarjetaGrafica,
    PlacaBase,
    FuenteAlimentacion,
    ComponenteRed,
    Periferico,
    Mantenimiento,
    Software,
    HistorialAsignacion
)


def init_database():
    """Crear todas las tablas en la base de datos"""
    Base.metadata.create_all(bind=engine)
    print("Base de datos inicializada correctamente")


def drop_database():
    """Eliminar todas las tablas de la base de datos"""
    Base.metadata.drop_all(bind=engine)
    print("Base de datos eliminada")


if __name__ == "__main__":
    init_database()
