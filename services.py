import storage

def add_car(vin, brand, model, status, latitude, longitude):
    fleet = storage.load_fleet()

    if vin in fleet:
        raise ValueError(f"Автомобиль с VIN '{vin}' уже существует в системе.")

    car_data = {
        "brand": brand,
        "model": model,
        "status": status,
        "latitude": latitude,
        "longitude": longitude,
    }
    fleet[vin] = car_data
    storage.save_fleet(fleet)
    return car_data

def get_car(vin):
    fleet = storage.load_fleet()
    return fleet.get(vin)

def get_cars(status_filter = None):
    fleet = storage.load_fleet()
    if not status_filter:
        return fleet

    target = status_filter.strip().lower()
    return {
        vin: car
        for vin, car in fleet.items()
        if car["status"].strip().lower() == target
    }

def update_car_status(vin, new_status):
    
    fleet = storage.load_fleet()

    if vin not in fleet:
        raise ValueError(f"Автомобиль с VIN '{vin}' не найден.")

    fleet[vin]["status"] = new_status
    storage.save_fleet(fleet)
    return fleet[vin]


def delete_car(vin):
   
    fleet = storage.load_fleet()

    if vin not in fleet:
        raise ValueError(f"Автомобиль с VIN '{vin}' не найден.")

    deleted_car = fleet.pop(vin)
    storage.save_fleet(fleet)
    return deleted_car   