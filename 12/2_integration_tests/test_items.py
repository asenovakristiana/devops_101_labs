import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from main import app, get_db
from main import Base

# Set up test database
SQLALCHEMY_DATABASE_URL = "sqlite:///./tests_database.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Test database fixture
@pytest.fixture(scope="module")
def test_db():
    Base.metadata.create_all(bind=engine)  # Create tables
    db = TestingSessionLocal()
    yield db
    db.close()
    Base.metadata.drop_all(bind=engine)  # Clean up

# Override dependency fixture
@pytest.fixture
def override_get_db(test_db):
    def _override():
        yield test_db
    app.dependency_overrides[get_db] = _override
    yield
    app.dependency_overrides.clear()

# Test client
@pytest.fixture
def client(override_get_db):
    return TestClient(app)

# Test creating an item
def test_create_item(client):
    response = client.post("/items/?name=Test Item")
    print(response.content)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] is not None
    assert data["name"] == "Test Item"

# Test getting an item
def test_get_item(client):
    # First, create an item
    create_response = client.post("/items/?name=Another Item")
    assert create_response.status_code == 200
    item_id = create_response.json()["id"]

    # Fetch the created item
    get_response = client.get(f"/items/{item_id}")
    assert get_response.status_code == 200
    data = get_response.json()
    assert data["id"] == item_id
    assert data["name"] == "Another Item"
