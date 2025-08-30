from typing import Generator
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from app.core.config import settings
from app.crud.crud_user import user as crud_user
from app.db.session import SessionLocal
from app.models.user import User
from app.security import verify_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl=f"/api/v1/auth/login")


def get_db() -> Generator:
    """
    สร้าง database session สำหรับใช้ใน API endpoints
    """
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


def get_current_user(
    db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)
) -> User:
    """
    ตรวจสอบ token และคืนค่า current user
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    email = verify_token(token)
    if email is None:
        raise credentials_exception
    
    user = crud_user.get_by_email(db, email=email)
    if user is None:
        raise credentials_exception
    
    return user


def get_current_active_user(current_user: User = Depends(get_current_user)) -> User:
    """
    ตรวจสอบว่า current user เป็น active user หรือไม่
    """
    if not current_user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


def get_current_active_superuser(
    current_user: User = Depends(get_current_user),
) -> User:
    """
    ตรวจสอบว่า current user เป็น superuser หรือไม่
    """
    if not current_user.is_superuser:
        raise HTTPException(
            status_code=400, detail="The user doesn't have enough privileges"
        )
    return current_user