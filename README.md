# Fleet Transport Tracker API

A lightweight, production-grade RESTful API designed for commercial fleet management, vehicle telematics, and lifecycle tracking. Built with **FastAPI**, **Pydantic v2**, and **SQLite3**, adhering strictly to **Layered Architecture** and Clean Code principles.

---

## Key Highlights

- **Layered Architecture (Separation of Concerns):** Clean separation between HTTP routing (`api.py`), business logic (`services.py`), and database persistence (`storage.py`).
- **Strict Schema Validation & DTOs:** All incoming payloads and responses are validated via Pydantic schemas (including coordinate boundaries and VIN constraints).
- **Domain Exception Translation:** Domain-layer business constraints (e.g., duplicate VIN registration) cleanly translate into standard HTTP status codes (`409 Conflict`, `404 Not Found`, `422 Unprocessable Entity`).
- **Zero-Side-Effect Unit Testing:** High-speed `pytest` suite running against an in-memory SQLite database (`:memory:`) with dynamic monkeypatching for test isolation without disk pollution.
- **Interactive Documentation:** Auto-generated interactive OpenAPI docs available via Swagger UI and ReDoc.

---

## Architecture Overview

```text
               [ HTTP Client / Frontend / Mobile App ]
                                  │
                                  ▼
                       [ api.py (FastAPI Routes) ]
                        ├── Request Validation (Pydantic DTOs)
                        └── HTTP Status & Error Mapping
                                  │
                                  ▼
                     [ services.py (Business Logic) ]
                        ├── Domain Rules & Validation
                        └── Operations Orchestration
                                  │
                                  ▼
                    [ storage.py (Persistence Layer) ]
                        ├── Schema Initialization
                        └── Raw SQL Queries (SQLite3)
```

---

## Tech Stack

| Component | Technology | Purpose |
| :--- | :--- | :--- |
| **Language** | Python 3.10+ | Core runtime |
| **Framework** | FastAPI | High-performance asynchronous-ready web framework |
| **Validation** | Pydantic v2 | Data modeling, typing enforcement, and schema validation |
| **Database** | SQLite3 | Embedded SQL database (modular design ready for PostgreSQL) |
| **Testing** | Pytest | Test suite with isolated in-memory database fixtures |
| **ASGI Server** | Uvicorn | Lightning-fast ASGI web server |

---

## Project Structure

```text
car_tracker/
├── api.py            # Presentation layer: REST endpoints and DTO schemas
├── services.py       # Domain layer: Business logic and validation rules
├── storage.py        # Persistence layer: SQLite database operations and schemas
├── tests/
│   ├── conftest.py   # Pytest fixtures and isolated in-memory DB configuration
│   └── test_services.py # Unit test suite covering core operations & edge cases
├── .gitignore        # Git ignore specifications
├── requirements.txt  # Project dependency manifest
└── README.md         # Architecture and API documentation
```

---

## API Specification

| Method | Endpoint | Description | Status Codes |
| :--- | :--- | :--- | :--- |
| `GET` | `/cars` | Retrieve all vehicles (optional filter: `?status_filter=free`) | `200 OK` |
| `GET` | `/cars/{vin}` | Retrieve a specific vehicle by its VIN | `200 OK`, `404 Not Found` |
| `POST` | `/cars` | Register a new vehicle in the fleet | `201 Created`, `409 Conflict`, `422 Unprocessable Entity` |
| `PATCH` | `/cars/{vin}/status` | Update status (`free`, `in_use`, `maintenance`) | `200 OK`, `404 Not Found` |
| `DELETE` | `/cars/{vin}` | Remove a vehicle from registry | `200 OK`, `404 Not Found` |

### Example Request (`POST /cars`)

```json
{
  "vin": "VIN456",
  "brand": "BMW",
  "model": "X5",
  "status": "free",
  "latitude": 52.23,
  "longitude": 19.52
}
```

### Example Response (`201 Created`)

```json
{
  "vin": "VIN456",
  "brand": "BMW",
  "model": "X5",
  "status": "free",
  "latitude": 52.23,
  "longitude": 19.52
}
```

---

## Getting Started

### Prerequisites

- Python 3.10+
- Git

### Installation & Run

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Din0o104/car-transport-tracker.git](https://github.com/Din0o104/car-transport-tracker.git)
   cd car-transport-tracker
   ```

2. **Create and activate a virtual environment:**
   ```powershell
   # Windows (PowerShell)
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1

   # Linux / macOS
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run development server:**
   ```bash
   python -m uvicorn api:app --reload
   ```

5. **Explore interactive documentation:**
   - **Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - **ReDoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## Running Automated Tests

Run the test suite against an isolated in-memory database:

```bash
python -m pytest -v
```

Expected output:
```text
tests/test_services.py::test_add_car PASSED                              [ 16%]
tests/test_services.py::test_add_car_duplicate_vin_raises_error PASSED   [ 33%]
tests/test_services.py::test_get_cars PASSED                             [ 50%]
tests/test_services.py::test_get_car_not_found PASSED                    [ 66%]
tests/test_services.py::test_update_status PASSED                        [ 83%]
tests/test_services.py::test_delete_car PASSED                           [100%]
============================== 6 passed in 0.04s ===============================
```

---

## Roadmap

- [ ] Add integration test suite for REST API endpoints using FastAPI `TestClient`.
- [ ] Containerize application via `Dockerfile` and `docker-compose.yml`.
- [ ] Add `trips` entity with relational foreign keys for route history.
- [ ] Set up GitHub Actions CI pipeline for automated linting and test execution.

---

## License

This project is licensed under the [MIT License](LICENSE).