# Backend - Sistema de Gestión de Parque Informático

API REST construida con FastAPI para gestión de inventario de equipos informáticos.

## Requisitos

- Python 3.10 o superior
- pip

## Instalación

1. Crear entorno virtual:
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

2. Instalar dependencias:
```bash
pip install -r requirements.txt
```

## Ejecución

### Modo Desarrollo
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Modo Producción
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

## Documentación API

Una vez iniciado el servidor, accede a:

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Estructura

```
backend/
├── app/
│   ├── __init__.py
│   ├── main.py              # Aplicación FastAPI
│   ├── config.py            # Configuración
│   ├── database/            # Conexión a BD
│   ├── models/              # Modelos SQLAlchemy
│   ├── schemas/             # Schemas Pydantic
│   ├── routes/              # Endpoints API
│   └── services/            # Lógica de negocio
├── requirements.txt
└── README.md
```

## Endpoints Principales

### Equipos
- `GET /api/equipos` - Listar equipos
- `GET /api/equipos/{id}` - Obtener equipo
- `POST /api/equipos` - Crear equipo
- `PUT /api/equipos/{id}` - Actualizar equipo
- `DELETE /api/equipos/{id}` - Eliminar equipo

### Usuarios
- `GET /api/usuarios` - Listar usuarios
- `GET /api/usuarios/{id}` - Obtener usuario
- `POST /api/usuarios` - Crear usuario
- `PUT /api/usuarios/{id}` - Actualizar usuario
- `DELETE /api/usuarios/{id}` - Eliminar usuario

### Ubicaciones
- `GET /api/ubicaciones` - Listar ubicaciones
- `GET /api/ubicaciones/{id}` - Obtener ubicación
- `POST /api/ubicaciones` - Crear ubicación
- `PUT /api/ubicaciones/{id}` - Actualizar ubicación
- `DELETE /api/ubicaciones/{id}` - Eliminar ubicación

### Hardware
- `POST /api/hardware/procesador` - Agregar procesador
- `POST /api/hardware/ram` - Agregar RAM
- `POST /api/hardware/almacenamiento` - Agregar almacenamiento
- `POST /api/hardware/gpu` - Agregar GPU
- `POST /api/hardware/placa-base` - Agregar placa base
- `POST /api/hardware/fuente` - Agregar fuente
- `POST /api/hardware/red` - Agregar componente de red
- `POST /api/hardware/periferico` - Agregar periférico

### Mantenimientos
- `GET /api/mantenimientos` - Listar mantenimientos
- `GET /api/mantenimientos/equipo/{id}` - Mantenimientos por equipo
- `POST /api/mantenimientos` - Registrar mantenimiento

### Estadísticas
- `GET /api/stats/dashboard` - Estadísticas generales
- `GET /api/stats/equipos-por-ubicacion` - Equipos por ubicación
- `GET /api/stats/equipos-asignados` - Equipos asignados

## Base de Datos

SQLite (`parque_informatico.db`) se crea automáticamente al iniciar la aplicación.

## Variables de Entorno

Crear archivo `.env` (opcional):

```env
DEBUG=True
DATABASE_URL=sqlite:///./parque_informatico.db
```

## Testing

```bash
pytest tests/
```
