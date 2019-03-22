import pytest


def test_methodA(set_up):
    print("demo1 method A")


def test_methodB(set_up):
    print("demo1 method B")

@pytest.fixture()
def set_up():
    print("Set up demo1")