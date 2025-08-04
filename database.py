from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
import os

DATABASE_URL = os.environ.get('DATABASE_URL', 'postgresql+asyncpg://user:password@localhost/recipes')

# Create async engine and sessionmaker
engine = create_async_engine(
    DATABASE_URL, echo=False, future=True
)

AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

def get_session():
    db = AsyncSessionLocal()
    try:
        yield db
    finally:
        db.close()
