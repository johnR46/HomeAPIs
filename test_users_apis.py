from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_get_users():
    response = client.get("/users/")
    assert response.status_code == 200


def test_get_users_by_id():
    response = client.get("/users/users/1")
    assert response.status_code == 200
