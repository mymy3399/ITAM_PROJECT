from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class AssetBase(BaseModel):
    name: str
    asset_tag: str
    category: str
    brand: Optional[str] = None
    model: Optional[str] = None
    serial_number: Optional[str] = None
    purchase_date: Optional[datetime] = None
    purchase_price: Optional[float] = None
    location: Optional[str] = None
    status: str = "Active"
    description: Optional[str] = None
    ip_address: Optional[str] = None
    mac_address: Optional[str] = None
    operating_system: Optional[str] = None
    assigned_user_id: Optional[int] = None


class AssetCreate(AssetBase):
    pass


class AssetUpdate(AssetBase):
    name: Optional[str] = None
    asset_tag: Optional[str] = None
    category: Optional[str] = None


class AssetInDBBase(AssetBase):
    id: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True


class Asset(AssetInDBBase):
    pass


class AssetInDB(AssetInDBBase):
    pass