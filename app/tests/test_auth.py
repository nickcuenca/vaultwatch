import pytest
from httpx import AsyncClient
from fastapi import status
from app.main import app
from app.database import Base, engine, SessionLocal, get_db
from sqlalchemy.orm import Session
from app import models
import asyncio

test_email = "testuser@example.com"
test_password = "testpassword"

@pytest.fixture(scope="module")
def override_test_db():
    # Setup test DB
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()

    def _get_test_db():
        try:
            yield db
        finally:
            pass

    app.dependency_overrides[get_db] = _get_test_db
    yield db
    db.close()

@pytest.mark.asyncio
async def test_register_and_login(override_test_db):
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/register", json={
            "email": test_email,
            "password": test_password
        })
        print("Register:", response.status_code, response.json())
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert data["email"] == test_email
        assert "id" in data
        assert "created_at" in data
        assert "role" in data

        response = await ac.post(
            "/login",
            data={"username": test_email, "password": test_password},
            headers={"Content-Type": "application/x-www-form-urlencoded"}
        )
        print("Login:", response.status_code, response.json())
        assert response.status_code == status.HTTP_200_OK
        token_data = response.json()
        assert "access_token" in token_data
        assert token_data["token_type"] == "bearer"

@pytest.mark.asyncio
async def test_failed_login(override_test_db):
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post(
            "/login",
            data={"username": test_email, "password": "wrongpassword"},
            headers={"Content-Type": "application/x-www-form-urlencoded"}
        )
        print("Failed login:", response.status_code, response.json())
        assert response.status_code == status.HTTP_400_BAD_REQUEST