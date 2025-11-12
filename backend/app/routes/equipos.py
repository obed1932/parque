"""
Rutas para Equipos
"""
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from ..database import get_db
from ..models import Equipo
from ..schemas import EquipoCreate, EquipoUpdate, EquipoResponse, EquipoDetailResponse

router = APIRouter(prefix="/equipos", tags=["Equipos"])


@router.get("/", response_model=List[EquipoResponse])
def listar_equipos(
    skip: int = 0,
    limit: int = 100,
    estado: str = None,
    ubicacion_id: int = None,
    db: Session = Depends(get_db)
):
    """Listar todos los equipos con filtros opcionales"""
    query = db.query(Equipo)

    if estado:
        query = query.filter(Equipo.estado == estado)
    if ubicacion_id:
        query = query.filter(Equipo.ubicacion_id == ubicacion_id)

    equipos = query.offset(skip).limit(limit).all()
    return equipos


@router.get("/{equipo_id}", response_model=EquipoDetailResponse)
def obtener_equipo(equipo_id: int, db: Session = Depends(get_db)):
    """Obtener un equipo por ID con información detallada de hardware"""
    equipo = db.query(Equipo).filter(Equipo.id == equipo_id).first()
    if not equipo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Equipo con ID {equipo_id} no encontrado"
        )
    return equipo


@router.post("/", response_model=EquipoResponse, status_code=status.HTTP_201_CREATED)
def crear_equipo(equipo: EquipoCreate, db: Session = Depends(get_db)):
    """Crear un nuevo equipo"""
    # Verificar que el código de inventario no exista
    existing = db.query(Equipo).filter(
        Equipo.codigo_inventario == equipo.codigo_inventario
    ).first()
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Ya existe un equipo con el código {equipo.codigo_inventario}"
        )

    db_equipo = Equipo(**equipo.model_dump())
    db.add(db_equipo)
    db.commit()
    db.refresh(db_equipo)
    return db_equipo


@router.put("/{equipo_id}", response_model=EquipoResponse)
def actualizar_equipo(
    equipo_id: int,
    equipo: EquipoUpdate,
    db: Session = Depends(get_db)
):
    """Actualizar un equipo existente"""
    db_equipo = db.query(Equipo).filter(Equipo.id == equipo_id).first()
    if not db_equipo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Equipo con ID {equipo_id} no encontrado"
        )

    # Actualizar solo los campos proporcionados
    update_data = equipo.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_equipo, field, value)

    db.commit()
    db.refresh(db_equipo)
    return db_equipo


@router.delete("/{equipo_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_equipo(equipo_id: int, db: Session = Depends(get_db)):
    """Eliminar un equipo"""
    db_equipo = db.query(Equipo).filter(Equipo.id == equipo_id).first()
    if not db_equipo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Equipo con ID {equipo_id} no encontrado"
        )

    db.delete(db_equipo)
    db.commit()
    return None


@router.get("/codigo/{codigo}", response_model=EquipoResponse)
def buscar_por_codigo(codigo: str, db: Session = Depends(get_db)):
    """Buscar equipo por código de inventario"""
    equipo = db.query(Equipo).filter(Equipo.codigo_inventario == codigo).first()
    if not equipo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Equipo con código {codigo} no encontrado"
        )
    return equipo
