-- ============================================
-- SISTEMA DE GESTIÓN DE PARQUE INFORMÁTICO
-- Esquema de Base de Datos SQLite
-- ============================================

-- Tabla de Ubicaciones/Servicios
CREATE TABLE IF NOT EXISTS ubicaciones (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre VARCHAR(100) NOT NULL,
    departamento VARCHAR(100),
    edificio VARCHAR(50),
    piso VARCHAR(20),
    descripcion TEXT,
    responsable VARCHAR(100),
    telefono VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabla de Usuarios/Empleados
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    telefono VARCHAR(20),
    cargo VARCHAR(100),
    departamento VARCHAR(100),
    activo BOOLEAN DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabla Principal de Equipos/PCs
CREATE TABLE IF NOT EXISTS equipos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    codigo_inventario VARCHAR(50) UNIQUE NOT NULL,
    nombre_equipo VARCHAR(100),
    tipo_equipo VARCHAR(50) DEFAULT 'Desktop', -- Desktop, Laptop, Servidor, etc.
    marca VARCHAR(50),
    modelo VARCHAR(100),
    numero_serie VARCHAR(100) UNIQUE,
    fecha_adquisicion DATE,
    fecha_garantia DATE,
    proveedor VARCHAR(100),
    precio_compra DECIMAL(10,2),
    estado VARCHAR(50) DEFAULT 'Operativo', -- Operativo, En reparación, Baja, etc.
    sistema_operativo VARCHAR(100),
    version_so VARCHAR(50),
    licencia_so VARCHAR(100),
    observaciones TEXT,
    ubicacion_id INTEGER,
    usuario_id INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (ubicacion_id) REFERENCES ubicaciones(id) ON DELETE SET NULL,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE SET NULL
);

-- Tabla de Procesadores
CREATE TABLE IF NOT EXISTS procesadores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    equipo_id INTEGER NOT NULL,
    marca VARCHAR(50),
    modelo VARCHAR(100),
    nucleos INTEGER,
    hilos INTEGER,
    frecuencia_base VARCHAR(20), -- En GHz
    frecuencia_turbo VARCHAR(20),
    socket VARCHAR(50),
    cache VARCHAR(50),
    FOREIGN KEY (equipo_id) REFERENCES equipos(id) ON DELETE CASCADE
);

-- Tabla de Memoria RAM
CREATE TABLE IF NOT EXISTS memoria_ram (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    equipo_id INTEGER NOT NULL,
    tipo VARCHAR(20), -- DDR3, DDR4, DDR5, etc.
    capacidad_gb INTEGER,
    velocidad_mhz INTEGER,
    marca VARCHAR(50),
    modelo VARCHAR(100),
    slots_ocupados INTEGER,
    slots_totales INTEGER,
    FOREIGN KEY (equipo_id) REFERENCES equipos(id) ON DELETE CASCADE
);

-- Tabla de Almacenamiento
CREATE TABLE IF NOT EXISTS almacenamiento (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    equipo_id INTEGER NOT NULL,
    tipo VARCHAR(20), -- HDD, SSD, NVMe, etc.
    capacidad_gb INTEGER,
    marca VARCHAR(50),
    modelo VARCHAR(100),
    numero_serie VARCHAR(100),
    interfaz VARCHAR(20), -- SATA, NVMe, etc.
    es_principal BOOLEAN DEFAULT 0,
    FOREIGN KEY (equipo_id) REFERENCES equipos(id) ON DELETE CASCADE
);

-- Tabla de Tarjetas Gráficas
CREATE TABLE IF NOT EXISTS tarjetas_graficas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    equipo_id INTEGER NOT NULL,
    tipo VARCHAR(20), -- Integrada, Dedicada
    marca VARCHAR(50),
    modelo VARCHAR(100),
    memoria_gb INTEGER,
    tipo_memoria VARCHAR(20), -- GDDR5, GDDR6, etc.
    FOREIGN KEY (equipo_id) REFERENCES equipos(id) ON DELETE CASCADE
);

-- Tabla de Placas Base
CREATE TABLE IF NOT EXISTS placas_base (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    equipo_id INTEGER NOT NULL,
    marca VARCHAR(50),
    modelo VARCHAR(100),
    chipset VARCHAR(50),
    socket VARCHAR(50),
    factor_forma VARCHAR(20), -- ATX, Micro-ATX, Mini-ITX, etc.
    FOREIGN KEY (equipo_id) REFERENCES equipos(id) ON DELETE CASCADE
);

