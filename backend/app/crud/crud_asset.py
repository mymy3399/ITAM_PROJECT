from sqlalchemy.orm import Session
from typing import List, Optional
from app.models.asset import Asset
from app.schemas.asset import AssetCreate, AssetUpdate


class CRUDAsset:
    def get(self, db: Session, id: int) -> Optional[Asset]:
        return db.query(Asset).filter(Asset.id == id).first()
    
    def get_by_asset_tag(self, db: Session, *, asset_tag: str) -> Optional[Asset]:
        return db.query(Asset).filter(Asset.asset_tag == asset_tag).first()
    
    def get_multi(self, db: Session, *, skip: int = 0, limit: int = 100) -> List[Asset]:
        return db.query(Asset).offset(skip).limit(limit).all()
    
    def get_by_category(self, db: Session, *, category: str, skip: int = 0, limit: int = 100) -> List[Asset]:
        return db.query(Asset).filter(Asset.category == category).offset(skip).limit(limit).all()
    
    def create(self, db: Session, *, obj_in: AssetCreate) -> Asset:
        db_obj = Asset(**obj_in.dict())
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj
    
    def update(self, db: Session, *, db_obj: Asset, obj_in: AssetUpdate) -> Asset:
        update_data = obj_in.dict(exclude_unset=True)
        for field, value in update_data.items():
            setattr(db_obj, field, value)
        
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj
    
    def remove(self, db: Session, *, id: int) -> Asset:
        obj = db.query(Asset).get(id)
        db.delete(obj)
        db.commit()
        return obj


asset = CRUDAsset()