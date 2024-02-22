"""
Module-level docstring explaining the purpose of the module.
"""
import time
import unittest
import pytest
from appium.webdriver.common.appiumby import AppiumBy
from Appium.base.driver_class import Driver
import Appium.utilities.CustomLogger as cl
from Appium.base.base_page import BasePage
from Appium.pages.searchPage import MyntraPage1

# @pytest.mark.usefixtures("theClass","theMethod")
@pytest.mark.usefixtures("driver_setup")
class MyntraP1(unittest.TestCase):
    """
    Test case class for MyntraPage1.
    """
    @pytest.fixture(autouse=True)
    def class_objects(self):
        """Set up class objects and attributes"""
        self.mp = MyntraPage1(self.driver)

    @pytest.mark.run(order=2)
    def test_enter_required_element(self):
        self.mp.typeTextInSearchButton()
        self.mp.selectTshirtsforWomen()

    @pytest.mark.run(order=1)
    def test_open_search_button(self):
        time.sleep(6)
        cl.allureLogs("App launched")
        # self.mp.verifySearchButton()
        self.mp.clickSearchButton()

    @pytest.mark.run(order=3)
    def test_apply_filters(self):
        self.mp.applyFilter()

    @pytest.mark.run(order=4)
    def test_apply_color_filter(self):
        self.mp.applyColor()
        self.mp.applyBlackColor()
        self.mp.clickOnAPPLY()

    @pytest.mark.run(order=5)
    def test_select_product(self):
        self.mp.selectRequiredProduct()

    @pytest.mark.run(order=6)
    def test_screenshot_of_product(self):
        self.mp.takeScreenshotofTheProduct()

    @pytest.mark.run(order=7)
    def test_select_size_and_add_to_Bag(self):
        self.mp.selectsizenAddtoCart()
