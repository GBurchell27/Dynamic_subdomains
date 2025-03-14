from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

# Import routers (will be implemented later)
# from app.routers import admin, tenant, auth

app = FastAPI(
    title="Marketing Mix Modeling SaaS Platform",
    description="API for multi-tenant marketing mix modeling platform",
    version="0.1.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, set this to specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Tenant middleware
@app.middleware("http")
async def add_tenant_context(request: Request, call_next):
    # Extract tenant from subdomain
    host = request.headers.get("host", "")
    subdomain = host.split(".")[0] if "." in host else None
    
    # Add tenant info to request state (actual implementation will lookup tenant in DB)
    request.state.tenant_id = subdomain
    
    response = await call_next(request)
    return response

# Include routers (commented out until implemented)
# app.include_router(auth.router, tags=["Authentication"])
# app.include_router(admin.router, prefix="/admin", tags=["Admin"])
# app.include_router(tenant.router, prefix="/tenant", tags=["Tenant"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the MMM SaaS Platform API"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True) 