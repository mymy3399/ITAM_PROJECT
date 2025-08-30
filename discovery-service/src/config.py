from pydantic_settings import BaseSettings
from typing import List, Optional


class Settings(BaseSettings):
    """
    Discovery Service Configuration
    """
    # API Configuration
    API_BASE_URL: str = "http://api:8000/api/v1"
    API_USERNAME: str = "admin@example.com"  # Service account email
    API_PASSWORD: str = "admin123"           # Service account password
    
    # Scanning Configuration
    SCAN_INTERVAL_MINUTES: int = 60          # How often to run scans
    NETWORK_SUBNETS: List[str] = ["192.168.1.0/24"]  # Networks to scan
    
    # Discovery Settings
    ENABLE_NMAP_SCAN: bool = True
    ENABLE_WMI_DISCOVERY: bool = False       # Requires Windows credentials
    ENABLE_SSH_DISCOVERY: bool = False       # Requires SSH credentials
    ENABLE_SNMP_DISCOVERY: bool = False      # Requires SNMP community strings
    
    # Timeouts
    NMAP_TIMEOUT: int = 300                  # 5 minutes
    CONNECTION_TIMEOUT: int = 30             # 30 seconds
    
    # Logging
    LOG_LEVEL: str = "INFO"
    
    class Config:
        env_file = ".env"


settings = Settings()