"""
Rutas para Ubicaciones
"""
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from ..database import get_db
from ..models import Ubicacion
from ..schemas import UbicacionCreate, UbicacionUpdate, UbicacionResponse

router = APIRouter(prefix="/ubicaciones", tags=["Ubicaciones"])


@router.get("/", response_model=List[UbicacionResponse])
def listar_ubicaciones(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    """Listar todas las ubicaciones"""
    ubicaciones = db.query(Ubicacion).offset(skip).limit(limit).all()
    return ubicaciones


@router.get("/{ubicacion_id}", response_model=UbicacionResponse)
def obtener_ubicacion(ubicacion_id: int, db: Session = Depends(get_db)):
    """Obtener una ubicación por ID"""
    ubicacion = db.query(Ubicacion).filter(Ubicacion.id == ubicacion_id).first()
    if not ubicacion:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Ubicación con ID {ubicacion_id} no encontrada"
        )
    return ubicacion


@router.post("/", response_model=UbicacionResponse, status_code=status.HTTP_201_CREATED)
def crear_ubicacion(ubicacion: UbicacionCreate, db: Session = Depends(get_db)):
    """Crear una nueva ubicación"""
    db_ubicacion = Ubicacion(**ubicacion.model_dump())
    db.add(db_ubicacion)
    db.commit()
    db.refresh(db_ubicacion)
    return db_ubicacion


@router.put("/{ubicacion_id}", response_model=UbicacionResponse)
def actualizar_ubicacion(
    ubicacion_id: int,
    ubicacion: UbicacionUpdate,
    db: Session = Depends(get_db)
):
    """Actualizar una ubicación existente"""
    db_ubicacion = db.query(Ubicacion).filter(Ubicacion.id == ubicacion_id).first()
    if not db_ubicacion:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Ubicación con ID {ubicacion_id} no encontrada"
        )

    # Actualizar solo los campos proporcionados
    update_data = ubicacion.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_ubicacion, field, value)

    db.commit()
    db.refresh(db_ubicacion)
    return db_ubicacion


@router.delete("/{ubicacion_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_ubicacion(ubicacion_id: int, db: Session = Depends(get_db)):
    """Eliminar una ubicación"""
    db_ubicacion = db.query(Ubicacion).filter(Ubicacion.id == ubicacion_id).first()
    if not db_ubicacion:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Ubicación con ID {ubicacion_id} no encontrada"
        )

    db.delete(db_ubicacion)
    db.commit()
    return None
