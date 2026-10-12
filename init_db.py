import sqlite3

connection = sqlite3.connect("fleet.db")

cursor = connection.cursor()

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

test_car = ("VIN999", "Toyota", "Camry", "free", 55.75, 37.61)

cursor.execute(
    """
INSERT OR IGNORE INTO cars (vin, brand, model, status, latitude, longitude)
VALUES (?, ?, ?, ?, ?, ?);
""",
    test_car,
)

connection.commit()

cursor.execute("SELECT * FROM cars;")
rows = cursor.fetchall()

print("Успех! Данные в таблице cars:")
for row in rows:
    print(row)

connection.close()
