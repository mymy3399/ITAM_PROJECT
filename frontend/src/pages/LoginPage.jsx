import React from 'react'
import LoginForm from '../components/LoginForm'

const LoginPage = () => {
  return (
    <div className="login-page" style={{
      minHeight: '100vh',
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'center',
      background: 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)'
    }}>
      <div style={{
        background: 'white',
        borderRadius: '10px',
        padding: '2rem',
        boxShadow: '0 10px 25px rgba(0,0,0,0.1)',
        width: '100%',
        maxWidth: '450px'
      }}>
        <div style={{ textAlign: 'center', marginBottom: '2rem' }}>
          <h1 style={{ color: '#333', fontSize: '2rem', fontWeight: 'bold' }}>
            U-ITAM
          </h1>
          <p style={{ color: '#666', margin: '0.5rem 0' }}>
            Unified IT Asset Management System
          </p>
        </div>
        <LoginForm />
      </div>
    </div>
  )
}

export default LoginPage