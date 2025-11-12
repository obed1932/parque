/**
 * Componente principal de la aplicación
 */
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Navbar from './components/common/Navbar';
import Home from './pages/Home';
import Equipos from './pages/Equipos';
import Usuarios from './pages/Usuarios';
import Ubicaciones from './pages/Ubicaciones';

function App() {
  return (
    <Router>
      <div className="min-h-screen bg-gray-50">
        <Navbar />
        <main>
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/equipos" element={<Equipos />} />
            <Route path="/usuarios" element={<Usuarios />} />
            <Route path="/ubicaciones" element={<Ubicaciones />} />
          </Routes>
        </main>
      </div>
    </Router>
  );
}

export default App;
