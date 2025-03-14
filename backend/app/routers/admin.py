from fastapi import APIRouter, Depends, HTTPException, status
from typing import List, Dict, Any

# These will be implemented later
# from app.schemas.tenant import TenantCreate, TenantUpdate, TenantDetail
# from app.services.tenant_service import TenantService
# from app.core.security import get_current_admin_user

router = APIRouter()

# Mock tenant data for development
MOCK_TENANTS = [
    {
        "id": "acme", 
        "name": "Acme Corporation", 
        "subdomain": "acme",
        "industry": "Technology",
        "features": ["dashboard", "data_upload", "basic_analysis", "advanced_analysis"],
        "primaryColor": "#3B82F6",
        "secondaryColor": "#1E40AF",
        "is_active": True
    },
    {
        "id": "globex", 
        "name": "Globex Industries", 
        "subdomain": "globex",
        "industry": "Manufacturing",
        "features": ["dashboard", "data_upload", "basic_analysis"],
        "primaryColor": "#10B981",
        "secondaryColor": "#065F46",
        "is_active": True
    }
]

@router.get("/tenants", response_model=List[Dict[str, Any]])
def get_tenants():
    """
    Get all tenants (admin only)
    """
    return MOCK_TENANTS

@router.post("/tenants", status_code=status.HTTP_201_CREATED)
def create_tenant(tenant_data: Dict[str, Any]):
    """
    Create a new tenant (admin only)
    """
    # Create new tenant from data
    new_tenant = {
        "id": tenant_data.get("subdomain", "").lower(),
        "name": tenant_data.get("name", ""),
        "subdomain": tenant_data.get("subdomain", "").lower(),
        "industry": tenant_data.get("industry", "General"),
        "features": tenant_data.get("features", ["dashboard"]),
        "primaryColor": tenant_data.get("primaryColor", "#3B82F6"),
        "secondaryColor": tenant_data.get("secondaryColor", "#1E40AF"),
        "is_active": True
    }
    
    # Add to mock database
    MOCK_TENANTS.append(new_tenant)
    
    return new_tenant

@router.get("/tenants/{tenant_id}", response_model=Dict[str, Any])
def get_tenant(tenant_id: str):
    """
    Get tenant by ID (admin only)
    """
    for tenant in MOCK_TENANTS:
        if tenant["id"] == tenant_id:
            return tenant
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Tenant not found"
    )

@router.get("/statistics")
def get_admin_statistics():
    """
    Get platform-wide statistics (admin only)
    """
    return {
        "total_tenants": len(MOCK_TENANTS),
        "active_tenants": len([t for t in MOCK_TENANTS if t["is_active"]]),
        "enterprise_tenants": len([t for t in MOCK_TENANTS if len(t["features"]) >= 5]),
        "avg_utilization": 78
    } 