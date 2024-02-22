import unittest
import pytest
import time
from SeleniumFrameWork.base.BasePage import BaseClass
from SeleniumFrameWork.pages.navigation_burger import BurgerMenu
import SeleniumFrameWork.utilities.customLogger as cl

@pytest.mark.usefixtures("beforeClass","beforeMethod")
class BurgerMenuTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.bm = BurgerMenu(self.driver)
        self.bp = BaseClass(self.driver)

    @pytest.mark.run(order=30)
    def test_login(self):
        self.bm.enterName()
        time.sleep(3)
        self.bm.enterPassword()
        time.sleep(3)
        self.bm.clickOnLogin()

    @pytest.mark.run(order=31)
    def test_navigate(self):
        time.sleep(1)
        self.bm.navigate_to_burger_menu()
        time.sleep(3)

    @pytest.mark.run(order=32)
    def test_selectall_Items(self):
        time.sleep(3)
        self.bm.all_items_menu()
        time.sleep(4)

    @pytest.mark.run(order=33)
    def test_selectabout_menu(self):
        self.bm.about_menu()
        time.sleep(3)

    @pytest.mark.run(order=34)
    def test_selectwebsite_menu(self):
        self.bm.website_menu()
        time.sleep(3)














