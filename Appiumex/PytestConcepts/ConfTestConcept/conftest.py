import pytest

@pytest.fixture(scope='module')
def theClass():
    print("before class ")
    yield
    print("after class")
@pytest.fixture()
def theMethod():
    print("before method ")
    yield
    print("after method")
