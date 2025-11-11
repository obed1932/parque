"""
Rutas para Mantenimientos
"""
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from ..database import get_db
from ..models import Mantenimiento, Equipo
from ..schemas import MantenimientoCreate, MantenimientoResponse

router = APIRouter(prefix="/mantenimientos", tags=["Mantenimientos"])


@router.get("/", response_model=List[MantenimientoResponse])
def listar_mantenimientos(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    """Listar todos los mantenimientos"""
    mantenimientos = db.query(Mantenimiento).offset(skip).limit(limit).all()
    return mantenimientos


@router.get("/equipo/{equipo_id}", response_model=List[MantenimientoResponse])
def listar_mantenimientos_equipo(
    equipo_id: int,
    db: Session = Depends(get_db)
):
    """Listar mantenimientos de un equipo específico"""
    equipo = db.query(Equipo).filter(Equipo.id == equipo_id).first()
    if not equipo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Equipo con ID {equipo_id} no encontrado"
        )

    mantenimientos = db.query(Mantenimiento).filter(
        Mantenimiento.equipo_id == equipo_id
    ).all()
    return mantenimientos


@router.post("/", response_model=MantenimientoResponse, status_code=status.HTTP_201_CREATED)
def crear_mantenimiento(
    mantenimiento: MantenimientoCreate,
    db: Session = Depends(get_db)
):
    """Registrar un nuevo mantenimiento"""
    # Verificar que el equipo existe
    equipo = db.query(Equipo).filter(Equipo.id == mantenimiento.equipo_id).first()
    if not equipo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Equipo con ID {mantenimiento.equipo_id} no encontrado"
        )

    db_mantenimiento = Mantenimiento(**mantenimiento.model_dump())
    db.add(db_mantenimiento)
    db.commit()
    db.refresh(db_mantenimiento)
    return db_mantenimiento


@router.get("/{mantenimiento_id}", response_model=MantenimientoResponse)
def obtener_mantenimiento(mantenimiento_id: int, db: Session = Depends(get_db)):
    """Obtener un mantenimiento por ID"""
    mantenimiento = db.query(Mantenimiento).filter(
        Mantenimiento.id == mantenimiento_id
    ).first()
    if not mantenimiento:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Mantenimiento con ID {mantenimiento_id} no encontrado"
        )
    return mantenimiento
