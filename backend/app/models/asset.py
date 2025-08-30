from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey, Text
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.db.base import Base


class Asset(Base):
    __tablename__ = "assets"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    asset_tag = Column(String, unique=True, index=True, nullable=False)
    category = Column(String, nullable=False)  # e.g., "Computer", "Monitor", "Printer"
    brand = Column(String, nullable=True)
    model = Column(String, nullable=True)
    serial_number = Column(String, unique=True, nullable=True)
    purchase_date = Column(DateTime(timezone=True), nullable=True)
    purchase_price = Column(Float, nullable=True)
    location = Column(String, nullable=True)
    status = Column(String, default="Active")  # Active, Inactive, Disposed, Under Repair
    description = Column(Text, nullable=True)
    ip_address = Column(String, nullable=True)
    mac_address = Column(String, nullable=True)
    operating_system = Column(String, nullable=True)
    assigned_user_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # Relationship
    assigned_user = relationship("User", back_populates="assets")


# Add back_populates to User model
from app.models.user import User
User.assets = relationship("Asset", back_populates="assigned_user")