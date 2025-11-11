/**
 * Página de Ubicaciones
 */
import { useEffect, useState } from 'react';
import { Plus, Trash2, Edit } from 'lucide-react';
import Table from '../components/common/Table';
import Modal from '../components/common/Modal';
import { ubicacionesService } from '../services/ubicaciones';

function UbicacionForm({ ubicacion, onSuccess, onCancel }) {
  const [formData, setFormData] = useState({
    nombre: '',
    departamento: '',
    edificio: '',
    piso: '',
    descripcion: '',
    responsable: '',
    telefono: '',
  });

  useEffect(() => {
    if (ubicacion) {
      setFormData({ ...ubicacion });
    }
  }, [ubicacion]);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prev) => ({ ...prev, [name]: value }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      if (ubicacion) {
        await ubicacionesService.update(ubicacion.id, formData);
      } else {
        await ubicacionesService.create(formData);
      }
      onSuccess();
    } catch (error) {
      alert('Error al guardar la ubicación');
    }
  };

  return (
    <form onSubmit={handleSubmit} className="space-y-4">
      <div className="grid grid-cols-2 gap-4">
        <div>
          <label className="block text-sm font-medium text-gray-700 mb-1">
            Nombre *
          </label>
          <input
            type="text"
            name="nombre"
            value={formData.nombre}
            onChange={handleChange}
            required
            className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
          />
        </div>

        <div>
          <label className="block text-sm font-medium text-gray-700 mb-1">
            Departamento
          </label>
          <input
            type="text"
            name="departamento"
            value={formData.departamento}
            onChange={handleChange}
            className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
          />
        </div>

        <div>
          <label className="block text-sm font-medium text-gray-700 mb-1">
            Edificio
          </label>
          <input
            type="text"
            name="edificio"
            value={formData.edificio}
            onChange={handleChange}
            className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
          />
        </div>

        <div>
          <label className="block text-sm font-medium text-gray-700 mb-1">
            Piso
          </label>
          <input
            type="text"
            name="piso"
            value={formData.piso}
            onChange={handleChange}
            className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
          />
        </div>

        <div>
          <label className="block text-sm font-medium text-gray-700 mb-1">
            Responsable
          </label>
          <input
            type="text"
            name="responsable"
            value={formData.responsable}
            onChange={handleChange}
            className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
          />
        </div>

        <div>
          <label className="block text-sm font-medium text-gray-700 mb-1">
            Teléfono
          </label>
          <input
            type="text"
            name="telefono"
            value={formData.telefono}
            onChange={handleChange}
            className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
          />
        </div>
      </div>

      <div>
        <label className="block text-sm font-medium text-gray-700 mb-1">
          Descripción
        </label>
        <textarea
          name="descripcion"
          value={formData.descripcion}
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
          className="px-4 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700"
        >
          Guardar
        </button>
      </div>
    </form>
  );
}

export default function Ubicaciones() {
  const [ubicaciones, setUbicaciones] = useState([]);
  const [loading, setLoading] = useState(true);
  const [showForm, setShowForm] = useState(false);
  const [selectedUbicacion, setSelectedUbicacion] = useState(null);

  useEffect(() => {
    loadUbicaciones();
  }, []);

  const loadUbicaciones = async () => {
    try {
      const data = await ubicacionesService.getAll();
      setUbicaciones(data);
    } catch (error) {
      console.error('Error al cargar ubicaciones:', error);
    } finally {
      setLoading(false);
    }
  };

  const handleCreate = () => {
    setSelectedUbicacion(null);
    setShowForm(true);
  };

  const handleEdit = (ubicacion, e) => {
    e.stopPropagation();
    setSelectedUbicacion(ubicacion);
    setShowForm(true);
  };

  const handleDelete = async (ubicacion, e) => {
    e.stopPropagation();
    if (window.confirm('¿Está seguro de eliminar esta ubicación?')) {
      try {
        await ubicacionesService.delete(ubicacion.id);
        loadUbicaciones();
      } catch (error) {
        alert('Error al eliminar la ubicación');
      }
    }
  };

  const handleFormSuccess = () => {
    setShowForm(false);
    loadUbicaciones();
  };

  const columns = [
    { key: 'nombre', label: 'Nombre' },
    { key: 'departamento', label: 'Departamento' },
    { key: 'edificio', label: 'Edificio' },
    { key: 'piso', label: 'Piso' },
    { key: 'responsable', label: 'Responsable' },
    {
      key: 'actions',
      label: 'Acciones',
      render: (_, ubicacion) => (
        <div className="flex space-x-2">
          <button
            onClick={(e) => handleEdit(ubicacion, e)}
            className="text-blue-600 hover:text-blue-800"
          >
            <Edit className="w-5 h-5" />
          </button>
          <button
            onClick={(e) => handleDelete(ubicacion, e)}
            className="text-red-600 hover:text-red-800"
          >
            <Trash2 className="w-5 h-5" />
          </button>
        </div>
      ),
    },
  ];

  if (loading) {
    return <div className="text-center py-8">Cargando ubicaciones...</div>;
  }

  return (
    <div className="container mx-auto px-4 py-8">
      <div className="space-y-4">
        <div className="flex justify-between items-center">
          <div>
            <h2 className="text-2xl font-bold text-gray-800">Ubicaciones</h2>
            <p className="text-gray-600">Gestión de ubicaciones físicas</p>
          </div>
          <button
            onClick={handleCreate}
            className="flex items-center px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700"
          >
            <Plus className="w-5 h-5 mr-2" />
            Nueva Ubicación
          </button>
        </div>

        <Table columns={columns} data={ubicaciones} />

        <Modal
          isOpen={showForm}
          onClose={() => setShowForm(false)}
          title={selectedUbicacion ? 'Editar Ubicación' : 'Nueva Ubicación'}
        >
          <UbicacionForm
            ubicacion={selectedUbicacion}
            onSuccess={handleFormSuccess}
            onCancel={() => setShowForm(false)}
          />
        </Modal>
      </div>
    </div>
  );
}
