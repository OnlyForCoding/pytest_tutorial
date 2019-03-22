import pytest


@pytest.fixture()
def set_up():
    print("before logout setup")
    yield
    print("After logout setup")

def test_logout(set_up):
    print("Method logout")
