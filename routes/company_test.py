from http import HTTPStatus
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_companies():
    response = client.get("/api/v1/company")
    assert response.status_code == HTTPStatus.OK
    assert response.headers["Content-Type"] == "application/json"
    assert isinstance(response.json()["data"], list)


def test_get_company():
    response = client.get("/api/v1/company/2")
    assert response.status_code == HTTPStatus.OK
    assert response.headers["Content-Type"] == "application/json"
    assert isinstance(response.json()["data"], dict)


def test_get_company_wrong_id():
    response = client.get("/api/v1/company/-1")
    assert response.status_code == HTTPStatus.BAD_REQUEST
