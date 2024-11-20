import os
import uvicorn
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.future import select


DATABASE_HOST = os.environ["DATABASE_HOST"]
DATABASE_USER = os.environ["DATABASE_USER"]
DATABASE_PASS = os.environ["DATABASE_PASS"]
DATABASE_NAME = os.environ["DATABASE_NAME"]
DATABASE_URL = f"postgresql+asyncpg://{DATABASE_USER}:{DATABASE_PASS}@{DATABASE_HOST}/{DATABASE_NAME}" 

# Database setup
engine = create_async_engine(DATABASE_URL, echo=True)
Base = declarative_base()
async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

# Dependency
async def get_db():
    async with async_session_maker() as session:
        yield session

# Models
class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

# Pydantic schemas
class ItemCreate(BaseModel):
    name: str

class ItemResponse(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True

# FastAPI app
app = FastAPI()

@app.on_event("startup")
async def startup():
    # Create tables on startup
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.get("/items", response_model=list[ItemResponse])
async def list_items(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Item))
    items = result.scalars().all()
    return items

@app.post("/items", response_model=ItemResponse)
async def add_item(item: ItemCreate, db: AsyncSession = Depends(get_db)):
    new_item = Item(name=item.name)
    db.add(new_item)
    await db.commit()
    await db.refresh(new_item)
    return new_item


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)