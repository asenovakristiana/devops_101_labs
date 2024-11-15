import os
import uvicorn
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, Session, declarative_base

# Database setup
DATABASE_URL = "sqlite:///data/data.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
Base = declarative_base()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Models
class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, index=True)

Base.metadata.create_all(bind=engine)

# FastAPI app
app = FastAPI()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# API Pydantic schema
class ItemCreate(BaseModel):
    text: str

# Endpoints
@app.get("/items", response_model=list[dict])
def list_items(db: Session = Depends(get_db)):
    items = db.query(Item).all()
    return [{"id": item.id, "text": item.text} for item in items]

@app.post("/items", response_model=dict)
def add_item(item: ItemCreate, db: Session = Depends(get_db)):
    db_item = Item(text=item.text)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return {"id": db_item.id, "text": db_item.text}

@app.delete("/items/{item_id}", response_model=dict)
def delete_item(item_id: int, db: Session = Depends(get_db)):
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(db_item)
    db.commit()
    return {"message": "Item deleted successfully"}

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)