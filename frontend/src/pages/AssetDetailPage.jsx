import React, { useState, useEffect } from 'react'
import { useParams, useNavigate } from 'react-router-dom'
import { assetService } from '../services/assetService'

const AssetDetailPage = () => {
  const { id } = useParams()
  const navigate = useNavigate()
  const [asset, setAsset] = useState(null)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)

  useEffect(() => {
    fetchAsset()
  }, [id])

  const fetchAsset = async () => {
    try {
      setLoading(true)
      const data = await assetService.getAsset(id)
      setAsset(data)
    } catch (err) {
      setError('Failed to load asset details')
      console.error('Error fetching asset:', err)
    } finally {
      setLoading(false)
    }
  }

  if (loading) {
    return <div>Loading asset details...</div>
  }

  if (error) {
    return (
      <div>
        <p>Error: {error}</p>
        <button className="btn btn-primary" onClick={() => navigate('/assets')}>
          Back to Assets
        </button>
      </div>
    )
  }

  if (!asset) {
    return (
      <div>
        <p>Asset not found</p>
        <button className="btn btn-primary" onClick={() => navigate('/assets')}>
          Back to Assets
        </button>
      </div>
    )
  }

  return (
    <div className="asset-detail-page">
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '2rem' }}>
        <h1 style={{ color: '#333', fontSize: '2rem', margin: 0 }}>
          Asset Details
        </h1>
        <div>
          <button 
            className="btn btn-secondary" 
            style={{ marginRight: '1rem' }}
            onClick={() => navigate('/assets')}
          >
            Back to Assets
          </button>
          <button className="btn btn-primary">
            Edit Asset
          </button>
        </div>
      </div>

      <div className="card">
        <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '2rem' }}>
          <div>
            <h3 style={{ marginBottom: '1rem', color: '#333' }}>Basic Information</h3>
            <div className="form-group">
              <label><strong>Asset Tag:</strong></label>
              <p>{asset.asset_tag}</p>
            </div>
            <div className="form-group">
              <label><strong>Name:</strong></label>
              <p>{asset.name}</p>
            </div>
            <div className="form-group">
              <label><strong>Category:</strong></label>
              <p>{asset.category}</p>
            </div>
            <div className="form-group">
              <label><strong>Brand:</strong></label>
              <p>{asset.brand || 'N/A'}</p>
            </div>
            <div className="form-group">
              <label><strong>Model:</strong></label>
              <p>{asset.model || 'N/A'}</p>
            </div>
            <div className="form-group">
              <label><strong>Serial Number:</strong></label>
              <p>{asset.serial_number || 'N/A'}</p>
            </div>
          </div>
          
          <div>
            <h3 style={{ marginBottom: '1rem', color: '#333' }}>Status & Location</h3>
            <div className="form-group">
              <label><strong>Status:</strong></label>
              <span 
                style={{
                  padding: '4px 12px',
                  borderRadius: '4px',
                  fontSize: '14px',
                  backgroundColor: asset.status === 'Active' ? '#d4edda' : '#fff3cd',
                  color: asset.status === 'Active' ? '#155724' : '#856404'
                }}
              >
                {asset.status}
              </span>
            </div>
            <div className="form-group">
              <label><strong>Location:</strong></label>
              <p>{asset.location || 'N/A'}</p>
            </div>
            <div className="form-group">
              <label><strong>Purchase Date:</strong></label>
              <p>{asset.purchase_date ? new Date(asset.purchase_date).toLocaleDateString() : 'N/A'}</p>
            </div>
            <div className="form-group">
              <label><strong>Purchase Price:</strong></label>
              <p>{asset.purchase_price ? `$${asset.purchase_price.toFixed(2)}` : 'N/A'}</p>
            </div>
          </div>
        </div>
        
        {asset.description && (
          <div style={{ marginTop: '2rem' }}>
            <h3 style={{ marginBottom: '1rem', color: '#333' }}>Description</h3>
            <p style={{ backgroundColor: '#f8f9fa', padding: '1rem', borderRadius: '4px' }}>
              {asset.description}
            </p>
          </div>
        )}

        {(asset.ip_address || asset.mac_address || asset.operating_system) && (
          <div style={{ marginTop: '2rem' }}>
            <h3 style={{ marginBottom: '1rem', color: '#333' }}>Technical Information</h3>
            <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr 1fr', gap: '1rem' }}>
              {asset.ip_address && (
                <div className="form-group">
                  <label><strong>IP Address:</strong></label>
                  <p>{asset.ip_address}</p>
                </div>
              )}
              {asset.mac_address && (
                <div className="form-group">
                  <label><strong>MAC Address:</strong></label>
                  <p>{asset.mac_address}</p>
                </div>
              )}
              {asset.operating_system && (
                <div className="form-group">
                  <label><strong>Operating System:</strong></label>
                  <p>{asset.operating_system}</p>
                </div>
              )}
            </div>
          </div>
        )}
      </div>
    </div>
  )
}

export default AssetDetailPage