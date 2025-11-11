# Frontend - Sistema de Gestión de Parque Informático

Interfaz de usuario construida con React, Vite y TailwindCSS.

## Requisitos

- Node.js 18 o superior
- npm o yarn

## Instalación

```bash
npm install
```

## Ejecución

### Modo Desarrollo
```bash
npm run dev
```

La aplicación estará disponible en: http://localhost:5173

### Build de Producción
```bash
npm run build
```

Los archivos se generarán en el directorio `dist/`.

### Vista Previa de Build
```bash
npm run preview
```

## Estructura

```
frontend/
├── public/               # Archivos estáticos
├── src/
│   ├── components/       # Componentes React
│   │   ├── common/      # Componentes reutilizables
│   │   ├── equipos/     # Componentes de equipos
│   │   ├── usuarios/    # Componentes de usuarios
│   │   ├── ubicaciones/ # Componentes de ubicaciones
│   │   └── dashboard/   # Dashboard
│   ├── pages/           # Páginas principales
│   ├── services/        # Servicios API
│   ├── styles/          # Estilos globales
│   ├── App.jsx          # Componente principal
│   └── main.jsx         # Punto de entrada
├── index.html
├── package.json
├── vite.config.js
└── tailwind.config.js
```

## Características

### Dashboard
- Estadísticas generales del parque informático
- Tarjetas de métricas principales
- Gráficos de distribución

### Gestión de Equipos
- Listado de equipos con filtros
- Formulario de creación/edición
- Vista detallada con información de hardware
- Asignación a ubicaciones y usuarios

### Gestión de Usuarios
- CRUD completo de usuarios
- Estado activo/inactivo
- Asignación de equipos

### Gestión de Ubicaciones
- CRUD completo de ubicaciones
- Departamentos y edificios
- Responsables

## Tecnologías

- **React 18**: Framework de UI
- **Vite**: Build tool y dev server
- **React Router DOM**: Enrutamiento
- **Axios**: Cliente HTTP
- **TailwindCSS**: Framework de CSS
- **Lucide React**: Iconos

## Configuración

### Variables de Entorno

Crear archivo `.env` en la raíz del proyecto:

```env
VITE_API_URL=http://localhost:8000/api
```

### Proxy de Desarrollo

El proxy está configurado en `vite.config.js` para redirigir las peticiones `/api` al backend.

## Componentes Principales

### Navbar
Barra de navegación principal con enlaces a todas las secciones.

### Table
Componente de tabla reutilizable con soporte para:
- Columnas personalizables
- Renderizado condicional de celdas
- Click en filas
- Acciones por fila

### Modal
Modal reutilizable para formularios y detalles.

### StatsCard
Tarjeta de estadísticas con iconos y colores personalizables.

## Estilos

Utiliza TailwindCSS con la configuración por defecto. Los estilos globales están en `src/styles/index.css`.

## Desarrollo

### Agregar Nueva Página

1. Crear componente en `src/pages/`
2. Agregar ruta en `src/App.jsx`
3. Agregar enlace en `src/components/common/Navbar.jsx`

### Agregar Nuevo Servicio API

1. Crear archivo en `src/services/`
2. Importar y usar la instancia de axios de `src/services/api.js`

## Build

```bash
npm run build
```

El build optimizado se genera en `dist/` y puede ser servido por cualquier servidor web estático.
