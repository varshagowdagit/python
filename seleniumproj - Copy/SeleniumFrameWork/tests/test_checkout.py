import unittest
import pytest
import time
from SeleniumFrameWork.base.BasePage import BaseClass
import SeleniumFrameWork.utilities.customLogger as cl
from SeleniumFrameWork.pages.checkoutPage import Checkout
log = cl.customLogger()

@pytest.mark.usefixtures("beforeClass","beforeMethod")
class CheckOut(unittest.TestCase):

     @pytest.fixture(autouse=True)
     def classObjects(self):
        self.cf = Checkout(self.driver)
        self.bp = BaseClass(self.driver)

     @pytest.mark.run(order=28)
     def test_verifyFormPage(self):
        self.cf.verify_login_page()
        cl.allureLogs("app launched")

     @pytest.mark.run(order=29)
     def test_ClickUserName(self):
        self.cf.giveUserName()
        time.sleep(5)
        self.cf.givePassword()
        time.sleep(5)
        self.cf.clickOnLogin()
        time.sleep(5)
        self.cf.addtoCart()
        time.sleep(5)
        self.cf.openCart()
        time.sleep(5)
        self.cf.checkOut()
        time.sleep(5)
        self.cf.firstName()
        time.sleep(5)
        self.cf.lastName()
        time.sleep(5)
        self.cf.pinCode()
        time.sleep(5)
        self.bp.scrollTo("continue")
        self.bp.clickOnElement('continue','id')
        time.sleep(5)
        self.cf.pressFinal()
        # self.bp.screenShot("order_placed")
        # time.sleep(5)






