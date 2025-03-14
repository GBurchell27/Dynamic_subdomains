from sqlalchemy import Column, String, Boolean, JSON, DateTime
from sqlalchemy.sql import func
import uuid

from app.utils.db import Base

class Tenant(Base):
    """
    SQLAlchemy model for tenants
    """
    __tablename__ = "tenants"
    
    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    name = Column(String, nullable=False)
    subdomain = Column(String, unique=True, nullable=False, index=True)
    industry = Column(String, nullable=True)
    features = Column(JSON, nullable=False, default=list)
    primary_color = Column(String, nullable=False, default="#3B82F6")
    secondary_color = Column(String, nullable=False, default="#1E40AF")
    is_active = Column(Boolean, nullable=False, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now()) 