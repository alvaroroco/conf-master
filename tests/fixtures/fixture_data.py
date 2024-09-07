import pytest


@pytest.fixture
def config_data():
    return {"database": {"host": "localhost", "port": 5432}, "debug": True}


@pytest.fixture
def schema():
    return {"database.host": str, "database.port": int, "debug": bool}
