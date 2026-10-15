from typing import  List, Optional
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
import services
import storage

storage.init_db()

app = FastAPI(
    title="Fleet Management API",
    description="REST API для управления автопарком",
    version= "1.0.0",
)

# --- DTO / Pydantic-схемы ---

class CarCreateSchema(BaseModel):
    vin: str = Field(..., min_length=3, max_length= 17, example="VIN100")
    brand: str =Field(..., example= "BMW")
    model: str =Field(..., example="X5")
    status: str = Field(default="free", example= "free")
    latitude: float = Field(..., ge=-90.0, le= 90.0, example= 76.23)
    longitude: float = Field(..., ge = -180.0, le = 180.0, example = 109.52)


class CarStatusUpdateSchema(BaseModel):
    status: str = Field(..., example ='maintenance')


class CarResponseSchema(BaseModel):
    vin: str
    brand: str
    model: str
    status: str
    latitude: float
    longitude: float



@app.get("/cars", response_model=List[CarResponseSchema], tags = ["Cars"])
def get_car(status_filter: Optional[str] = None):

    return services.get_cars(status_filter=status_filter)


@app.get("/cars/{vin}", response_model=CarResponseSchema, tags=["Cars"])
def get_car_by_vin(vin: str):
    car = services.get_car(vin)

    if not car:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Автомобиль с VIN '{vin}' не найден",
        )
    return car


@app.post(
    "/cars",
    response_model=CarResponseSchema,
    status_code=status.HTTP_201_CREATED,
    tags=["Cars"],
)
def create_car(car_data: CarCreateSchema):
    try:
        return services.add_car(
            vin=car_data.vin,
            brand=car_data.brand,
            model=car_data.model,
            status=car_data.status,
            latitude= car_data.latitude,
            longitude = car_data.longitude,
        )
    except ValueError as e:
        raise HTTPException(
            status_code= status.HTTP_409_CONFLICT,
            detail=str(e)
        )


@app.patch(
    "/cars/{vin}/status", response_model=CarResponseSchema, tags = ["Cars"]
)
def update_status(vin:str, update_data: CarStatusUpdateSchema):
    try:
        return services.update_car_status(vin, update_data.status)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e),
        )


@app.delete("/cars/{vin}", response_model=CarResponseSchema, tags=["Cars"])
def delete_car(vin: str):
    try:
        return services.delete_car(vin)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e),
        )
