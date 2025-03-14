from sqlalchemy import Column, String, Float, Date, ForeignKey, DateTime
from sqlalchemy.sql import func
import uuid

from app.utils.db import Base

class MarketingData(Base):
    """
    SQLAlchemy model for marketing channel data
    """
    __tablename__ = "marketing_data"
    
    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    tenant_id = Column(String, ForeignKey("tenants.id"), nullable=False, index=True)
    date = Column(Date, nullable=False, index=True)
    channel = Column(String, nullable=False, index=True)
    spend = Column(Float, nullable=False)
    impressions = Column(Float, nullable=True)
    clicks = Column(Float, nullable=True)
    conversions = Column(Float, nullable=True)
    revenue = Column(Float, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Make sure RLS is enabled on this table
    __table_args__ = {
        'info': {'rls': True}
    } 