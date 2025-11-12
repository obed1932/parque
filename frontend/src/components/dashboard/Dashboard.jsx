/**
 * Componente Dashboard principal
 */
import { useEffect, useState } from 'react';
import { Monitor, MapPin, Users, Wrench } from 'lucide-react';
import StatsCard from './StatsCard';
import { statsService } from '../../services/stats';

export default function Dashboard() {
  const [stats, setStats] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    loadStats();
  }, []);

  const loadStats = async () => {
    try {
      const data = await statsService.getDashboard();
      setStats(data);
    } catch (error) {
      console.error('Error al cargar estadísticas:', error);
    } finally {
      setLoading(false);
    }
  };

  if (loading) {
    return (
      <div className="flex items-center justify-center h-64">
        <div className="text-xl text-gray-600">Cargando estadísticas...</div>
      </div>
    );
  }

  if (!stats) {
    return (
      <div className="flex items-center justify-center h-64">
        <div className="text-xl text-red-600">Error al cargar estadísticas</div>
      </div>
    );
  }

  return (
    <div className="space-y-6">
      <div>
        <h2 className="text-2xl font-bold text-gray-800">Dashboard</h2>
        <p className="text-gray-600">Resumen del parque informático</p>
      </div>

      {/* Tarjetas de estadísticas principales */}
      <div className="grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-4">
        <StatsCard
          title="Total Equipos"
          value={stats.total_equipos}
          icon={Monitor}
          color="blue"
        />
        <StatsCard
          title="Ubicaciones"
          value={stats.total_ubicaciones}
          icon={MapPin}
          color="green"
        />
        <StatsCard
          title="Usuarios Activos"
          value={stats.usuarios_activos}
          icon={Users}
          color="purple"
        />
        <StatsCard
          title="Mantenimientos"
          value={stats.total_mantenimientos}
          icon={Wrench}
          color="yellow"
        />
      </div>

      {/* Equipos por estado */}
      <div className="bg-white rounded-lg shadow-md p-6">
        <h3 className="text-lg font-semibold text-gray-800 mb-4">
          Equipos por Estado
        </h3>
        <div className="space-y-3">
          {stats.equipos_por_estado.map((item) => (
            <div key={item.estado} className="flex items-center justify-between">
              <span className="text-gray-700">{item.estado}</span>
              <span className="font-semibold text-gray-900">{item.cantidad}</span>
            </div>
          ))}
        </div>
      </div>

      {/* Equipos por tipo */}
      <div className="bg-white rounded-lg shadow-md p-6">
        <h3 className="text-lg font-semibold text-gray-800 mb-4">
          Equipos por Tipo
        </h3>
        <div className="space-y-3">
          {stats.equipos_por_tipo.map((item) => (
            <div key={item.tipo} className="flex items-center justify-between">
              <span className="text-gray-700">{item.tipo}</span>
              <span className="font-semibold text-gray-900">{item.cantidad}</span>
            </div>
          ))}
        </div>
      </div>

      {/* Costos de mantenimiento */}
      <div className="bg-white rounded-lg shadow-md p-6">
        <h3 className="text-lg font-semibold text-gray-800 mb-4">
          Costos de Mantenimiento
        </h3>
        <p className="text-3xl font-bold text-blue-600">
          ${stats.costo_total_mantenimientos.toFixed(2)}
        </p>
        <p className="text-sm text-gray-600 mt-1">Total acumulado</p>
      </div>
    </div>
  );
}
