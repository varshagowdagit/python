import unittest
import pytest
import time
from SeleniumFrameWork.base.BasePage import BaseClass
from SeleniumFrameWork.pages.cartpage import CartPage
import SeleniumFrameWork.utilities.customLogger as cl
@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class CartPageTest(unittest.TestCase):
    """
    Test class for CartPage functionality.

    This class contains test methods for login, adding products to the cart, shopping, and related actions.

    Fixtures:
    - beforeClass: Setup actions to be performed before the class.
    - beforeMethod: Setup actions to be performed before each test method.

    Attributes:
    - cp (CartPage): Instance of the CartPage class for testing.
    - bp (BaseClass): Instance of the BaseClass for testing.

    Test Methods:
    - test_login: Test the login functionality.
    - test_products: Test adding products to the cart.
    - test_shopping: Test the shopping cart actions including removal, verification, and continuing shopping.
    """

    @pytest.fixture(autouse=True)
    def classObjects(self):
        """
        Fixture to set up instances of CartPage and BaseClass before each test method.

        Parameters:
        - None

        Returns:
        - None
        """
        self.cp = CartPage(self.driver)
        self.bp = BaseClass(self.driver)

    @pytest.mark.run(order=25)
    def test_login(self):
        """
        Test the login functionality.

        This test case covers the login process.

        Parameters:
        - None

        Returns:
        - None
        """
        self.cp.enterName()
        time.sleep(3)
        self.cp.enterPassword()
        time.sleep(3)
        self.cp.clickOnLogin()

    @pytest.mark.run(order=26)
    def test_products(self):
        """
        Test adding products to the cart.

        This test case covers the process of adding products to the cart.

        Parameters:
        - None

        Returns:
        - None
        """
        time.sleep(3)
        self.cp.addToCart()
        time.sleep(3)

    @pytest.mark.run(order=27)
    def test_shopping(self):
        """
        Test shopping cart actions.

        This test case covers actions like going to the cart, removing items, verifying, and continuing shopping.

        Parameters:
        - None

        Returns:
        - None
        """
        time.sleep(3)
        self.cp.goToCart()
        time.sleep(3)
        self.cp.removeFromCart()
        time.sleep(3)
        self.cp.verifyContinueShopping()
        time.sleep(3)
        self.cp.continueShopping()
