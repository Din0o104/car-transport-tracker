from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI(title= "песочница FastAPI")

@app.get("/")
def home():
    return {"message": "песочница работает!"}

@app.get("/calc/{operation}")
def calculate(operator: str, a: int, b: int):
    if operator == "add":
        return {"result": a + b}
    elif operator == "sub":
        return {"result": a - b}
    return {"error": "неизвестная операция"}

class CarOrder(BaseModel):
    brand: str
    passengers: int
    has_child_seat: bool = False

@app.post("/order")
def make_order(order: CarOrder):
    return {
        "status": "успешно",
        "car": order.brand,
        "passengers": order.passengers,
        "need_seat": order.has_child_seat,
    }

@app.post("/order")
def make_order(order: CarOrder):
    return {
        "status": "успешно",
        "car": order.brand,
        "passengers": order.passengers,
        "need_seat": order.has_child_seat,
    }