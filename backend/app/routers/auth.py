from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import Dict, Any
from datetime import timedelta

# These will be implemented later
# from app.core.security import create_access_token, verify_password
# from app.core.config import settings
# from app.models.user import User

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

# Mock user data for development
MOCK_USERS = {
    "admin": {
        "username": "admin",
        "email": "admin@example.com",
        "hashed_password": "$2b$12$lkG9Lih5Q0j8CjwH1NyEbehsj0lU7ZR2G/Y/eBJpY0hy4t73BZjMS",  # "password"
        "is_admin": True,
        "tenant_id": None
    },
    "acme_user": {
        "username": "acme_user",
        "email": "user@acme.com",
        "hashed_password": "$2b$12$lkG9Lih5Q0j8CjwH1NyEbehsj0lU7ZR2G/Y/eBJpY0hy4t73BZjMS",  # "password"
        "is_admin": False,
        "tenant_id": "acme"
    },
    "globex_user": {
        "username": "globex_user",
        "email": "user@globex.com",
        "hashed_password": "$2b$12$lkG9Lih5Q0j8CjwH1NyEbehsj0lU7ZR2G/Y/eBJpY0hy4t73BZjMS",  # "password"
        "is_admin": False,
        "tenant_id": "globex"
    }
}

@router.post("/login", response_model=Dict[str, Any])
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    """
    OAuth2 compatible token login, get an access token for future requests
    """
    user = MOCK_USERS.get(form_data.username)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # In production, use verify_password(form_data.password, user["hashed_password"])
    password_matches = form_data.password == "password"
    
    if not password_matches:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Use a hard-coded token for development
    # In production, use create_access_token from the security module
    access_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZ"
    if user["is_admin"]:
        access_token += ".admin"
    else:
        access_token += f".{user['tenant_id']}"
    
    return {
        "access_token": access_token,
        "token_type": "bearer"
    }

@router.get("/me", response_model=Dict[str, Any])
async def read_users_me(token: str = Depends(oauth2_scheme)):
    """
    Get current user
    """
    # In production, this would decode and validate the JWT token
    # For development, check the mock token
    
    is_admin = token.endswith(".admin")
    
    if is_admin:
        user = MOCK_USERS["admin"]
    else:
        tenant_id = token.split(".")[-1]
        # Find the user for this tenant
        for username, user_data in MOCK_USERS.items():
            if user_data.get("tenant_id") == tenant_id:
                user = user_data
                break
        else:
            user = None
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    return {
        "username": user["username"],
        "email": user["email"],
        "is_admin": user["is_admin"],
        "tenant_id": user["tenant_id"]
    } 