from dataclasses import dataclass

@dataclass

class Car:
    vin: str
    brand: str
    model: str
    status: str
    latitude: float
    longitude: float

    def to_dict(self) -> dict:

        return {
            "brand": self.brand,
            "model": self.model,
            "status": self.status,
            "latitude": self.latitude,
            "longitude": self.longitude,
        }

    @classmethod

    def from_dict(cls, vin: str, data: dict) -> "Car":
        return cls(
            vin = vin,
            brand = data["brand"],
            model = data["model"],
            status = data["status"],
            latitude = float(data["latitude"]),
            longitude = float(data["longitude"]),
        )

