import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.db import Base
from app.main import app
from app.routers import get_db
from fastapi.testclient import TestClient

SQLALCHEMY_DATABASE_URL = "sqlite:///test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)

TestingSessionLocal = sessionmaker(bind=engine)

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


Base.metadata.create_all(bind=engine)
app.dependency_overrides[get_db] = override_get_db


@pytest.fixture
def test_client():
    return TestClient(app)

@pytest.fixture
def test_user(test_client):
    """Helper fixture to create a user before tests"""
    payload = {"name": "John Doe", "email": "john@example.com"}
    response = test_client.post("/users/", json=payload)
    assert response.status_code == 200
    return response.json()