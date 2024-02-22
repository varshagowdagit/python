import json
import time
import unittest
import allure
import pytest
from allure_commons.types import AttachmentType
import SeleniumFrameWork.utilities.customLogger as cl
from SeleniumFrameWork.base.BasePage import BaseClass
from SeleniumFrameWork.pages.addCartPage import AddCartTest


@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class CartTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.lp = AddCartTest(self.driver)
        self.bp = BaseClass(self.driver)

    @pytest.mark.run(order=19)
    def test_enterName(self):
        time.sleep(3)
        self.lp.userNameBox()

    @pytest.mark.run(order=18)
    def test_loginPage(self):
        time.sleep(3)
        self.lp.verifyLoginPage()

    @pytest.mark.run(order=20)
    def test_enterPassword(self):
        time.sleep(3)
        self.lp.passwordBox()

    @pytest.mark.run(order=21)
    def test_clickLogin(self):
        time.sleep(3)
        self.lp.loginButton()

    @pytest.mark.run(order=22)
    def test_productPage(self):
        time.sleep(3)
        self.lp.verifyProductPage()

    @pytest.mark.run(order=23)
    def test_addToCart(self):
        time.sleep(3)
        self.lp.addBackPack()
        time.sleep(2)
        self.lp.addBikeLight()
        time.sleep(2)
        self.lp.addTShirt()
        time.sleep(2)
        self.lp.addCasualJacket()
        time.sleep(2)
        self.lp.addOneSie()
        time.sleep(2)
        self.lp.addTShirtRed()
        time.sleep(2)

    @pytest.mark.run(order=24)
    def test_addToCartPage(self):
        time.sleep(2)
        self.lp.goToCartPage()

