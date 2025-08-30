from sqlalchemy.orm import declarative_base

# สร้าง Base class สำหรับ SQLAlchemy models ทั้งหมด
# ทุก model จะต้อง inherit จาก Base นี้
Base = declarative_base()