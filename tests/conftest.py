import sqlite3
import pytest
import storage


@pytest.fixture(autouse=True)
def clean_db(monkeypatch):
    """Изолированная база в памяти, доступная для потоков FastAPI."""
    conn = sqlite3.connect(":memory:", check_same_thread=False)
    monkeypatch.setattr(storage, "get_connection", lambda: conn)
    storage.init_db()
    yield
    conn.close()