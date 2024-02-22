import unittest
import pytest
import time
from SeleniumFrameWork.base.BasePage import BaseClass
from SeleniumFrameWork.pages.LoginPage import LoginPage
import SeleniumFrameWork.utilities.customLogger as cl


@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class LoginTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.lp = LoginPage(self.driver)
        self.bp = BaseClass(self.driver)

    @pytest.mark.run(order=1)
    def test_verify_login(self):
        self.lp.verify_login_page()
        time.sleep(3)

    @pytest.mark.run(order=3)
    def test_logout(self):
        time.sleep(3)
        self.lp.clickOnMenuButton()
        time.sleep(3)
        self.lp.clickOnLogoutButton()

    @pytest.mark.run(order=2)
    def test_login(self):
        self.lp.giveUserName()
        time.sleep(3)
        self.lp.givePassword()
        time.sleep(3)
        self.lp.clickOnLogin()
        time.sleep(3)

    @pytest.mark.run(order=4)
    def test_loginWrong(self):
        self.lp.give_wrong_UserName()
        time.sleep(3)
        self.lp.give_wrong_Password()
        time.sleep(3)
        self.lp.clickOnLogin()
        time.sleep(3)
        # self.lp.verify_Wrong_UserName_Password()
        # time.sleep(3)

    @pytest.mark.run(order=5)
    def test_verify_wrong_login(self):
        self.lp.verify_Wrong_UserName_Password()
        time.sleep(3)

    @pytest.mark.run(order=6)
    def test_refreshPage(self):
        time.sleep(3)
        self.lp.refreshPage()

    @pytest.mark.run(order=7)
    def test_loginBlank(self):
        # self.lp.giveUserName()
        # time.sleep(3)
        # self.lp.givePassword()
        time.sleep(3)
        self.lp.clickOnLogin()
        time.sleep(3)
        self.lp.verify_blank_username_password()
        time.sleep(3)