-- Tabla de Fuentes de Alimentación
CREATE TABLE IF NOT EXISTS fuentes_alimentacion (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    equipo_id INTEGER NOT NULL,
    marca VARCHAR(50),
    modelo VARCHAR(100),
    potencia_watts INTEGER,
    certificacion VARCHAR(50), -- 80 Plus, Bronze, Silver, Gold, etc.
    FOREIGN KEY (equipo_id) REFERENCES equipos(id) ON DELETE CASCADE
);

-- Tabla de Periféricos
CREATE TABLE IF NOT EXISTS perifericos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    equipo_id INTEGER,
    tipo VARCHAR(50), -- Monitor, Teclado, Mouse, Impresora, etc.
    marca VARCHAR(50),
    modelo VARCHAR(100),
    numero_serie VARCHAR(100),
    especificaciones TEXT,
    estado VARCHAR(50) DEFAULT 'Operativo',
    FOREIGN KEY (equipo_id) REFERENCES equipos(id) ON DELETE SET NULL
);

-- Tabla de Red
CREATE TABLE IF NOT EXISTS componentes_red (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    equipo_id INTEGER NOT NULL,
    tipo VARCHAR(50), -- Ethernet, WiFi
    marca VARCHAR(50),
    modelo VARCHAR(100),
    velocidad VARCHAR(50), -- 1Gbps, 2.5Gbps, WiFi 6, etc.
    mac_address VARCHAR(17),
    FOREIGN KEY (equipo_id) REFERENCES equipos(id) ON DELETE CASCADE
);

-- Tabla de Historial de Mantenimiento
CREATE TABLE IF NOT EXISTS mantenimientos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    equipo_id INTEGER NOT NULL,
    tipo_mantenimiento VARCHAR(50), -- Preventivo, Correctivo, Actualización
    descripcion TEXT,
    fecha_mantenimiento DATE NOT NULL,
    tecnico_responsable VARCHAR(100),
    costo DECIMAL(10,2),
    tiempo_inactividad_horas INTEGER,
    proximo_mantenimiento DATE,
    observaciones TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (equipo_id) REFERENCES equipos(id) ON DELETE CASCADE
);

-- Tabla de Software Instalado
CREATE TABLE IF NOT EXISTS software (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    equipo_id INTEGER NOT NULL,
    nombre VARCHAR(100) NOT NULL,
    version VARCHAR(50),
    fabricante VARCHAR(100),
    tipo VARCHAR(50), -- Aplicación, Utilidad, Desarrollo, etc.
    licencia VARCHAR(100),
    fecha_instalacion DATE,
    fecha_expiracion_licencia DATE,
    FOREIGN KEY (equipo_id) REFERENCES equipos(id) ON DELETE CASCADE
);

-- Tabla de Historial de Asignaciones
CREATE TABLE IF NOT EXISTS historial_asignaciones (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    equipo_id INTEGER NOT NULL,
    usuario_id INTEGER,
    ubicacion_id INTEGER,
    fecha_asignacion DATE NOT NULL,
    fecha_devolucion DATE,
    motivo TEXT,
    estado VARCHAR(50),
    FOREIGN KEY (equipo_id) REFERENCES equipos(id) ON DELETE CASCADE,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE SET NULL,
    FOREIGN KEY (ubicacion_id) REFERENCES ubicaciones(id) ON DELETE SET NULL
);

-- Índices para mejorar el rendimiento
CREATE INDEX idx_equipos_codigo ON equipos(codigo_inventario);
CREATE INDEX idx_equipos_ubicacion ON equipos(ubicacion_id);
CREATE INDEX idx_equipos_usuario ON equipos(usuario_id);
CREATE INDEX idx_equipos_estado ON equipos(estado);
CREATE INDEX idx_mantenimientos_equipo ON mantenimientos(equipo_id);
CREATE INDEX idx_mantenimientos_fecha ON mantenimientos(fecha_mantenimiento);
CREATE INDEX idx_software_equipo ON software(equipo_id);
CREATE INDEX idx_historial_equipo ON historial_asignaciones(equipo_id);

-- Triggers para actualizar timestamps
CREATE TRIGGER update_equipos_timestamp
AFTER UPDATE ON equipos
BEGIN
    UPDATE equipos SET updated_at = CURRENT_TIMESTAMP WHERE id = NEW.id;
END;

CREATE TRIGGER update_ubicaciones_timestamp
AFTER UPDATE ON ubicaciones
BEGIN
    UPDATE ubicaciones SET updated_at = CURRENT_TIMESTAMP WHERE id = NEW.id;
END;

CREATE TRIGGER update_usuarios_timestamp
AFTER UPDATE ON usuarios
BEGIN
    UPDATE usuarios SET updated_at = CURRENT_TIMESTAMP WHERE id = NEW.id;
END;
