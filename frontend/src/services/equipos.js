/**
 * Servicio para gestión de equipos
 */
import api from './api';

export const equiposService = {
  // Obtener todos los equipos
  getAll: async (params = {}) => {
    const response = await api.get('/equipos', { params });
    return response.data;
  },

  // Obtener un equipo por ID
  getById: async (id) => {
    const response = await api.get(`/equipos/${id}`);
    return response.data;
  },

  // Crear nuevo equipo
  create: async (data) => {
    const response = await api.post('/equipos', data);
    return response.data;
  },

  // Actualizar equipo
  update: async (id, data) => {
    const response = await api.put(`/equipos/${id}`, data);
    return response.data;
  },

  // Eliminar equipo
  delete: async (id) => {
    await api.delete(`/equipos/${id}`);
  },

  // Buscar por código
  getByCodigo: async (codigo) => {
    const response = await api.get(`/equipos/codigo/${codigo}`);
    return response.data;
  },
};
