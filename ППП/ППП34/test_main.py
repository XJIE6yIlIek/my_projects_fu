from fastapi.testclient import TestClient
from myapp.main import app

client = TestClient(app)


def test_create_city():
    response = client.post("/city/", json={"name": "Test City"})
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "Test City"}


def test_get_cities():
    response = client.get("/city/")
    assert response.status_code == 200
    assert len(response.json()) > 0


def test_create_prediction():
    response = client.post("/predictions/1", json={
        "date": "2024-01-01T00:00:00",
        "temperature": -10,
        "cloud": "none"
    })
    assert response.status_code == 200
    assert "prediction_id" in response.json()


def test_get_last_weather():
    response = client.get("/city/1")
    assert response.status_code == 200
    assert len(response.json()) == 0


def test_get_weather_predictions():
    response = client.get("/city/1/predictions/?date=2024-01-01")
    assert response.status_code == 200
    assert len(response.json()) > 0


def test_update_weather():
    response = client.put("/predictions/1/1", json={
        "date": "2024-01-01",
        "temperature": -5,
        "cloud": "clear"
    })
    assert response.status_code == 200
    assert response.json()["temperature"] == -5


def test_delete_weather():
    response = client.delete("/predictions/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1
