Fleet Transport Tracker API

A lightweight, production-ready REST API for commercial vehicle tracking, telematics, and fleet lifecycle management. Built with FastAPI, Pydantic v2, and SQLite, designed following Layered Architecture principles.



Key Highlights

-Layered Architecture (Separation of Concerns): Strict boundary separation between HTTP transport (api.py), domain business logic (services.py), and persistence (storage.py).

-Strict Data Validation & DTOs:
Incoming payloads and outgoing responses are strictly validated using Pydantic schemas with geographic boundary checks and VIN validation.

-Domain Exception Mapping:
Business-layer constraints (such as duplicate VIN conflicts) cleanly translate into standard HTTP status codes (409 Conflict, 404 Not Found, 422 Unprocessable Entity).

-Zero-Side-Effect Unit Testing:
High-speed pytest suite utilizing an in-memory SQLite database (:memory:) and dynamic monkeypatching, running tests in sub-second time without disk pollution.

-Interactive OpenAPI Documentation:
Fully documented interactive Swagger UI and ReDoc generated automatically on startup.



Architecture Overview

[ HTTP Client / Browser / Mobile App ]
                 │
                 ▼
      [ api.py (FastAPI Routes) ]
       ├── Request Validation (Pydantic DTOs)
       └── HTTP Error Translation (HTTPException)
                 │
                 ▼
      [ services.py (Business Logic) ]
       ├── Domain Rules & Validation
       └── Orchestration
                 │
                 ▼
      [ storage.py (Persistence Layer) ]
       ├── Schema Migration / Initialization
       └── Raw SQL Queries (SQLite / DB Engine)



Tech Stack
-Component          Technology              Description
 Language           Python 3.10+            Core programming language
 Framework          FastAPI                 High-performance asynchronous-ready
 web framework      ValidationPydantic v2   Data parsing, type enforcement, and schema validation
 Database           SQLite3                 Embedded SQL database (designed for pluggable PostgreSQL)
 Testing            Pytest                  Automated test framework with in-memory fixtures
 Server             Uvicorn                 Lightning-fast ASGI server implementation
 
 
  
Project Structure

car_tracker/
├── api.py               # Presentation layer: REST endpoints and route definitions
├── services.py          # Domain layer: Business logic, domain invariants, validations
├── storage.py           # Persistence layer: Database connection, queries, and schema
├── tests/
│   ├── conftest.py      # Pytest fixtures and isolated in-memory DB setups
│   └── test_services.py # Unit tests covering happy paths and edge cases
├── .gitignore           # Git ignore rules for virtual environments, caches, and DB files
├── requirements.txt     # Explicit project dependency list
└── README.md            # Project documentation and setup guide



API Endpoints Specification

Method          Endpoint                Description                                         StatusCodes
GET             /cars                   Retrieve all vehicles (optional status_filter)      200 OK
GET             /cars/{vin}             Retrieve a specific vehicle by its VIN              200 OK, 404 Not Found
POST            /cars                   Register a new vehicle in the fleet                 201 Created, 409 Conflict, 422 Unprocessable Entity
PATCH           /cars/{vin}/status      Update vehicle status (free, maintenance, etc.)     200 OK, 404 Not Found
DELETE          /cars/{vin}             Remove a vehicle from the fleet registry            200 OK, 404 Not Found



Getting Started

Prerequisites:
Python 3.10 or higher
Git


Installation & Local Run

1. Clone the repository:
git clone https://github.com/Din0o104/car-transport-tracker.git
cd car-transport-tracker

2. Create and activate a virtual environment:
# Windows (PowerShell)
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# Linux / macOS
python3 -m venv .venv
source .venv/bin/activate

3. Install dependencies:
pip install -r requirements.txt

4. Launch the development server:
python -m uvicorn api:app --reload

5. Access the API:
Interactive Swagger Documentation: http://127.0.0.1:8000/docs
Alternative ReDoc UI: http://127.0.0.1:8000/redoc



Running Automated Tests



The test suite runs against an isolated, in-memory SQLite database to ensure idempotency and test independence:
python -m pytest -v

Expected output:
tests/test_services.py::test_add_car PASSED                              [ 12%]
tests/test_services.py::test_add_car_duplicate_vin_raises_error PASSED   [ 25%]
tests/test_services.py::test_get_cars PASSED                             [ 37%]
tests/test_services.py::test_get_car_not_found PASSED                    [ 50%]
tests/test_services.py::test_update_status PASSED                        [ 62%]
tests/test_services.py::test_delete_car PASSED                           [ 75%]
...
============================= 8 passed in 0.04s ==============================



Roadmap
[ ] Add trips entity with a foreign key relation to cars and trip history tracking.
[ ] Containerize application via multi-stage Dockerfile and docker-compose.yml.
[ ] Introduce asynchronous database layer with PostgreSQL and SQLAlchemy Core.
[ ] Configure GitHub Actions workflow for continuous integration (CI) test execution.



License

This project is open-source and available under the MIT License.