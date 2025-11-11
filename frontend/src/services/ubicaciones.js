/**
 * Servicio para gestión de ubicaciones
 */
import api from './api';

export const ubicacionesService = {
  getAll: async (params = {}) => {
    const response = await api.get('/ubicaciones', { params });
    return response.data;
  },

  getById: async (id) => {
    const response = await api.get(`/ubicaciones/${id}`);
    return response.data;
  },

  create: async (data) => {
    const response = await api.post('/ubicaciones', data);
    return response.data;
  },

  update: async (id, data) => {
    const response = await api.put(`/ubicaciones/${id}`, data);
    return response.data;
  },

  delete: async (id) => {
    await api.delete(`/ubicaciones/${id}`);
  },
};
