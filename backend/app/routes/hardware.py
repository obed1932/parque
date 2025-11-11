"""
Rutas para Hardware
"""
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import (
    Procesador,
    MemoriaRAM,
    Almacenamiento,
    TarjetaGrafica,
    PlacaBase,
    FuenteAlimentacion,
    ComponenteRed,
    Periferico,
    Equipo
)
from ..schemas import (
    ProcesadorCreate,
    MemoriaRAMCreate,
    AlmacenamientoCreate,
    TarjetaGraficaCreate,
    PlacaBaseCreate,
    FuenteAlimentacionCreate,
    ComponenteRedCreate,
    PerifericoCreate
)

router = APIRouter(prefix="/hardware", tags=["Hardware"])


def verificar_equipo_existe(equipo_id: int, db: Session):
    """Verificar que el equipo existe"""
    equipo = db.query(Equipo).filter(Equipo.id == equipo_id).first()
    if not equipo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Equipo con ID {equipo_id} no encontrado"
        )
    return equipo


@router.post("/procesador", status_code=status.HTTP_201_CREATED)
def agregar_procesador(procesador: ProcesadorCreate, db: Session = Depends(get_db)):
    """Agregar procesador a un equipo"""
    verificar_equipo_existe(procesador.equipo_id, db)

    db_procesador = Procesador(**procesador.model_dump())
    db.add(db_procesador)
    db.commit()
    db.refresh(db_procesador)
    return db_procesador


@router.post("/ram", status_code=status.HTTP_201_CREATED)
def agregar_ram(ram: MemoriaRAMCreate, db: Session = Depends(get_db)):
    """Agregar memoria RAM a un equipo"""
    verificar_equipo_existe(ram.equipo_id, db)

    db_ram = MemoriaRAM(**ram.model_dump())
    db.add(db_ram)
    db.commit()
    db.refresh(db_ram)
    return db_ram


@router.post("/almacenamiento", status_code=status.HTTP_201_CREATED)
def agregar_almacenamiento(almacenamiento: AlmacenamientoCreate, db: Session = Depends(get_db)):
    """Agregar almacenamiento a un equipo"""
    verificar_equipo_existe(almacenamiento.equipo_id, db)

    db_almacenamiento = Almacenamiento(**almacenamiento.model_dump())
    db.add(db_almacenamiento)
    db.commit()
    db.refresh(db_almacenamiento)
    return db_almacenamiento


@router.post("/gpu", status_code=status.HTTP_201_CREATED)
def agregar_gpu(gpu: TarjetaGraficaCreate, db: Session = Depends(get_db)):
    """Agregar tarjeta gráfica a un equipo"""
    verificar_equipo_existe(gpu.equipo_id, db)

    db_gpu = TarjetaGrafica(**gpu.model_dump())
    db.add(db_gpu)
    db.commit()
    db.refresh(db_gpu)
    return db_gpu


@router.post("/placa-base", status_code=status.HTTP_201_CREATED)
def agregar_placa_base(placa: PlacaBaseCreate, db: Session = Depends(get_db)):
    """Agregar placa base a un equipo"""
    verificar_equipo_existe(placa.equipo_id, db)

    db_placa = PlacaBase(**placa.model_dump())
    db.add(db_placa)
    db.commit()
    db.refresh(db_placa)
    return db_placa


@router.post("/fuente", status_code=status.HTTP_201_CREATED)
def agregar_fuente(fuente: FuenteAlimentacionCreate, db: Session = Depends(get_db)):
    """Agregar fuente de alimentación a un equipo"""
    verificar_equipo_existe(fuente.equipo_id, db)

    db_fuente = FuenteAlimentacion(**fuente.model_dump())
    db.add(db_fuente)
    db.commit()
    db.refresh(db_fuente)
    return db_fuente


@router.post("/red", status_code=status.HTTP_201_CREATED)
def agregar_componente_red(componente: ComponenteRedCreate, db: Session = Depends(get_db)):
    """Agregar componente de red a un equipo"""
    verificar_equipo_existe(componente.equipo_id, db)

    db_componente = ComponenteRed(**componente.model_dump())
    db.add(db_componente)
    db.commit()
    db.refresh(db_componente)
    return db_componente


@router.post("/periferico", status_code=status.HTTP_201_CREATED)
def agregar_periferico(periferico: PerifericoCreate, db: Session = Depends(get_db)):
    """Agregar periférico"""
    if periferico.equipo_id:
        verificar_equipo_existe(periferico.equipo_id, db)

    db_periferico = Periferico(**periferico.model_dump())
    db.add(db_periferico)
    db.commit()
    db.refresh(db_periferico)
    return db_periferico
