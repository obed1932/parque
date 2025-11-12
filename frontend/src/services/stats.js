/**
 * Servicio para obtener estadísticas
 */
import api from './api';

export const statsService = {
  getDashboard: async () => {
    const response = await api.get('/stats/dashboard');
    return response.data;
  },

  getEquiposPorUbicacion: async () => {
    const response = await api.get('/stats/equipos-por-ubicacion');
    return response.data;
  },

  getEquiposAsignados: async () => {
    const response = await api.get('/stats/equipos-asignados');
    return response.data;
  },
};
