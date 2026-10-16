from fastapi.testclient import TestClient
from api import app

client = TestClient(app)


def test_create_car_success():
    """Проверка успешного создания автомобиля через POST /cars (статус 201)."""
    payload = {
        "vin": "VIN_API_1",
        "brand": "Tesla",
        "model": "Model 3",
        "status": "free",
        "latitude": 55.75,
        "longitude": 37.61,
    }
    response = client.post("/cars", json=payload)

    assert response.status_code == 201
    data = response.json()
    assert data["vin"] == "VIN_API_1"
    assert data["brand"] == "Tesla"
    assert data["status"] == "free"


def test_create_car_duplicate_vin_returns_409():
    """Проверка перехвата дубликата VIN и возврата статуса 409 Conflict."""
    payload = {
        "vin": "VIN_DUP",
        "brand": "Audi",
        "model": "A6",
        "status": "free",
        "latitude": 52.0,
        "longitude": 21.0,
    }
    first_resp = client.post("/cars", json=payload)
    assert first_resp.status_code == 201

    second_resp = client.post("/cars", json=payload)
    assert second_resp.status_code == 409
    assert "уже существует" in second_resp.json()["detail"]


def test_create_car_invalid_coordinates_returns_422():
    """Проверка валидации Pydantic: некорректные координаты возвращают 422."""
    payload = {
        "vin": "VIN_BAD_LAT",
        "brand": "Lada",
        "model": "Vesta",
        "status": "free",
        "latitude": 150.0,
        "longitude": 30.0,
    }
    response = client.post("/cars", json=payload)
    assert response.status_code == 422


def test_get_car_by_vin_not_found_returns_404():
    """Проверка запроса несуществующего автомобиля через GET /cars/{vin}."""
    response = client.get("/cars/NON_EXISTING_VIN")
    assert response.status_code == 404
    assert response.json()["detail"] == "Автомобиль с VIN 'NON_EXISTING_VIN' не найден"


def test_update_status_and_delete_car_lifecycle():
    """Проверка жизненного цикла: создание -> обновление статуса -> удаление."""
    car_payload = {
        "vin": "VIN_LIFECYCLE",
        "brand": "Volvo",
        "model": "XC90",
        "status": "free",
        "latitude": 59.93,
        "longitude": 30.33,
    }
    resp_create = client.post("/cars", json=car_payload)
    assert resp_create.status_code == 201

    patch_payload = {"status": "maintenance"}
    resp_patch = client.patch("/cars/VIN_LIFECYCLE/status", json=patch_payload)
    assert resp_patch.status_code == 200
    assert resp_patch.json()["status"] == "maintenance"

    resp_delete = client.delete("/cars/VIN_LIFECYCLE")
    assert resp_delete.status_code == 200

    resp_check = client.get("/cars/VIN_LIFECYCLE")
    assert resp_check.status_code == 404