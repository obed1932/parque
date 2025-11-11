/**
 * Componente para tarjeta de estadísticas
 */
export default function StatsCard({ title, value, icon: Icon, color = 'blue' }) {
  const colorClasses = {
    blue: 'bg-blue-500',
    green: 'bg-green-500',
    yellow: 'bg-yellow-500',
    red: 'bg-red-500',
    purple: 'bg-purple-500',
  };

  return (
    <div className="bg-white rounded-lg shadow-md p-6">
      <div className="flex items-center justify-between">
        <div>
          <p className="text-sm font-medium text-gray-600 uppercase">{title}</p>
          <p className="mt-2 text-3xl font-semibold text-gray-900">{value}</p>
        </div>
        {Icon && (
          <div className={`p-3 rounded-full ${colorClasses[color]} bg-opacity-10`}>
            <Icon className={`w-8 h-8 text-${color}-600`} />
          </div>
        )}
      </div>
    </div>
  );
}
