from SeleniumFrameWork.base.BasePage import BaseClass
import SeleniumFrameWork.utilities.customLogger as cl
import time
class CartPage(BaseClass):
    """
    Represents the Cart Page with methods for interacting with the cart functionality.

    This class inherits from the BaseClass, providing common functionality for handling web pages.

    Parameters:
    - driver: WebDriver instance

    Attributes:
    - _username (str): Locator for the username field (id)
    - _password (str): Locator for the password field (id)
    - _login (str): Locator for the login button (id)
    - _add_to_cart1 to _add_to_cart4 (str): Locators for adding items to the cart (id)
    - _remove_from_cart1 to _remove_from_cart4 (str): Locators for removing items from the cart (id)
    - _cart (str): Locator for the shopping cart link (class)
    - _continue_shopping (str): Locator for the 'Continue Shopping' button (id)

    Methods:
    - enterName(): Enter username into the username field.
    - enterPassword(): Enter password into the password field.
    - clickOnLogin(): Click on the Login button.
    - addToCart(): Add items to the shopping cart.
    - goToCart(): Navigate to the shopping cart page.
    - removeFromCart(): Remove items from the shopping cart.
    - verifyContinueShopping(): Verify if the 'Continue Shopping' button is displayed.
    - continueShopping(): Click on the 'Continue Shopping' button.
    """

    def __init__(self, driver):
        """
        Constructor for CartPage class.

        Parameters:
        - driver: WebDriver instance
        """
        super().__init__(driver)
        self.driver = driver

    _username="user-name" #id
    _password="password" #id
    _login="login-button"#id
    _add_to_cart1="add-to-cart-sauce-labs-backpack"#id
    _add_to_cart2="add-to-cart-sauce-labs-bike-light"#id
    _add_to_cart3="add-to-cart-sauce-labs-bolt-t-shirt"#id
    _add_to_cart4="add-to-cart-sauce-labs-fleece-jacket"#id
    _remove_from_cart1="remove-sauce-labs-backpack"#id
    _remove_from_cart2="remove-sauce-labs-bike-light"#id
    _remove_from_cart3="remove-sauce-labs-bolt-t-shirt"#id
    _remove_from_cart4="remove-sauce-labs-fleece-jacket"#id
    _cart= "shopping_cart_link"#classname
    _continue_shopping="continue-shopping"#id
    def enterName(self):
         """
    Enter the username into the designated field.

    This method uses the 'sendText' method to input the username into the specified username field.

    Parameters:
    - None

    Returns:
    - None
    """
         self.sendText("standard_user", self._username, "id")
         cl.allureLogs("Entered username")
    def enterPassword(self):
        """
    Enter the password into the designated field.

    This method uses the 'sendText' method to input the password into the specified password field.

    Parameters:
    - None

    Returns:
    - None
    """
        self.sendText("secret_sauce",self._password,"id")
        cl.allureLogs("Entered Password")
    def clickOnLogin(self):
        """
    Click on the Login button.

    Parameters:
    - None

    Returns:
    - None
    """
        self.clickOnElement(self._login,"id")
        cl.allureLogs("Clicked on Login")
    def addToCart(self):
        """
    Add items to the shopping cart.

    This method clicks on each 'Add to Cart' button, with a delay between each click.

    Parameters:
    - None

    Returns:
    - None
    """
        self.clickOnElement(self._add_to_cart1,"id")
        time.sleep(3)
        self.clickOnElement(self._add_to_cart2,"id")
        time.sleep(3)
        self.clickOnElement(self._add_to_cart3,"id")
        time.sleep(3)
        self.clickOnElement(self._add_to_cart4,"id")
        time.sleep(3)
        cl.allureLogs("Clicked on add to cart")
    def goToCart(self):
        """
    Navigate to the shopping cart page.

    Parameters:
    - None

    Returns:
    - None
    """
        self.clickOnElement(self._cart,"class")
        cl.allureLogs("Clicked on go to cart")
    def removeFromCart(self):
        """
    Remove items from the shopping cart.

    This method clicks on each 'Remove from Cart' button, with a delay between each click.

    Parameters:
    - None

    Returns:
    - None
    """
        self.clickOnElement(self._remove_from_cart1,"id")
        time.sleep(3)
        self.clickOnElement(self._remove_from_cart2,"id")
        time.sleep(3)
        self.clickOnElement(self._remove_from_cart3,"id")
        time.sleep(3)
        self.clickOnElement(self._remove_from_cart4,"id")
        time.sleep(3)
        cl.allureLogs("Clicked on remove from cart")
    def verifyContinueShopping(self):
        """
    Verify if the 'Continue Shopping' button is displayed.

    Parameters:
    - None

    Returns:
    - None
    """
        element = self.isElementDisplayed(self._continue_shopping, "id")
        assert element == True
        cl.allureLogs("Verified continue shopping")
    def continueShopping(self):
        """
    Click on the 'Continue Shopping' button.

    Parameters:
    - None

    Returns:
    - None
    """
        self.clickOnElement(self._continue_shopping,"id")
        cl.allureLogs("Clicked on continue shopping")

