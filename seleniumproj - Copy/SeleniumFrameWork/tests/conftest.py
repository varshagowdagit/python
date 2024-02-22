import pytest
from SeleniumFrameWork.base.BasePage import BaseClass
from SeleniumFrameWork.base.DriverClass import WebDriverClass
import time

@pytest.fixture(scope='class')
def beforeClass(request):
    print('Before Class')
    driver1 = WebDriverClass()
    driver = driver1.get_web_driver("chrome")
    bp = BaseClass(driver)
    bp.launchWebPage("https://www.saucedemo.com/","Swag Labs")
    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    time.sleep(5)
    driver.quit()
    print('After Class')


@pytest.fixture()
def beforeMethod():
    print('Before Method')
    yield
    print('After Method')
