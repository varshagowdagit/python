import pytest
from Appium.base.driver_class import Driver
import time
'''@pytest.fixture(scope='class')
def theClass(request):
    print("before class ")
    driver1 = Driver()
    driver = driver1.getDriverMethod()
    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    time.sleep(5)
    driver.quit()
    print("after class")
@pytest.fixture()
def theMethod():
    print("before method ")
    yield
    print("after method")'''


@pytest.fixture(scope='class')
def driver_setup(request):
    driver1 = Driver()
    driver = driver1.getDriverMethod()
    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    time.sleep(5)
    driver.quit()
