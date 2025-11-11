# Manual de Usuario
## Sistema de Gestión de Parque Informático

## Introducción

Este manual le guiará en el uso del Sistema de Gestión de Parque Informático, una herramienta diseñada para administrar de manera eficiente el inventario de equipos informáticos de su organización.

## Acceso al Sistema

1. Abra su navegador web
2. Acceda a la URL del sistema: `http://localhost:5173` (desarrollo)
3. Verá el Dashboard principal

## Dashboard

El Dashboard es la página principal y muestra:

- **Total de Equipos**: Cantidad total de equipos registrados
- **Ubicaciones**: Número de ubicaciones configuradas
- **Usuarios Activos**: Empleados activos en el sistema
- **Mantenimientos**: Total de mantenimientos realizados
- **Equipos por Estado**: Distribución de equipos (Operativos, En reparación, etc.)
- **Equipos por Tipo**: Distribución por tipo (Desktop, Laptop, Servidor)
- **Costos de Mantenimiento**: Total acumulado de gastos

## Gestión de Equipos

### Listar Equipos

1. Haga clic en "Equipos" en la barra de navegación
2. Verá una tabla con todos los equipos registrados
3. La tabla muestra: Código, Nombre, Tipo, Marca, Modelo y Estado

### Crear Nuevo Equipo

1. Haga clic en el botón "Nuevo Equipo"
2. Complete el formulario:
   - **Código de Inventario** (requerido): Identificador único
   - **Nombre del Equipo**: Nombre descriptivo
   - **Tipo de Equipo**: Desktop, Laptop, Servidor, etc.
   - **Marca**: Fabricante del equipo
   - **Modelo**: Modelo específico
   - **Número de Serie**: Serial del fabricante
   - **Estado**: Operativo, En reparación, Baja, etc.
   - **Sistema Operativo**: SO instalado
   - **Ubicación**: Seleccione de la lista
   - **Usuario Asignado**: Seleccione de la lista
   - **Observaciones**: Notas adicionales
3. Haga clic en "Guardar"

### Ver Detalles de un Equipo

1. Haga clic sobre cualquier fila en la tabla de equipos
2. Se abrirá un modal con información detallada:
   - Información general
   - Especificaciones de hardware (CPU, RAM, almacenamiento, GPU)
   - Observaciones

### Editar un Equipo

1. Haga clic en el icono de lápiz (editar) en la fila del equipo
2. Modifique los campos necesarios
3. Haga clic en "Guardar"

### Eliminar un Equipo

1. Haga clic en el icono de papelera (eliminar) en la fila del equipo
2. Confirme la eliminación en el diálogo

**Nota**: Esta acción no se puede deshacer.

## Gestión de Usuarios

### Listar Usuarios

1. Haga clic en "Usuarios" en la barra de navegación
2. Verá una tabla con todos los usuarios registrados

### Crear Nuevo Usuario

1. Haga clic en "Nuevo Usuario"
2. Complete el formulario:
   - **Nombre** (requerido)
   - **Apellido** (requerido)
   - **Email**: Correo electrónico
   - **Teléfono**: Número de contacto
   - **Cargo**: Puesto de trabajo
   - **Departamento**: Área de trabajo
   - **Usuario activo**: Marque si está activo
3. Haga clic en "Guardar"

### Editar/Eliminar Usuarios

Similar al proceso de equipos, use los iconos de editar y eliminar en cada fila.

## Gestión de Ubicaciones

### Listar Ubicaciones

1. Haga clic en "Ubicaciones" en la barra de navegación
2. Verá todas las ubicaciones registradas

### Crear Nueva Ubicación

1. Haga clic en "Nueva Ubicación"
2. Complete el formulario:
   - **Nombre** (requerido): Nombre de la ubicación
   - **Departamento**: Departamento asociado
   - **Edificio**: Nombre del edificio
   - **Piso**: Número de piso
   - **Responsable**: Persona a cargo
   - **Teléfono**: Teléfono de contacto
   - **Descripción**: Información adicional
3. Haga clic en "Guardar"

## Filtros y Búsqueda

### Filtrar Equipos

En la página de equipos puede filtrar por:
- Estado (usando el parámetro de URL)
- Ubicación (usando el parámetro de URL)

### Buscar por Código

Use el endpoint de búsqueda para encontrar un equipo específico por su código de inventario.

## Estados de Equipos

Los equipos pueden tener los siguientes estados:

- **Operativo**: Funcionando correctamente
- **En reparación**: Necesita mantenimiento
- **Baja**: Dado de baja
- **Almacenado**: En almacén

Los estados se visualizan con colores:
- Verde: Operativo
- Amarillo: En reparación
- Rojo: Baja

## Tipos de Equipos

- **Desktop**: PC de escritorio
- **Laptop**: Computadora portátil
- **Servidor**: Servidor
- **All-in-One**: Todo en uno

## Asignación de Equipos

Para asignar un equipo a un usuario:

1. Edite el equipo
2. En el campo "Usuario Asignado", seleccione el usuario
3. Opcionalmente, seleccione una ubicación
4. Guarde los cambios

## Buenas Prácticas

### Códigos de Inventario

- Use un sistema consistente de numeración
- Ejemplo: `PC-001`, `LAP-001`, `SRV-001`
- No repita códigos

### Registro de Hardware

- Complete la mayor cantidad de información posible
- Registre todos los componentes importantes
- Actualice cuando realice mejoras

### Mantenimiento

- Registre todos los mantenimientos realizados
- Incluya costos para llevar control de gastos
- Programe mantenimientos preventivos

### Ubicaciones

- Cree ubicaciones específicas
- Asigne responsables
- Mantenga la información actualizada

## Solución de Problemas

### No puedo crear un equipo

- Verifique que el código de inventario sea único
- Asegúrese de completar todos los campos requeridos (*)

### No veo las estadísticas en el Dashboard

- Verifique que el backend esté ejecutándose
- Revise la consola del navegador para errores

### Error al eliminar

- Algunos registros no se pueden eliminar si tienen relaciones
- Contacte al administrador del sistema

## Atajos de Teclado

- **ESC**: Cerrar modales
- **Tab**: Navegar entre campos de formulario

## Soporte Técnico

Para soporte técnico o reportar problemas:
- Revise los logs del backend
- Contacte al equipo de desarrollo
- Consulte la documentación técnica en `/docs`

## Notas Adicionales

- El sistema se actualiza automáticamente al hacer cambios
- Los datos se guardan en una base de datos SQLite
- Realice copias de seguridad periódicas
- No comparta credenciales de acceso (cuando se implemente autenticación)
