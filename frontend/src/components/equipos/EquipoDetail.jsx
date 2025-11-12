/**
 * Componente para mostrar detalles completos de un equipo
 */
import { useEffect, useState } from 'react';
import { equiposService } from '../../services/equipos';

export default function EquipoDetail({ equipoId }) {
  const [equipo, setEquipo] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    loadEquipo();
  }, [equipoId]);

  const loadEquipo = async () => {
    try {
      const data = await equiposService.getById(equipoId);
      setEquipo(data);
    } catch (error) {
      console.error('Error al cargar equipo:', error);
    } finally {
      setLoading(false);
    }
  };

  if (loading) {
    return <div className="text-center py-4">Cargando...</div>;
  }

  if (!equipo) {
    return <div className="text-center py-4 text-red-600">Error al cargar el equipo</div>;
  }

  return (
    <div className="space-y-6">
      {/* Información General */}
      <div>
        <h3 className="text-lg font-semibold text-gray-800 mb-3">Información General</h3>
        <div className="grid grid-cols-2 gap-4">
          <div>
            <span className="text-sm text-gray-600">Código:</span>
            <p className="font-medium">{equipo.codigo_inventario}</p>
          </div>
          <div>
            <span className="text-sm text-gray-600">Nombre:</span>
            <p className="font-medium">{equipo.nombre_equipo || 'N/A'}</p>
          </div>
          <div>
            <span className="text-sm text-gray-600">Tipo:</span>
            <p className="font-medium">{equipo.tipo_equipo}</p>
          </div>
          <div>
            <span className="text-sm text-gray-600">Estado:</span>
            <p className="font-medium">{equipo.estado}</p>
          </div>
          <div>
            <span className="text-sm text-gray-600">Marca:</span>
            <p className="font-medium">{equipo.marca || 'N/A'}</p>
          </div>
          <div>
            <span className="text-sm text-gray-600">Modelo:</span>
            <p className="font-medium">{equipo.modelo || 'N/A'}</p>
          </div>
          <div>
            <span className="text-sm text-gray-600">Sistema Operativo:</span>
            <p className="font-medium">{equipo.sistema_operativo || 'N/A'}</p>
          </div>
          <div>
            <span className="text-sm text-gray-600">Número de Serie:</span>
            <p className="font-medium">{equipo.numero_serie || 'N/A'}</p>
          </div>
        </div>
      </div>

      {/* Hardware */}
      {equipo.procesadores && equipo.procesadores.length > 0 && (
        <div>
          <h3 className="text-lg font-semibold text-gray-800 mb-3">Procesador</h3>
          {equipo.procesadores.map((proc) => (
            <div key={proc.id} className="bg-gray-50 p-3 rounded">
              <p><strong>Marca:</strong> {proc.marca}</p>
              <p><strong>Modelo:</strong> {proc.modelo}</p>
              <p><strong>Núcleos/Hilos:</strong> {proc.nucleos}/{proc.hilos}</p>
              <p><strong>Frecuencia:</strong> {proc.frecuencia_base}</p>
            </div>
          ))}
        </div>
      )}

      {equipo.memorias_ram && equipo.memorias_ram.length > 0 && (
        <div>
          <h3 className="text-lg font-semibold text-gray-800 mb-3">Memoria RAM</h3>
          {equipo.memorias_ram.map((ram) => (
            <div key={ram.id} className="bg-gray-50 p-3 rounded">
              <p><strong>Tipo:</strong> {ram.tipo}</p>
              <p><strong>Capacidad:</strong> {ram.capacidad_gb} GB</p>
              <p><strong>Velocidad:</strong> {ram.velocidad_mhz} MHz</p>
              <p><strong>Marca:</strong> {ram.marca}</p>
            </div>
          ))}
        </div>
      )}

      {equipo.almacenamientos && equipo.almacenamientos.length > 0 && (
        <div>
          <h3 className="text-lg font-semibold text-gray-800 mb-3">Almacenamiento</h3>
          {equipo.almacenamientos.map((storage) => (
            <div key={storage.id} className="bg-gray-50 p-3 rounded mb-2">
              <p><strong>Tipo:</strong> {storage.tipo}</p>
              <p><strong>Capacidad:</strong> {storage.capacidad_gb} GB</p>
              <p><strong>Marca:</strong> {storage.marca}</p>
              <p><strong>Modelo:</strong> {storage.modelo}</p>
              {storage.es_principal && (
                <span className="text-xs bg-blue-100 text-blue-800 px-2 py-1 rounded">
                  Principal
                </span>
              )}
            </div>
          ))}
        </div>
      )}

      {equipo.tarjetas_graficas && equipo.tarjetas_graficas.length > 0 && (
        <div>
          <h3 className="text-lg font-semibold text-gray-800 mb-3">Tarjeta Gráfica</h3>
          {equipo.tarjetas_graficas.map((gpu) => (
            <div key={gpu.id} className="bg-gray-50 p-3 rounded">
              <p><strong>Tipo:</strong> {gpu.tipo}</p>
              <p><strong>Marca:</strong> {gpu.marca}</p>
              <p><strong>Modelo:</strong> {gpu.modelo}</p>
              <p><strong>Memoria:</strong> {gpu.memoria_gb} GB</p>
            </div>
          ))}
        </div>
      )}

      {equipo.observaciones && (
        <div>
          <h3 className="text-lg font-semibold text-gray-800 mb-3">Observaciones</h3>
          <p className="text-gray-700">{equipo.observaciones}</p>
        </div>
      )}
    </div>
  );
}
