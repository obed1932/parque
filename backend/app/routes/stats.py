"""
Rutas para Estadísticas
"""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from ..database import get_db
from ..models import Equipo, Ubicacion, Usuario, Mantenimiento

router = APIRouter(prefix="/stats", tags=["Estadísticas"])


@router.get("/dashboard")
def obtener_estadisticas_dashboard(db: Session = Depends(get_db)):
    """Obtener estadísticas generales para el dashboard"""

    # Total de equipos
    total_equipos = db.query(func.count(Equipo.id)).scalar()

    # Equipos por estado
    equipos_por_estado = db.query(
        Equipo.estado,
        func.count(Equipo.id).label('cantidad')
    ).group_by(Equipo.estado).all()

    # Total de ubicaciones
    total_ubicaciones = db.query(func.count(Ubicacion.id)).scalar()

    # Total de usuarios
    total_usuarios = db.query(func.count(Usuario.id)).scalar()

    # Usuarios activos
    usuarios_activos = db.query(func.count(Usuario.id)).filter(
        Usuario.activo == True
    ).scalar()

    # Equipos por tipo
    equipos_por_tipo = db.query(
        Equipo.tipo_equipo,
        func.count(Equipo.id).label('cantidad')
    ).group_by(Equipo.tipo_equipo).all()

    # Total de mantenimientos
    total_mantenimientos = db.query(func.count(Mantenimiento.id)).scalar()

    # Costo total de mantenimientos
    costo_total_mantenimientos = db.query(
        func.sum(Mantenimiento.costo)
    ).scalar() or 0

    return {
        "total_equipos": total_equipos,
        "equipos_por_estado": [
            {"estado": estado, "cantidad": cantidad}
            for estado, cantidad in equipos_por_estado
        ],
        "total_ubicaciones": total_ubicaciones,
        "total_usuarios": total_usuarios,
        "usuarios_activos": usuarios_activos,
        "equipos_por_tipo": [
            {"tipo": tipo, "cantidad": cantidad}
            for tipo, cantidad in equipos_por_tipo
        ],
        "total_mantenimientos": total_mantenimientos,
        "costo_total_mantenimientos": float(costo_total_mantenimientos)
    }


@router.get("/equipos-por-ubicacion")
def obtener_equipos_por_ubicacion(db: Session = Depends(get_db)):
    """Obtener cantidad de equipos por ubicación"""
    resultados = db.query(
        Ubicacion.nombre,
        func.count(Equipo.id).label('cantidad')
    ).join(Equipo, Equipo.ubicacion_id == Ubicacion.id, isouter=True)\
     .group_by(Ubicacion.id, Ubicacion.nombre).all()

    return [
        {"ubicacion": nombre, "cantidad": cantidad}
        for nombre, cantidad in resultados
    ]


@router.get("/equipos-asignados")
def obtener_equipos_asignados(db: Session = Depends(get_db)):
    """Obtener estadísticas de equipos asignados vs no asignados"""
    equipos_asignados = db.query(func.count(Equipo.id)).filter(
        Equipo.usuario_id.isnot(None)
    ).scalar()

    equipos_no_asignados = db.query(func.count(Equipo.id)).filter(
        Equipo.usuario_id.is_(None)
    ).scalar()

    return {
        "equipos_asignados": equipos_asignados,
        "equipos_no_asignados": equipos_no_asignados,
        "total": equipos_asignados + equipos_no_asignados
    }
