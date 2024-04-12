import pytest
from fastapi import Depends,APIRouter, requests, status
from app1.models import User1
from httpx import AsyncClient
from main import app
from fastapi.testclient import TestClient
router = APIRouter()
client = TestClient(app)

def test_login_for_access_token():
    login_data = {"username": "tommy", "password": "call"}
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    response = client.post("/token/", data=login_data, headers = headers)
    assert response.status_code == 202
    assert "access_token" in response.json()
    assert response.json()["token_type"] == "bearer"
    return response.json()["access_token"]

def test_create_user():
    user_data = {
        "id": 65,
        "username": "test_user1 ",
        "password": "test_password"
    }
    response = client.post("/users/", json=user_data)
    assert response.status_code == 202
    assert response.json()["username"] == "test_user"

@pytest.mark.asyncio
async def test_update_user():
    access_token = await test_login_for_access_token()
    user_data = {"username": "testuser_updated", "password": "testpassword_updated"}
    async with AsyncClient(app=app, base_url="http://localhost:8000") as client:
        response = await client.put("/users/1", json=user_data, headers={"Authorization": f"Bearer {access_token}"})
    assert response.status_code == status.HTTP_202_ACCEPTED
    assert response.json()["username"] == user_data["username"]

@pytest.mark.asyncio
async def test_delete_user():
    access_token = await test_login_for_access_token()
    async with AsyncClient(app=app, base_url="http://localhost:8000") as client:
        response = await client.delete("/users/1", headers={"Authorization": f"Bearer {access_token}"})
    assert response.status_code == status.HTTP_202_ACCEPTED

@pytest.mark.asyncio
async def test_create_new_book():
    access_token = await test_login_for_access_token()
    book_data = {"title": "Test Book", "author": "Test Author", "genre": "Test Genre", "price": 10.99, "quantity": 5}
    async with AsyncClient(app=app, base_url="http://localhost:8000") as client:
        response = await client.post("/books/", json=book_data, headers={"Authorization": f"Bearer {access_token}"})
    assert response.status_code == status.HTTP_202_ACCEPTED
    assert response.json()["title"] == book_data["title"]

@pytest.mark.asyncio
async def test_get_all_books_route():
    access_token = await test_login_for_access_token()
    async with AsyncClient(app=app, base_url="http://localhost:8000") as client:
        response = await client.get("/books/", headers={"Authorization": f"Bearer {access_token}"})
    assert response.status_code == status.HTTP_202_ACCEPTED
    assert isinstance(response.json(), list)

@pytest.mark.asyncio
async def test_get_book_by_title_route():
    access_token = await test_login_for_access_token()
    async with AsyncClient(app=app, base_url="http://localhost:8000") as client:
        response = await client.get("/books/Test Book", headers={"Authorization": f"Bearer {access_token}"})
    assert response.status_code == status.HTTP_202_ACCEPTED
    assert response.json()["title"] == "Test Book"

@pytest.mark.asyncio
async def test_update_book_by_title_route():
    access_token = await test_login_for_access_token()
    updated_book_data = {"title": "Test Book", "author": "Updated Author", "genre": "Updated Genre", "price": 12.99, "quantity": 7}
    async with AsyncClient(app=app, base_url="http://localhost:8000") as client:
        response = await client.put("/books/Test Book", json=updated_book_data, headers={"Authorization": f"Bearer {access_token}"})
    assert response.status_code == status.HTTP_202_ACCEPTED
    assert response.json()["author"] == updated_book_data["author"]

@pytest.mark.asyncio
async def test_delete_book_by_title_route():
    access_token = await test_login_for_access_token()
    async with AsyncClient(app=app, base_url="http://localhost:8000") as client:
        response = await client.delete("/books/Test Book", headers={"Authorization": f"Bearer {access_token}"})
    assert response.status_code == status.HTTP_202_ACCEPTED