/**
 * Servicio para gestión de usuarios
 */
import api from './api';

export const usuariosService = {
  getAll: async (params = {}) => {
    const response = await api.get('/usuarios', { params });
    return response.data;
  },

  getById: async (id) => {
    const response = await api.get(`/usuarios/${id}`);
    return response.data;
  },

  create: async (data) => {
    const response = await api.post('/usuarios', data);
    return response.data;
  },

  update: async (id, data) => {
    const response = await api.put(`/usuarios/${id}`, data);
    return response.data;
  },

  delete: async (id) => {
    await api.delete(`/usuarios/${id}`);
  },
};
