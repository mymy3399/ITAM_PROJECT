"""
Database initialization script.
Creates initial admin user and sample data.
"""
from sqlalchemy.orm import Session
from app.core.config import settings
from app.crud.crud_user import user as crud_user
from app.db.session import SessionLocal
from app.schemas.user import UserCreate


def init_db(db: Session) -> None:
    """
    Initialize database with default data
    """
    # Check if admin user exists
    admin_user = crud_user.get_by_email(db, email="admin@example.com")
    if not admin_user:
        # Create admin user
        user_in = UserCreate(
            email="admin@example.com",
            password="admin123",
            full_name="System Administrator",
            is_superuser=True,
            is_active=True
        )
        admin_user = crud_user.create(db, obj_in=user_in)
        print(f"Created admin user: {admin_user.email}")
    else:
        print("Admin user already exists")


def main():
    """
    Main function to initialize database
    """
    db = SessionLocal()
    try:
        init_db(db)
    finally:
        db.close()


if __name__ == "__main__":
    main()