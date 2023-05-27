import pytest


@pytest.fixture(scope="module")
def flag():
    return True
