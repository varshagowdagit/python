from SeleniumFrameWork.base.BasePage import BaseClass
import SeleniumFrameWork.utilities.customLogger as cl

class AddToCartPage(BaseClass):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _username = 'user-name'  # id
    _password = 'password'  # id
    _login = 'login-button'
    _productPage = "inventory_container" # id
    _backPack = "add-to-cart-sauce-labs-backpack" # id
    _bikeLight = "add-to-cart-sauce-labs-bike-light" # id
    _tShirt = "add-to-cart-sauce-labs-bolt-t-shirt" # id
    _casualJacket = "add-to-cart-sauce-labs-fleece-jacket" # id
    _oneSie = "add-to-cart-sauce-labs-onesie" # id
    _tShirtRed = "add-to-cart-test.allthethings()-t-shirt-(red)" # id
    _goToCart = "shopping_cart_container" # id

    def enterUsername(self):
        #Enter the username in the username field.
        self.sendText("standard_user", self._username, "id")
        cl.allureLogs("Entered username")

    def enterPassword(self):
        #Enter the password in the password field.
        self.sendText("secret_sauce", self._password, "id")
        cl.allureLogs("Entered password")

    def clickLoginButton(self):
        #Click on the Login button.
        self.clickOnElement(self._login, "id")
        cl.allureLogs("clicked on Login button ")

    def verifyProductPage(self):
        element = self.isElementDisplayed(self._productPage, "id")
        assert element == True

    def addBackPack(self):
        self.clickOnElement(self._backPack, "id")

    def addBikeLight(self):
        self.clickOnElement(self._bikeLight, "id")

    def addTShirt(self):
        self.scrollTo(self._tShirt, "id")
        self.clickOnElement(self._tShirt, "id")

    def addCasualJacket(self):
        self.scrollTo(self._casualJacket, "id")
        self.clickOnElement(self._casualJacket, "id")

    def addOneSie(self):
        self.scrollTo(self._oneSie, "id")
        self.clickOnElement(self._oneSie, "id")

    def addTShirtRed(self):
        self.scrollTo(self._tShirtRed, "id")
        self.clickOnElement(self._tShirtRed, "id")

    def goToCartPage(self):
        self.clickOnElement(self._goToCart, "id")

