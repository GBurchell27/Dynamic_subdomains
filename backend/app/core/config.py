import os
from pydantic_settings import BaseSettings
from typing import List, Optional, Dict, Any

class Settings(BaseSettings):
    """
    Application settings configured via environment variables
    """
    # API
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "MMM SaaS Platform"
    
    # Security
    SECRET_KEY: str = os.getenv("SECRET_KEY", "dev_secret_key_change_in_production")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8  # 8 days
    
    # Database
    DATABASE_URL: str = os.getenv(
        "DATABASE_URL", "postgresql://postgres:postgres@localhost:5432/mmm_saas"
    )
    
    # CORS
    CORS_ORIGINS: List[str] = [
        "http://localhost:3000",
        "http://localhost:8000",
        # Add your frontend domains in production
    ]
    
    # Tenant Settings
    DEFAULT_TENANT_FEATURES: List[str] = ["dashboard", "data_upload", "basic_analysis"]
    
    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings() 