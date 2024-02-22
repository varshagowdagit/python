import unittest
import pytest
import time
from SeleniumFrameWork.base.BasePage import BaseClass
import SeleniumFrameWork.utilities.customLogger as cl
from SeleniumFrameWork.pages.scrollPage import AddToCartPage

@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class AddCartTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.ac = AddToCartPage(self.driver)
        self.bp = BaseClass(self.driver)

    @pytest.mark.run(order=8)
    def test_enterDetails(self):
        self.ac.enterUsername()
        self.ac.enterPassword()
        self.ac.clickLoginButton()

    @pytest.mark.run(order=9)
    def test_productPage(self):
        self.ac.verifyProductPage()

    @pytest.mark.run(order=10)
    def test_addToCart(self):
        self.ac.addBackPack()
        time.sleep(2)
        self.ac.addBikeLight()
        time.sleep(2)
        self.ac.addTShirt()
        time.sleep(2)
        self.ac.addCasualJacket()
        time.sleep(2)
        self.ac.addOneSie()
        time.sleep(2)
        self.ac.addTShirtRed()
        time.sleep(2)

    @pytest.mark.run(order=11)
    def test_goToCartPage(self):
        time.sleep(2)
        self.ac.goToCartPage()
