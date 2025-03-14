from pydantic import BaseModel, Field, validator
from typing import List, Optional
from datetime import datetime

class TenantBase(BaseModel):
    """Base Tenant schema with common attributes"""
    name: str
    subdomain: str
    industry: Optional[str] = None
    features: List[str] = Field(default_factory=list)
    primary_color: str = "#3B82F6"
    secondary_color: str = "#1E40AF"

class TenantCreate(TenantBase):
    """Schema for tenant creation"""
    @validator('subdomain')
    def validate_subdomain(cls, v):
        if not v.isalnum():
            raise ValueError('Subdomain must be alphanumeric')
        return v.lower()

class TenantUpdate(BaseModel):
    """Schema for tenant updates"""
    name: Optional[str] = None
    industry: Optional[str] = None
    features: Optional[List[str]] = None
    primary_color: Optional[str] = None
    secondary_color: Optional[str] = None
    is_active: Optional[bool] = None

class TenantInDB(TenantBase):
    """Schema for tenant as stored in database"""
    id: str
    is_active: bool = True
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    class Config:
        orm_mode = True

class TenantDetail(TenantInDB):
    """Schema for detailed tenant information"""
    pass 