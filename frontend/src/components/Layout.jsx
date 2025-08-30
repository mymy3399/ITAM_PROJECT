import React from 'react'
import { Outlet, Link } from 'react-router-dom'
import { useAuthStore } from '../store/authStore'

const Layout = () => {
  const { user, logout } = useAuthStore()

  const handleLogout = () => {
    logout()
  }

  return (
    <div className="layout">
      <nav className="navbar" style={{ 
        background: '#007bff', 
        color: 'white', 
        padding: '1rem 2rem',
        display: 'flex',
        justifyContent: 'space-between',
        alignItems: 'center'
      }}>
        <div className="nav-brand">
          <Link to="/" style={{ color: 'white', textDecoration: 'none', fontSize: '1.5rem', fontWeight: 'bold' }}>
            U-ITAM
          </Link>
        </div>
        <div className="nav-links">
          <Link to="/assets" style={{ color: 'white', textDecoration: 'none', marginRight: '1rem' }}>
            Assets
          </Link>
          <span style={{ marginRight: '1rem' }}>Welcome, {user?.full_name || user?.email}</span>
          <button 
            onClick={handleLogout} 
            className="btn btn-secondary"
            style={{ background: 'rgba(255,255,255,0.2)', border: 'none' }}
          >
            Logout
          </button>
        </div>
      </nav>
      <main className="main-content" style={{ flex: 1, padding: '2rem' }}>
        <div className="container">
          <Outlet />
        </div>
      </main>
    </div>
  )
}

export default Layout