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

def test_methodA(theClass,theMethod):
    print("This is method A")
def test_methodB(theClass,theMethod):
    print("This is method B")

# py.test -v -s .\test_pythonFixture.py   ------ to execute
