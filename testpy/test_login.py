import pytest


@pytest.fixture()
def set_up():
    print("before login setup")
    yield
    print("After login setup")

def test_login(set_up):
    print("Method login")
