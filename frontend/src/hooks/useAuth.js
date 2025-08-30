import { useState, useEffect } from 'react'
import { useAuthStore } from '../store/authStore'

export const useAuth = () => {
  const { user, isAuthenticated, login, logout, checkAuth } = useAuthStore()
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    const initAuth = async () => {
      try {
        await checkAuth()
      } catch (error) {
        console.error('Auth check failed:', error)
      } finally {
        setLoading(false)
      }
    }

    initAuth()
  }, [checkAuth])

  return {
    user,
    isAuthenticated,
    loading,
    login,
    logout
  }
}