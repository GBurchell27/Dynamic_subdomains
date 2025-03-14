from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from datetime import date, datetime

class MarketingDataBase(BaseModel):
    """Base schema for marketing data"""
    date: date
    channel: str
    spend: float
    impressions: Optional[float] = None
    clicks: Optional[float] = None
    conversions: Optional[float] = None
    revenue: Optional[float] = None

class MarketingDataCreate(MarketingDataBase):
    """Schema for creating marketing data"""
    pass

class MarketingDataInDB(MarketingDataBase):
    """Schema for marketing data as stored in database"""
    id: str
    tenant_id: str
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    class Config:
        orm_mode = True

class MarketingDataBulkUpload(BaseModel):
    """Schema for bulk uploading marketing data"""
    data: List[MarketingDataBase]

class ChannelMetrics(BaseModel):
    """Schema for channel metrics"""
    channel: str
    spend: float
    efficiency: float

class PerformanceMetrics(BaseModel):
    """Schema for tenant performance metrics"""
    roas: float
    cpa: float
    ctr: float
    channel_efficiency: List[ChannelMetrics]

class DashboardSummary(BaseModel):
    """Schema for dashboard summary statistics"""
    total_spend: float
    total_impressions: float
    total_clicks: float

class DashboardMetrics(BaseModel):
    """Schema for full dashboard metrics"""
    summary: DashboardSummary
    performance: PerformanceMetrics

class ChannelAttribution(BaseModel):
    """Schema for marketing channel attribution"""
    channel: str
    contribution: float
    roi: Optional[float] = None

class ModelAccuracy(BaseModel):
    """Schema for model accuracy metrics"""
    r_squared: float
    mape: float

class MMMResults(BaseModel):
    """Schema for marketing mix modeling results"""
    channel_attribution: List[ChannelAttribution]
    model_accuracy: ModelAccuracy

class AnalysisResult(BaseModel):
    """Schema for complete analysis result"""
    analysis_id: str
    status: str
    results: Optional[MMMResults] = None
    created_at: datetime 