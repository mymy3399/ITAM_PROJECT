import React, { useState, useEffect } from 'react'
import { assetService } from '../services/assetService'

const AssetTable = () => {
  const [assets, setAssets] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)

  useEffect(() => {
    fetchAssets()
  }, [])

  const fetchAssets = async () => {
    try {
      setLoading(true)
      const data = await assetService.getAssets()
      setAssets(data)
    } catch (err) {
      setError('Failed to load assets')
      console.error('Error fetching assets:', err)
    } finally {
      setLoading(false)
    }
  }

  if (loading) {
    return <div>Loading assets...</div>
  }

  if (error) {
    return <div>Error: {error}</div>
  }

  return (
    <div className="asset-table">
      <table className="table">
        <thead>
          <tr>
            <th>Asset Tag</th>
            <th>Name</th>
            <th>Category</th>
            <th>Brand</th>
            <th>Model</th>
            <th>Status</th>
            <th>Location</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          {assets.map((asset) => (
            <tr key={asset.id}>
              <td>{asset.asset_tag}</td>
              <td>{asset.name}</td>
              <td>{asset.category}</td>
              <td>{asset.brand || 'N/A'}</td>
              <td>{asset.model || 'N/A'}</td>
              <td>
                <span 
                  className={`status ${asset.status?.toLowerCase()}`}
                  style={{
                    padding: '4px 8px',
                    borderRadius: '4px',
                    fontSize: '12px',
                    backgroundColor: asset.status === 'Active' ? '#d4edda' : '#fff3cd',
                    color: asset.status === 'Active' ? '#155724' : '#856404'
                  }}
                >
                  {asset.status}
                </span>
              </td>
              <td>{asset.location || 'N/A'}</td>
              <td>
                <button 
                  className="btn btn-primary" 
                  style={{ marginRight: '8px', fontSize: '12px', padding: '4px 8px' }}
                  onClick={() => window.location.href = `/assets/${asset.id}`}
                >
                  View
                </button>
                <button 
                  className="btn btn-secondary"
                  style={{ fontSize: '12px', padding: '4px 8px' }}
                >
                  Edit
                </button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
      {assets.length === 0 && (
        <div style={{ textAlign: 'center', padding: '2rem', color: '#666' }}>
          No assets found
        </div>
      )}
    </div>
  )
}

export default AssetTable