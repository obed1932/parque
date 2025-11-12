# Sistema de Gestión de Parque Informático

## Arquitectura del Sistema

### Estructura del Proyecto

```
parque/
├── backend/                    # API REST Backend
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py            # Punto de entrada FastAPI
│   │   ├── config.py          # Configuración
│   │   ├── database/
│   │   │   ├── __init__.py
│   │   │   ├── connection.py  # Conexión SQLite
│   │   │   └── init_db.py     # Inicialización DB
│   │   ├── models/            # Modelos SQLAlchemy
│   │   │   ├── __init__.py
│   │   │   ├── equipo.py
│   │   │   ├── usuario.py
│   │   │   ├── ubicacion.py
│   │   │   ├── hardware.py
│   │   │   └── mantenimiento.py
│   │   ├── schemas/           # Schemas Pydantic
│   │   │   ├── __init__.py
│   │   │   ├── equipo.py
│   │   │   ├── usuario.py
│   │   │   └── ubicacion.py
│   │   ├── routes/            # Endpoints API
│   │   │   ├── __init__.py
│   │   │   ├── equipos.py
│   │   │   ├── usuarios.py
│   │   │   ├── ubicaciones.py
│   │   │   ├── hardware.py
│   │   │   └── mantenimientos.py
│   │   └── services/          # Lógica de negocio
│   │       ├── __init__.py
│   │       ├── equipo_service.py
│   │       └── stats_service.py
│   ├── tests/
│   ├── requirements.txt
│   └── README.md
│
├── frontend/                   # Interfaz React
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   │   ├── common/        # Componentes reutilizables
│   │   │   │   ├── Navbar.jsx
│   │   │   │   ├── Sidebar.jsx
│   │   │   │   ├── Table.jsx
│   │   │   │   └── Modal.jsx
│   │   │   ├── equipos/
│   │   │   │   ├── EquiposList.jsx
│   │   │   │   ├── EquipoForm.jsx
│   │   │   │   └── EquipoDetail.jsx
│   │   │   ├── ubicaciones/
│   │   │   │   ├── UbicacionesList.jsx
│   │   │   │   └── UbicacionForm.jsx
│   │   │   ├── usuarios/
│   │   │   │   ├── UsuariosList.jsx
│   │   │   │   └── UsuarioForm.jsx
│   │   │   └── dashboard/
│   │   │       ├── Dashboard.jsx
│   │   │       └── StatsCard.jsx
│   │   ├── pages/
│   │   │   ├── Home.jsx
│   │   │   ├── Equipos.jsx
│   │   │   ├── Usuarios.jsx
│   │   │   └── Ubicaciones.jsx
│   │   ├── services/
│   │   │   ├── api.js         # Configuración Axios
│   │   │   ├── equipos.js
│   │   │   ├── usuarios.js
│   │   │   └── ubicaciones.js
│   │   ├── utils/
│   │   │   └── helpers.js
│   │   ├── styles/
│   │   ├── App.jsx
│   │   └── main.jsx
│   ├── package.json
│   ├── vite.config.js
│   └── tailwind.config.js
│
├── docs/
│   ├── API.md
│   └── MANUAL_USUARIO.md
│
├── database_schema.sql
└── README.md
```

## Stack Tecnológico

### Backend
- **Framework**: FastAPI (Python 3.10+)
- **Base de Datos**: SQLite
- **ORM**: SQLAlchemy
- **Validación**: Pydantic
- **CORS**: FastAPI CORS Middleware

### Frontend
- **Framework**: React 18
- **Build Tool**: Vite
- **Estilos**: TailwindCSS
- **Routing**: React Router DOM
- **HTTP Client**: Axios
- **Iconos**: Lucide React

## Esquema de Base de Datos

### Tablas Principales

1. **ubicaciones**: Lugares físicos donde se encuentran los equipos
2. **usuarios**: Empleados que usan los equipos
3. **equipos**: Información principal de cada PC
4. **procesadores**: Detalles de CPUs
5. **memoria_ram**: Información de RAM
6. **almacenamiento**: Discos duros/SSDs
7. **tarjetas_graficas**: GPUs
8. **placas_base**: Motherboards
9. **fuentes_alimentacion**: PSUs
10. **componentes_red**: Tarjetas de red
11. **perifericos**: Monitores, teclados, etc.
12. **mantenimientos**: Historial de mantenimiento
13. **software**: Software instalado
14. **historial_asignaciones**: Registro de asignaciones

## API Endpoints

### Equipos
- `GET /api/equipos` - Listar todos los equipos
- `GET /api/equipos/{id}` - Obtener equipo por ID
- `POST /api/equipos` - Crear nuevo equipo
- `PUT /api/equipos/{id}` - Actualizar equipo
- `DELETE /api/equipos/{id}` - Eliminar equipo
- `GET /api/equipos/{id}/hardware` - Obtener hardware completo

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
- etc.

### Mantenimientos
- `GET /api/mantenimientos` - Listar mantenimientos
- `POST /api/mantenimientos` - Registrar mantenimiento
- `GET /api/mantenimientos/equipo/{id}` - Historial por equipo

### Estadísticas
- `GET /api/stats/dashboard` - Estadísticas generales
- `GET /api/stats/equipos-por-ubicacion` - Equipos por ubicación
- `GET /api/stats/equipos-por-estado` - Equipos por estado

## Características del Sistema

### Gestión de Equipos
- Registro completo de hardware
- Seguimiento de ubicación y usuario
- Historial de cambios
- Estado del equipo

### Gestión de Hardware
- Procesadores
- Memoria RAM
- Almacenamiento
- Tarjetas gráficas
- Placas base
- Fuentes de alimentación
- Componentes de red
- Periféricos

### Gestión de Mantenimiento
- Programación de mantenimientos
- Historial de reparaciones
- Costos de mantenimiento
- Seguimiento de garantías

### Reportes y Estadísticas
- Dashboard con métricas clave
- Equipos por ubicación
- Equipos por estado
- Historial de mantenimientos
- Costos y gastos

## Flujo de Datos

1. **Frontend** realiza peticiones HTTP a la API
2. **API (FastAPI)** recibe y valida con Pydantic
3. **Services** procesan la lógica de negocio
4. **Models (SQLAlchemy)** interactúan con SQLite
5. **Database** almacena y recupera datos
6. Respuesta JSON al frontend

## Seguridad

- Validación de datos con Pydantic
- Manejo de errores centralizado
- CORS configurado
- SQL injection prevenido por ORM

## Despliegue

### Desarrollo
```bash
# Backend
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload

# Frontend
cd frontend
npm install
npm run dev
```

### Producción
- Backend: Uvicorn + Nginx
- Frontend: Build estático servido por Nginx
- Base de datos: SQLite (considerar PostgreSQL para mayor escala)
