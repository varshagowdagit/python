import unittest
import pytest
from Appium.pages.homepage import Homepage
from Appium.pages.searchPage import MyntraPage1

@pytest.mark.usefixtures("driver_setup")
# @pytest.mark.usefixtures("theClass","theMethod")
class TestHomePage:

    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.hp = Homepage(self.driver)
        self.mp = MyntraPage1(self.driver)

    def test_hot_trends(self):
        self.hp.verifyHotTrends()
        self.hp.clickHotTrends()
        self.driver.press_keycode(67)

    def test_everyday_deals(self):
        self.hp.verifyEveryDayDeals()
        self.hp.clickEverydayDeals()

    def test_luxe(self):
        self.hp.verifyMyntraLuxe()
        self.hp.clickMyntraLuxe()

    def test_profile_icon(self):
        self.hp.verifyprofileIcon()
        self.hp.clickProfileIcon()

    def test_home_button(self):
        self.hp.verifyhomeIcon()
        self.hp.clickHomeIcon()

    def test_notification_button(self):
        self.hp.verify_notification_button()

    def test_search_button(self):
        self.mp.clickSearchButton()
