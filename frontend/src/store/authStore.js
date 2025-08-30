import { create } from 'zustand'
import { persist } from 'zustand/middleware'
import apiClient from '../services/apiClient'

export const useAuthStore = create(
  persist(
    (set, get) => ({
      user: null,
      token: null,
      isAuthenticated: false,

      login: async (email, password) => {
        try {
          const formData = new FormData()
          formData.append('username', email)
          formData.append('password', password)

          const response = await apiClient.post('/auth/login', formData, {
            headers: {
              'Content-Type': 'application/x-www-form-urlencoded',
            },
          })

          const { access_token, token_type } = response.data

          // Store token
          localStorage.setItem('access_token', access_token)

          // Get user info
          const userResponse = await apiClient.get('/auth/test-token', {
            headers: {
              Authorization: `Bearer ${access_token}`,
            },
          })

          const user = userResponse.data

          set({
            user,
            token: access_token,
            isAuthenticated: true,
          })

          return { user, token: access_token }
        } catch (error) {
          const message = error.response?.data?.detail || 'Login failed'
          throw new Error(message)
        }
      },

      logout: () => {
        localStorage.removeItem('access_token')
        localStorage.removeItem('user')
        set({
          user: null,
          token: null,
          isAuthenticated: false,
        })
      },

      checkAuth: async () => {
        const token = localStorage.getItem('access_token')
        if (!token) {
          set({ isAuthenticated: false })
          return
        }

        try {
          const response = await apiClient.get('/auth/test-token', {
            headers: {
              Authorization: `Bearer ${token}`,
            },
          })

          const user = response.data

          set({
            user,
            token,
            isAuthenticated: true,
          })
        } catch (error) {
          // Token is invalid
          localStorage.removeItem('access_token')
          localStorage.removeItem('user')
          set({
            user: null,
            token: null,
            isAuthenticated: false,
          })
        }
      },
    }),
    {
      name: 'auth-storage',
      partialize: (state) => ({
        user: state.user,
        token: state.token,
        isAuthenticated: state.isAuthenticated,
      }),
    }
  )
)