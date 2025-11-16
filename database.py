from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import text
from dotenv import load_dotenv
import os
import asyncio

# Load .env file
load_dotenv()

# Get variables
DB_HOST = os.getenv("POSTGRES_HOST")
DB_PORT = os.getenv("POSTGRES_PORT")
DB_NAME = os.getenv("POSTGRES_DB")
DB_USER = os.getenv("POSTGRES_USER")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD")

# Build DATABASE URL
DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# SQLAlchemy Engine
engine = create_async_engine(DATABASE_URL, echo=True)

# Connection test
async def test_connection():
    try:
        async with engine.connect() as conn:
            await conn.execute(text("SELECT 1"))
            print("✅ Connected to PostgreSQL successfully.")
    except Exception as e:
        print(f"❌ PostgreSQL connection failed: {e}")

# Run when script is executed directly
if __name__ == "__main__":
    asyncio.run(test_connection())
