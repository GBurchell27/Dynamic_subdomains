from typing import Generator
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

# Import settings later
# from app.core.config import settings

# For now, hardcode the database URL
DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/mmm_saas"

# Create SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Create session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create base class for SQLAlchemy models
Base = declarative_base()

def get_db() -> Generator[Session, None, None]:
    """
    Get a database session as a dependency
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def init_db() -> None:
    """
    Initialize database
    """
    # Create tables if they don't exist
    # This should use Alembic in production
    Base.metadata.create_all(bind=engine) 