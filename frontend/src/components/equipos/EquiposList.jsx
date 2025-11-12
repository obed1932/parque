/**
 * Componente para listar equipos
 */
import { useEffect, useState } from 'react';
import { Plus, Trash2, Edit } from 'lucide-react';
import Table from '../common/Table';
import Modal from '../common/Modal';
import EquipoForm from './EquipoForm';
import EquipoDetail from './EquipoDetail';
import { equiposService } from '../../services/equipos';

export default function EquiposList() {
  const [equipos, setEquipos] = useState([]);
  const [loading, setLoading] = useState(true);
  const [showForm, setShowForm] = useState(false);
  const [showDetail, setShowDetail] = useState(false);
  const [selectedEquipo, setSelectedEquipo] = useState(null);

  useEffect(() => {
    loadEquipos();
  }, []);

  const loadEquipos = async () => {
    try {
      const data = await equiposService.getAll();
      setEquipos(data);
    } catch (error) {
      console.error('Error al cargar equipos:', error);
    } finally {
      setLoading(false);
    }
  };

  const handleCreate = () => {
    setSelectedEquipo(null);
    setShowForm(true);
  };

  const handleEdit = (equipo, e) => {
    e.stopPropagation();
    setSelectedEquipo(equipo);
    setShowForm(true);
  };

  const handleDelete = async (equipo, e) => {
    e.stopPropagation();
    if (window.confirm('¿Está seguro de eliminar este equipo?')) {
      try {
        await equiposService.delete(equipo.id);
        loadEquipos();
      } catch (error) {
        alert('Error al eliminar el equipo');
      }
    }
  };

  const handleRowClick = (equipo) => {
    setSelectedEquipo(equipo);
    setShowDetail(true);
  };

  const handleFormSuccess = () => {
    setShowForm(false);
    loadEquipos();
  };

  const columns = [
    { key: 'codigo_inventario', label: 'Código' },
    { key: 'nombre_equipo', label: 'Nombre' },
    { key: 'tipo_equipo', label: 'Tipo' },
    { key: 'marca', label: 'Marca' },
    { key: 'modelo', label: 'Modelo' },
    {
      key: 'estado',
      label: 'Estado',
      render: (value) => (
        <span className={`px-2 py-1 text-xs rounded ${
          value === 'Operativo' ? 'bg-green-100 text-green-800' :
          value === 'En reparación' ? 'bg-yellow-100 text-yellow-800' :
          'bg-red-100 text-red-800'
        }`}>
          {value}
        </span>
      ),
    },
    {
      key: 'actions',
      label: 'Acciones',
      render: (_, equipo) => (
        <div className="flex space-x-2">
          <button
            onClick={(e) => handleEdit(equipo, e)}
            className="text-blue-600 hover:text-blue-800"
          >
            <Edit className="w-5 h-5" />
          </button>
          <button
            onClick={(e) => handleDelete(equipo, e)}
            className="text-red-600 hover:text-red-800"
          >
            <Trash2 className="w-5 h-5" />
          </button>
        </div>
      ),
    },
  ];

  if (loading) {
    return <div className="text-center py-8">Cargando equipos...</div>;
  }

  return (
    <div className="space-y-4">
      <div className="flex justify-between items-center">
        <div>
          <h2 className="text-2xl font-bold text-gray-800">Equipos</h2>
          <p className="text-gray-600">Gestión de equipos informáticos</p>
        </div>
        <button
          onClick={handleCreate}
          className="flex items-center px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700"
        >
          <Plus className="w-5 h-5 mr-2" />
          Nuevo Equipo
        </button>
      </div>

      <Table columns={columns} data={equipos} onRowClick={handleRowClick} />

      <Modal
        isOpen={showForm}
        onClose={() => setShowForm(false)}
        title={selectedEquipo ? 'Editar Equipo' : 'Nuevo Equipo'}
        size="lg"
      >
        <EquipoForm
          equipo={selectedEquipo}
          onSuccess={handleFormSuccess}
          onCancel={() => setShowForm(false)}
        />
      </Modal>

      <Modal
        isOpen={showDetail}
        onClose={() => setShowDetail(false)}
        title="Detalle del Equipo"
        size="xl"
      >
        {selectedEquipo && <EquipoDetail equipoId={selectedEquipo.id} />}
      </Modal>
    </div>
  );
}
