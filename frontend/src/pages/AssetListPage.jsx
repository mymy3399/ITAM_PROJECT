import React from 'react'
import AssetTable from '../components/AssetTable'

const AssetListPage = () => {
  return (
    <div className="asset-list-page">
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '2rem' }}>
        <h1 style={{ color: '#333', fontSize: '2rem', margin: 0 }}>
          IT Assets
        </h1>
        <button className="btn btn-primary">
          Add New Asset
        </button>
      </div>

      <div className="filters" style={{ marginBottom: '1.5rem' }}>
        <div style={{ display: 'flex', gap: '1rem', alignItems: 'center' }}>
          <div className="form-group" style={{ margin: 0, minWidth: '150px' }}>
            <select className="form-control">
              <option value="">All Categories</option>
              <option value="Computer">Computer</option>
              <option value="Monitor">Monitor</option>
              <option value="Printer">Printer</option>
              <option value="Network">Network Equipment</option>
            </select>
          </div>
          <div className="form-group" style={{ margin: 0, minWidth: '150px' }}>
            <select className="form-control">
              <option value="">All Status</option>
              <option value="Active">Active</option>
              <option value="Inactive">Inactive</option>
              <option value="Under Repair">Under Repair</option>
              <option value="Disposed">Disposed</option>
            </select>
          </div>
          <div className="form-group" style={{ margin: 0, flex: 1 }}>
            <input 
              type="text" 
              className="form-control" 
              placeholder="Search assets..."
            />
          </div>
        </div>
      </div>

      <div className="card">
        <AssetTable />
      </div>
    </div>
  )
}

export default AssetListPage