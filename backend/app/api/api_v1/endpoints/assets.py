from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api import deps
from app.crud.crud_asset import asset as crud_asset
from app.schemas.asset import Asset, AssetCreate, AssetUpdate
from app.models.user import User as UserModel

router = APIRouter()


@router.get("/", response_model=List[Asset])
def read_assets(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: UserModel = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve assets.
    """
    assets = crud_asset.get_multi(db, skip=skip, limit=limit)
    return assets


@router.post("/", response_model=Asset)
def create_asset(
    *,
    db: Session = Depends(deps.get_db),
    asset_in: AssetCreate,
    current_user: UserModel = Depends(deps.get_current_active_user),
) -> Any:
    """
    Create new asset.
    """
    asset = crud_asset.get_by_asset_tag(db, asset_tag=asset_in.asset_tag)
    if asset:
        raise HTTPException(
            status_code=400,
            detail="The asset with this asset tag already exists in the system.",
        )
    asset = crud_asset.create(db, obj_in=asset_in)
    return asset


@router.get("/{id}", response_model=Asset)
def read_asset(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: UserModel = Depends(deps.get_current_active_user),
) -> Any:
    """
    Get asset by ID.
    """
    asset = crud_asset.get(db, id=id)
    if not asset:
        raise HTTPException(status_code=404, detail="Asset not found")
    return asset


@router.put("/{id}", response_model=Asset)
def update_asset(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    asset_in: AssetUpdate,
    current_user: UserModel = Depends(deps.get_current_active_user),
) -> Any:
    """
    Update an asset.
    """
    asset = crud_asset.get(db, id=id)
    if not asset:
        raise HTTPException(status_code=404, detail="Asset not found")
    asset = crud_asset.update(db, db_obj=asset, obj_in=asset_in)
    return asset


@router.delete("/{id}", response_model=Asset)
def delete_asset(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: UserModel = Depends(deps.get_current_active_user),
) -> Any:
    """
    Delete an asset.
    """
    asset = crud_asset.get(db, id=id)
    if not asset:
        raise HTTPException(status_code=404, detail="Asset not found")
    asset = crud_asset.remove(db, id=id)
    return asset


@router.get("/category/{category}", response_model=List[Asset])
def read_assets_by_category(
    *,
    db: Session = Depends(deps.get_db),
    category: str,
    skip: int = 0,
    limit: int = 100,
    current_user: UserModel = Depends(deps.get_current_active_user),
) -> Any:
    """
    Get assets by category.
    """
    assets = crud_asset.get_by_category(db, category=category, skip=skip, limit=limit)
    return assets