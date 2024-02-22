def test_methodA():
    print("This is method A")
def test_methodB():
    print("This is method B")

# py.test -v -s
# py.test -v -s test_Ex1.py                 ----particular py file
# py.test -v -s .test_Ex1.py::test_methodB  -----particular method of selected py file

