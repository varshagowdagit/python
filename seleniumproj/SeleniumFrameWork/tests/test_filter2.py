import unittest
import pytest
import time
from SeleniumFrameWork.base.BasePage import BaseClass
from SeleniumFrameWork.pages.filterpage2 import Filter_Dropdown

# Using a fixture to set up and tear down resources
@pytest.mark.usefixtures("beforeClass","beforeMethod")
class FilterDropdownTest(unittest.TestCase):

    # Fixture to initialize class objects
    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.fd = Filter_Dropdown(self.driver)
        self.bp = BaseClass(self.driver)

    # Test to click on the filter button
    @pytest.mark.run(order=2)
    def test_clickFilter(self):
        time.sleep(5)
        self.fd.clickOnFilterButton()

    # Test to enter login details
    @pytest.mark.run(order=1)
    def test_enterDetails(self):
        self.fd.enterUsername()
        self.fd.enterPassword()
        self.fd.clickLoginButton()

    # Test to select filter A-Z
    @pytest.mark.run(order=3)
    def test_selectFilterZ_A(self):
        time.sleep(5)
        self.fd.clickFilterZ_A()
        time.sleep(3)

    # Test to select filter A-Z
    @pytest.mark.run(order=4)
    def test_selectFilterA_Z(self):
        self.fd.clickOnFilterButton()
        time.sleep(5)
        self.fd.clickFilterA_Z()
        time.sleep(3)

    # Test to select filter Low to High
    @pytest.mark.run(order=5)
    def test_selectFilterLowToHigh(self):
        self.fd.clickOnFilterButton()
        time.sleep(5)
        self.fd.clickPriceLowToHigh()
        time.sleep(5)

    # Test to select filter High to Low
    @pytest.mark.run(order=6)
    def test_selectFilterHighToLow(self):
        self.fd.clickOnFilterButton()
        time.sleep(5)
        self.fd.clickPriceHighToLow()
