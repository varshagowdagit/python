import unittest
import pytest
from appium.webdriver.common.appiumby import AppiumBy

from Appium.base.DriverClass import Driver
import Appium.utilities.CustomLogger as cl
from Appium.base.BasePage import BasePage
from Appium.pages.MyntraPage1 import MyntraPage1


@pytest.mark.usefixtures("theClass","theMethod")
class MyntraP1(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.mp = MyntraPage1(self.driver)

    @pytest.mark.run(order=2)
    def test_enterRequiredElement(self):
        self.mp.typeTextInSearchButton()
        self.mp.selectRequiredProduct()

    @pytest.mark.run(order=1)
    def test_openSearchButton(self):
        self.mp.verifySearchButton()
        self.mp.clickSearchButton()











'''log.info("Launch app")

bp = BasePage(driver)
# element = bp.waitForElement("search","des")
# element.click()
bp.clickElement("search","des")
# bp.clickElement("View All","text")
# bp.clickElement("search","des")
bp.sendText("Tshirts","search_default_search_text_input","des")
bp.clickElement("Tshirts For Women","text")
bp.clickElement("  Filters","text")
bp.clickElement("Color","text")
bp.clickElement("Black","text")
bp.clickElement("APPLY","text")
#bp.screenShot("myntra")

bp.scroll_using_scrollable("Barbie Printed Cotton T-Shirts")


# bp.scroll_using_scrollable("XL")
# bp.scroll_using_scrollable("ADD TO BAG")

element_to_swipe = driver.find_element(AppiumBy.ID,"00000000-0000-012c-ffff-ffff00000900")#des
bp.swipe_element_left_to_right(element_to_swipe)
bp.swipe_element_right_to_left(element_to_swipe)'''
