from models import Car
import storage


def add_car(
        vin: str,
        brand: str,
        model: str,
        status: str,
        latitude: float,
        longitude: float,
    ) -> Car:

        if storage.get_car_by_vin(vin):
            raise ValueError(f"Машина с VIN '{vin}' уже существует")

        car = Car(
            vin = vin,
            brand = brand,
            model = model,
            status = status,
            latitude = latitude,
            longitude = longitude,
        )

        storage.insert_car(car)
        return car


def get_car(vin: str) -> Car | None:
    
    return storage.get_car_by_vin(vin)


def get_cars(status_filter: str | None = None) -> list[Car]:
    return storage.get_cars(status_filter)

def update_car_status(vin: str, new_status: str) -> Car:
    car = storage.get_car_by_vin(vin)
    if not car:
        raise ValueError(f"Автомобиль с VIN '{vin}' не найден.")

    storage.update_car_status(vin, new_status)
    return storage.get_car_by_vin(vin)


def delete_car(vin: str) -> Car:
   
    car = storage.get_car_by_vin(vin)

    if not car:
        raise ValueError(f"Автомобиль с VIN '{vin}' не найден.")

    storage.delete_car(vin)
    return car   