/**
 * Formulario para crear/editar equipos
 */
import { useState, useEffect } from 'react';
import { equiposService } from '../../services/equipos';
import { ubicacionesService } from '../../services/ubicaciones';
import { usuariosService } from '../../services/usuarios';

export default function EquipoForm({ equipo, onSuccess, onCancel }) {
  const [formData, setFormData] = useState({
    codigo_inventario: '',
    nombre_equipo: '',
    tipo_equipo: 'Desktop',
    marca: '',
    modelo: '',
    numero_serie: '',
    fecha_adquisicion: '',
    fecha_garantia: '',
    proveedor: '',
    precio_compra: '',
    estado: 'Operativo',
    sistema_operativo: '',
    version_so: '',
    licencia_so: '',
    observaciones: '',
    ubicacion_id: '',
    usuario_id: '',
  });

  const [ubicaciones, setUbicaciones] = useState([]);
  const [usuarios, setUsuarios] = useState([]);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    loadUbicaciones();
    loadUsuarios();
    if (equipo) {
      setFormData({ ...equipo });
    }
  }, [equipo]);

  const loadUbicaciones = async () => {
    try {
      const data = await ubicacionesService.getAll();
      setUbicaciones(data);
    } catch (error) {
      console.error('Error al cargar ubicaciones:', error);
    }
  };

  const loadUsuarios = async () => {
    try {
      const data = await usuariosService.getAll({ activo: true });
      setUsuarios(data);
    } catch (error) {
      console.error('Error al cargar usuarios:', error);
    }
  };

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prev) => ({ ...prev, [name]: value }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);

    try {
      const dataToSend = {
        ...formData,
        ubicacion_id: formData.ubicacion_id ? parseInt(formData.ubicacion_id) : null,
        usuario_id: formData.usuario_id ? parseInt(formData.usuario_id) : null,
        precio_compra: formData.precio_compra ? parseFloat(formData.precio_compra) : null,
      };

      if (equipo) {
        await equiposService.update(equipo.id, dataToSend);
      } else {
        await equiposService.create(dataToSend);
      }
      onSuccess();
    } catch (error) {
      alert('Error al guardar el equipo: ' + (error.response?.data?.detail || error.message));
    } finally {
      setLoading(false);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="space-y-4">
      <div className="grid grid-cols-2 gap-4">
        <div>
          <label className="block text-sm font-medium text-gray-700 mb-1">
            Código de Inventario *
          </label>
          <input
            type="text"
            name="codigo_inventario"
            value={formData.codigo_inventario}
            onChange={handleChange}
            required
            className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
          />
        </div>

        <div>
          <label className="block text-sm font-medium text-gray-700 mb-1">
            Nombre del Equipo
          </label>
          <input
            type="text"
            name="nombre_equipo"
            value={formData.nombre_equipo}
            onChange={handleChange}
            className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
          />
        </div>

        <div>
          <label className="block text-sm font-medium text-gray-700 mb-1">
            Tipo de Equipo
          </label>
          <select
            name="tipo_equipo"
            value={formData.tipo_equipo}
            onChange={handleChange}
            className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
          >
            <option value="Desktop">Desktop</option>
            <option value="Laptop">Laptop</option>
            <option value="Servidor">Servidor</option>
            <option value="All-in-One">All-in-One</option>
          </select>
        </div>

        <div>
          <label className="block text-sm font-medium text-gray-700 mb-1">
            Marca
          </label>
          <input
            type="text"
            name="marca"
            value={formData.marca}
            onChange={handleChange}
            className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
          />
        </div>

        <div>
          <label className="block text-sm font-medium text-gray-700 mb-1">
            Modelo
          </label>
          <input
            type="text"
            name="modelo"
            value={formData.modelo}
            onChange={handleChange}
            className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
          />
        </div>

        <div>
          <label className="block text-sm font-medium text-gray-700 mb-1">
            Número de Serie
          </label>
          <input
            type="text"
            name="numero_serie"
            value={formData.numero_serie}
            onChange={handleChange}
            className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
          />
        </div>

        <div>
          <label className="block text-sm font-medium text-gray-700 mb-1">
            Estado
          </label>
          <select
            name="estado"
            value={formData.estado}
            onChange={handleChange}
            className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
          >
            <option value="Operativo">Operativo</option>
            <option value="En reparación">En reparación</option>
            <option value="Baja">Baja</option>
            <option value="Almacenado">Almacenado</option>
          </select>
        </div>

        <div>
          <label className="block text-sm font-medium text-gray-700 mb-1">
            Sistema Operativo
          </label>
          <input
            type="text"
            name="sistema_operativo"
            value={formData.sistema_operativo}
            onChange={handleChange}
            placeholder="Ej: Windows 11"
            className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
          />
        </div>

        <div>
          <label className="block text-sm font-medium text-gray-700 mb-1">
            Ubicación
          </label>
          <select
            name="ubicacion_id"
            value={formData.ubicacion_id}
            onChange={handleChange}
            className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
          >
            <option value="">Sin asignar</option>
            {ubicaciones.map((ub) => (
              <option key={ub.id} value={ub.id}>
                {ub.nombre}
              </option>
            ))}
          </select>
        </div>

        <div>
          <label className="block text-sm font-medium text-gray-700 mb-1">
            Usuario Asignado
          </label>
          <select
            name="usuario_id"
            value={formData.usuario_id}
            onChange={handleChange}
            className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
          >
            <option value="">Sin asignar</option>
            {usuarios.map((usr) => (
              <option key={usr.id} value={usr.id}>
                {usr.nombre} {usr.apellido}
              </option>
            ))}
          </select>
        </div>
      </div>

      <div>
        <label className="block text-sm font-medium text-gray-700 mb-1">
          Observaciones
        </label>
        <textarea
          name="observaciones"
          value={formData.observaciones}
          onChange={handleChange}
          rows="3"
          className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
        />
      </div>

      <div className="flex justify-end space-x-3 pt-4">
        <button
          type="button"
          onClick={onCancel}
          className="px-4 py-2 border border-gray-300 rounded-md text-gray-700 hover:bg-gray-50"
        >
          Cancelar
        </button>
        <button
          type="submit"
          disabled={loading}
          className="px-4 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700 disabled:bg-gray-400"
        >
          {loading ? 'Guardando...' : 'Guardar'}
        </button>
      </div>
    </form>
  );
}
