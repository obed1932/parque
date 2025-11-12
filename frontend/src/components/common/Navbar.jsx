/**
 * Componente de barra de navegación
 */
import { Link } from 'react-router-dom';
import { Monitor } from 'lucide-react';

export default function Navbar() {
  return (
    <nav className="bg-blue-600 text-white shadow-lg">
      <div className="container mx-auto px-4">
        <div className="flex items-center justify-between h-16">
          <Link to="/" className="flex items-center space-x-2">
            <Monitor className="h-8 w-8" />
            <span className="text-xl font-bold">Parque Informático</span>
          </Link>

          <div className="flex space-x-4">
            <Link
              to="/"
              className="px-3 py-2 rounded-md hover:bg-blue-700 transition"
            >
              Dashboard
            </Link>
            <Link
              to="/equipos"
              className="px-3 py-2 rounded-md hover:bg-blue-700 transition"
            >
              Equipos
            </Link>
            <Link
              to="/usuarios"
              className="px-3 py-2 rounded-md hover:bg-blue-700 transition"
            >
              Usuarios
            </Link>
            <Link
              to="/ubicaciones"
              className="px-3 py-2 rounded-md hover:bg-blue-700 transition"
            >
              Ubicaciones
            </Link>
          </div>
        </div>
      </div>
    </nav>
  );
}
