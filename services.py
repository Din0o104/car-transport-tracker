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

    fleet = storage.load_fleet()

    if vin in fleet:
        raise ValueError(f"Автомобиль с VIN '{vin}' уже существует в системе.")

    car = Car(
        vin = vin,
        brand = brand,
        model = model,
        status=status,
        latitude=latitude,
        longitude=longitude,
    )
    fleet[vin] = car.to_dict()
    storage.save_fleet(fleet)
    return car


def get_car(vin: str) -> Car | None:
    fleet = storage.load_fleet()
    raw_data = fleet.get(vin)
    if not raw_data:
        return None
    return Car.from_dict(vin, raw_data)


def get_cars(status_filter: str | None = None) -> list[Car]:
    fleet = storage.load_fleet()

    cars = [Car.from_dict(vin, data) for vin, data in fleet.items()]

    if not status_filter:
        return cars

    target = status_filter.strip().lower()
    return [car for car in cars if car.status.strip().lower() == target]


def update_car_status(vin: str, new_status: str) -> Car:
    
    fleet = storage.load_fleet()

    if vin not in fleet:
        raise ValueError(f"Автомобиль с VIN '{vin}' не найден.")

    fleet[vin]["status"] = new_status
    storage.save_fleet(fleet)
    return Car.from_dict(vin, fleet[vin])


def delete_car(vin: str) -> Car:
   
    fleet = storage.load_fleet()

    if vin not in fleet:
        raise ValueError(f"Автомобиль с VIN '{vin}' не найден.")

    deleted_car = fleet.pop(vin)
    storage.save_fleet(fleet)
    return Car.from_dict(vin, deleted_car)   