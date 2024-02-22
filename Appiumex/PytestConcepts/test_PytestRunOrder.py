# import pytest
#
#
# @pytest.mark.run(order=3)
# def test_methodA():
#     print("This is method A")
#
#
# @pytest.mark.run(order=4)
# def test_methodB():
#     print("This is method B")
#
#
# @pytest.mark.run(order=1)
# def test_methodC():
#     print("This is method C")
#
#
# @pytest.mark.run(order=2)
# def test_methodD():
#     print("This is method D")


import pytest


@pytest.mark.run(order=4)
def test_method1():
    print("this is method1")


@pytest.mark.run(order=2)
def test_method2():
    print("this is method2")


@pytest.mark.run(order=1)
def test_method3():
    print("this is method3")


@pytest.mark.run(order=3)
def test_method4():
    print("this is method4")