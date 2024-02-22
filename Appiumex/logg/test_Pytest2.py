'''import pytest

@pytest.mark.run(order=3)
def test_methodC():
    print("This is method C")

@pytest.mark.run(order=4)
def test_methodD():
    print("This is method D")

@pytest.mark.run(order=1)
def test_methodA():
    print("This is method A")

@pytest.mark.run(order=2)
def test_methodB():
    print("This is method B")'''
import pytest

@pytest.mark.order(2)
def test_second():
    assert 2 + 2 == 4

@pytest.mark.order(1)
def test_first():
    assert 1 + 1 == 2

@pytest.mark.order(3)
def test_third():
    assert 3 * 3 == 9
