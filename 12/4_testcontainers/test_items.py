import pytest
from testcontainers.postgres import PostgresContainer
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from fastapi.testclient import TestClient
from main import app, get_db

# SQLAlchemy setup
Base = declarative_base()
TestingSessionLocal = None

class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

# Dependency override
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

# Test fixture for PostgreSQL with testcontainers
@pytest.fixture(scope="module")
def postgres_container():
    with PostgresContainer("postgres:15.2") as postgres:
        engine = create_engine(postgres.get_connection_url())
        global TestingSessionLocal
        TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        
        # Create tables
        Base.metadata.create_all(bind=engine)
        yield engine  # Provide the engine to the tests
        
        # Cleanup
        Base.metadata.drop_all(bind=engine)

# Test client fixture
@pytest.fixture
def client(postgres_container):
    return TestClient(app)

# Test cases
def test_create_item(client):
    response = client.post("/items/?name=Test Item")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] is not None
    assert data["name"] == "Test Item"

def test_get_item(client):
    # Create an item
    create_response = client.post("/items/?name=Another Item")
    assert create_response.status_code == 200
    item_id = create_response.json()["id"]

    # Retrieve the item
    get_response = client.get(f"/items/{item_id}")
    assert get_response.status_code == 200
    data = get_response.json()
    assert data["id"] == item_id
    assert data["name"] == "Another Item"
