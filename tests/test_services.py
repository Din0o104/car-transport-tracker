import sqlite3
import pytest
import services
import storage


@pytest.fixture(autouse=True)
def clean_db(monkeypatch):
    conn =   sqlite3.connect(":memory:")
    monkeypatch.setattr(storage, "get_connection", lambda: conn)
    storage.init_db()
    yield
    conn.close()

def test_add_car_success():
    car = services.add_car("VIN100", "BMW", "X5", "free", 55.34, 37.45)

    assert car.vin == "VIN100"
    assert car.brand == "BMW"

    saved = services.get_car("VIN100")
    assert saved is not None
    assert saved.model == "X5"

def test_add_car_duplicate_vin_raise_error():
    services.add_car("VIN100", "BMW", "X5", "free", 55.34, 37.45)

    with pytest.raises(ValueError, match= "уже существует"):
        services.add_car("VIN100", "Audi", "A6", "free", 59.93, 30.33)

def test_get_car_not_found():
    assert services.get_car("NON_EXISTING_VIN") is None


def test_get_cars_filter_by_status():
    services.add_car("VIN1", "BMW", "X5", "free", 55.34, 37.45)
    services.add_car("VIN2", "Audi", "A6", "in_use", 55.35, 37.46)
    services.add_car("VIN3", "Tesla", "Model 3", "free", 55.36, 37.47)

    free_cars = services.get_cars(status_filter="free")
    assert len(free_cars) == 2
    assert all(car.status == "free" for car in free_cars)


def test_update_car_status_success():
    services.add_car("VIN100", "BMW", "X5", "free", 55.34, 37.45)

    updated = services.update_car_status("VIN100", "maintenance")
    assert updated.status == "maintenance"

    saved = services.get_car("VIN100")
    assert saved.status == "maintenance"


def test_update_car_status_not_found():
    with pytest.raises(ValueError):
        services.update_car_status("UNKNOWN_VIN", "in_use")


def test_delete_car_success():
    services.add_car("VIN100", "BMW", "X5", "free", 55.34, 37.45)

    deleted = services.delete_car("VIN100")
    assert deleted.vin == "VIN100"
    assert services.get_car("VIN100") is None


def test_delete_car_not_found():
    with pytest.raises(ValueError):
        services.delete_car("UNKNOWN_VIN")