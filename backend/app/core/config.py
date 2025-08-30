from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    Class to manage application settings and environment variables.
    """
    # Database connection URL
    # Pydantic จะอ่านค่านี้จาก environment variable ชื่อ DATABASE_URL โดยอัตโนมัติ
    DATABASE_URL: str = "postgresql://user:password@postgresserver/db"

    # Secret key for JWT
    SECRET_KEY: str = "a_very_secret_key"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config:
        # ระบุไฟล์ .env ที่จะใช้ (ถ้ามี)
        env_file = ".env"


# สร้าง instance ของ Settings เพื่อนำไปใช้ในส่วนอื่นๆ ของแอป
settings = Settings()