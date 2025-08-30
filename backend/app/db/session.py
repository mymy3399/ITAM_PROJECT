from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

# สร้าง engine สำหรับเชื่อมต่อกับ Database
# pool_pre_ping=True เพื่อตรวจสอบ connection ก่อนใช้งาน
engine = create_engine(settings.DATABASE_URL, pool_pre_ping=True)

# สร้าง SessionLocal class สำหรับสร้าง database session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)