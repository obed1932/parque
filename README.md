# Sistema de Gestión de Parque Informático

Sistema completo para la gestión y control de inventario de equipos informáticos, desarrollado con FastAPI (Python) y React.

## Características Principales

- Gestión completa de equipos informáticos
- Registro detallado de hardware (CPU, RAM, almacenamiento, GPU, etc.)
- Control de ubicaciones y asignaciones
- Gestión de usuarios y empleados
- Historial de mantenimientos
- Dashboard con estadísticas en tiempo real
- API REST documentada automáticamente
- Interfaz de usuario moderna y responsive

## Estructura del Proyecto

```
parque/
├── backend/                # API REST con FastAPI
│   ├── app/
│   │   ├── models/        # Modelos SQLAlchemy
│   │   ├── schemas/       # Schemas Pydantic
│   │   ├── routes/        # Endpoints API
│   │   ├── database/      # Configuración BD
│   │   └── main.py        # App principal
│   └── requirements.txt
│
├── frontend/              # Interfaz React
│   ├── src/
│   │   ├── components/    # Componentes React
│   │   ├── pages/         # Páginas
│   │   ├── services/      # Servicios API
│   │   └── styles/        # Estilos
│   └── package.json
│
├── docs/                  # Documentación
├── database_schema.sql    # Esquema de BD
└── ARQUITECTURA.md        # Documentación técnica
```

## Stack Tecnológico

### Backend
- **FastAPI**: Framework web moderno y rápido
- **SQLAlchemy**: ORM para Python
- **Pydantic**: Validación de datos
- **SQLite**: Base de datos
- **Uvicorn**: Servidor ASGI

### Frontend
- **React 18**: Biblioteca de UI
- **Vite**: Build tool
- **TailwindCSS**: Framework CSS
- **React Router**: Enrutamiento
- **Axios**: Cliente HTTP
- **Lucide React**: Iconos

## Instalación y Configuración

### Requisitos Previos

- Python 3.10 o superior
- Node.js 18 o superior
- npm o yarn

### Instalación del Backend

1. Navegar al directorio backend:
```bash
cd backend
```

2. Crear entorno virtual:
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

4. Iniciar el servidor:
```bash
uvicorn app.main:app --reload
```

El backend estará disponible en: http://localhost:8000
Documentación API: http://localhost:8000/docs

### Instalación del Frontend

1. Navegar al directorio frontend:
```bash
cd frontend
```

2. Instalar dependencias:
```bash
npm install
```

3. Iniciar el servidor de desarrollo:
```bash
npm run dev
```

El frontend estará disponible en: http://localhost:5173

## Uso del Sistema

### 1. Dashboard
- Vista general del parque informático
- Estadísticas de equipos, usuarios y ubicaciones
- Gráficos de distribución

### 2. Gestión de Equipos
- Crear, editar y eliminar equipos
- Registrar información detallada de hardware
- Asignar a ubicaciones y usuarios
- Ver historial completo

### 3. Gestión de Usuarios
- Administrar usuarios del sistema
- Asignar equipos a empleados
- Control de usuarios activos/inactivos

### 4. Gestión de Ubicaciones
- Crear y administrar ubicaciones físicas
- Organizar por edificios, pisos y departamentos
- Asignar responsables

## API Endpoints

### Equipos
```
GET    /api/equipos              # Listar todos
GET    /api/equipos/{id}         # Obtener por ID
POST   /api/equipos              # Crear
PUT    /api/equipos/{id}         # Actualizar
DELETE /api/equipos/{id}         # Eliminar
GET    /api/equipos/codigo/{codigo}  # Buscar por código
```

### Usuarios
```
GET    /api/usuarios             # Listar todos
GET    /api/usuarios/{id}        # Obtener por ID
POST   /api/usuarios             # Crear
PUT    /api/usuarios/{id}        # Actualizar
DELETE /api/usuarios/{id}        # Eliminar
```

### Ubicaciones
```
GET    /api/ubicaciones          # Listar todas
GET    /api/ubicaciones/{id}     # Obtener por ID
POST   /api/ubicaciones          # Crear
PUT    /api/ubicaciones/{id}     # Actualizar
DELETE /api/ubicaciones/{id}     # Eliminar
```

### Hardware
```
POST   /api/hardware/procesador      # Agregar procesador
POST   /api/hardware/ram             # Agregar RAM
POST   /api/hardware/almacenamiento  # Agregar almacenamiento
POST   /api/hardware/gpu             # Agregar GPU
POST   /api/hardware/placa-base      # Agregar placa base
POST   /api/hardware/fuente          # Agregar fuente
POST   /api/hardware/red             # Agregar componente de red
POST   /api/hardware/periferico      # Agregar periférico
```

### Mantenimientos
```
GET    /api/mantenimientos                # Listar todos
GET    /api/mantenimientos/equipo/{id}    # Por equipo
POST   /api/mantenimientos                # Registrar
```

### Estadísticas
```
GET    /api/stats/dashboard               # Estadísticas generales
GET    /api/stats/equipos-por-ubicacion   # Distribución
GET    /api/stats/equipos-asignados       # Asignaciones
```

## Base de Datos

El sistema utiliza SQLite con el siguiente esquema:

- **ubicaciones**: Lugares físicos
- **usuarios**: Empleados del sistema
- **equipos**: Información principal de PCs
- **procesadores**: CPUs
- **memoria_ram**: Módulos de RAM
- **almacenamiento**: Discos duros/SSDs
- **tarjetas_graficas**: GPUs
- **placas_base**: Motherboards
- **fuentes_alimentacion**: PSUs
- **componentes_red**: Tarjetas de red
- **perifericos**: Monitores, teclados, etc.
- **mantenimientos**: Historial de mantenimiento
- **software**: Software instalado
- **historial_asignaciones**: Registro de asignaciones

Ver `database_schema.sql` para el esquema completo.

## Desarrollo

### Backend

Ejecutar en modo desarrollo con recarga automática:
```bash
uvicorn app.main:app --reload
```

### Frontend

Ejecutar servidor de desarrollo:
```bash
npm run dev
```

Build de producción:
```bash
npm run build
```

## Documentación Adicional

- [ARQUITECTURA.md](./ARQUITECTURA.md) - Arquitectura del sistema
- [backend/README.md](./backend/README.md) - Documentación del backend
- [frontend/README.md](./frontend/README.md) - Documentación del frontend
- [database_schema.sql](./database_schema.sql) - Esquema de base de datos
- [docs/MANUAL_USUARIO.md](./docs/MANUAL_USUARIO.md) - Manual de usuario

## Características Futuras

- Autenticación y autorización
- Reportes en PDF/Excel
- Sistema de notificaciones
- Gestión de garantías automática
- Integración con sistemas de tickets
- Aplicación móvil
- Backup automático

## Licencia

Este proyecto es de código abierto.

## Autor

Sistema desarrollado para la gestión eficiente de parques informáticos.