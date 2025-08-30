import apiClient from './apiClient'

export const assetService = {
  // Get all assets
  async getAssets(params = {}) {
    try {
      const response = await apiClient.get('/assets', { params })
      return response.data
    } catch (error) {
      throw new Error(error.response?.data?.detail || 'Failed to fetch assets')
    }
  },

  // Get single asset by ID
  async getAsset(id) {
    try {
      const response = await apiClient.get(`/assets/${id}`)
      return response.data
    } catch (error) {
      throw new Error(error.response?.data?.detail || 'Failed to fetch asset')
    }
  },

  // Create new asset
  async createAsset(assetData) {
    try {
      const response = await apiClient.post('/assets', assetData)
      return response.data
    } catch (error) {
      throw new Error(error.response?.data?.detail || 'Failed to create asset')
    }
  },

  // Update asset
  async updateAsset(id, assetData) {
    try {
      const response = await apiClient.put(`/assets/${id}`, assetData)
      return response.data
    } catch (error) {
      throw new Error(error.response?.data?.detail || 'Failed to update asset')
    }
  },

  // Delete asset
  async deleteAsset(id) {
    try {
      const response = await apiClient.delete(`/assets/${id}`)
      return response.data
    } catch (error) {
      throw new Error(error.response?.data?.detail || 'Failed to delete asset')
    }
  },

  // Get assets by category
  async getAssetsByCategory(category, params = {}) {
    try {
      const response = await apiClient.get(`/assets/category/${category}`, { params })
      return response.data
    } catch (error) {
      throw new Error(error.response?.data?.detail || 'Failed to fetch assets by category')
    }
  }
}