from typing import Optional
from fastapi import Request, Depends, HTTPException, status
from sqlalchemy.orm import Session

# These imports will be implemented later
# from app.models.tenant import Tenant
# from app.utils.db import get_db

class TenantNotFound(Exception):
    """Exception raised when tenant is not found"""
    pass

def get_tenant_id_from_subdomain(subdomain: Optional[str]) -> Optional[str]:
    """
    Get tenant ID from subdomain
    
    In production, this would lookup the tenant ID from database based on subdomain
    """
    if not subdomain or subdomain == "admin" or subdomain == "api":
        return None
    
    # For now, just return the subdomain as the tenant ID
    # In production, you would query the database
    return subdomain

def set_tenant_context_in_db(tenant_id: str, db: Session):
    """
    Set tenant context in database session
    
    For PostgreSQL, this would set the RLS context variable
    """
    # Set the tenant ID as an application context in the DB session
    # Example for PostgreSQL:
    # db.execute("SET app.tenant_id = :tenant_id", {"tenant_id": tenant_id})
    pass

async def get_current_tenant_id(request: Request) -> Optional[str]:
    """
    Get current tenant ID from request
    """
    return request.state.tenant_id

async def get_tenant_or_404(
    tenant_id: str = Depends(get_current_tenant_id),
    # db: Session = Depends(get_db)
):
    """
    Get tenant or raise 404
    
    In production, this would lookup the tenant from the database
    """
    if not tenant_id:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Tenant not found",
        )
    
    # Mock tenant object for now
    # In production, you would query the database:
    # tenant = db.query(Tenant).filter(Tenant.id == tenant_id).first()
    # if not tenant:
    #     raise HTTPException(status_code=404, detail="Tenant not found")
    
    return {"id": tenant_id, "name": f"Tenant {tenant_id}", "is_active": True} 