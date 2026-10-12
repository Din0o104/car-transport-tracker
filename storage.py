import sqlite3
from models import Car

DB_NAME = "fleet.db"

def get_connection() -> sqlite3.Connection:
    return sqlite3.connect(DB_NAME)

def init_db() -> None:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS cars (
                vin TEXT PRIMARY KEY,
                brand TEXT NOT NULL,
                model TEXT NOT NULL,
                status TEXT NOT NULL,
                latitude REAL NOT NULL,
                longitude REAL NOT NULL
            );
        """
        )
        conn.commit()

def row_to_car(row: tuple) -> Car:
    return Car(
        vin = row[0],
        brand= row [1],
        model = row[2],
        status = row[3],
        latitude = row[4],
        longitude = row[5]
    )

def insert_car(car: Car) -> None:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO cars (vin, brand, model, status, latitude, longitude)
            VALUES (?,?,?,?,?,?);
        """,
            (
                car.vin,
                car.brand,
                car.model,
                car.status,
                car.latitude,
                car.longitude,
            ),
        )
        conn.commit()

def get_car_by_vin(vin: str) -> Car | None:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT vin, brand, model, status, latitude, longitude FROM cars WHERE vin = ?",
            (vin,),
        )
    row = cursor.fetchone()
    if not row:
        return None
    return row_to_car(row)

def get_cars(status_filter: str | None = None) -> list[Car]:
    with get_connection() as conn:
        cursor = conn.cursor()

        if status_filter:
            cursor.execute(
                """
                SELECT vin, brand, model, status, latitude, longitude
                FROM cars
                WHERE LOWER(status) = LOWER(?)
            """,
            (status_filter.strip(),),
            )
        else:
            cursor.execute(
                "SELECT vin, brand, model, status, latitude, longitude FROM cars"
            )

        rows = cursor.fetchall()
        return [row_to_car(row) for row in rows]


def update_car_status(vin: str, new_status: str) -> bool:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE cars SET status = ? WHERE vin = ?",
            (new_status, vin),
        )
        conn.commit()
        return cursor.rowcount > 0

def delete_car(vin: str) -> bool:   
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM cars WHERE vin = ?", (vin,))
        conn.commit()
        return cursor.rowcount > 0