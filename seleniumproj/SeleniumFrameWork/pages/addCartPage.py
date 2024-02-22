from SeleniumFrameWork.base.BasePage import BaseClass
import SeleniumFrameWork.utilities.customLogger as cl

class AddCartTest(BaseClass):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators values in login page
    _login_page = "login_button_container"  # id
    _enterName = "user-name"  # id
    _enterPassword = "password"  # id
    _clickLogin = "login-button"  # id

    _productPage = "inventory_container" # id
    _backPack = "add-to-cart-sauce-labs-backpack" # id
    _bikeLight = "add-to-cart-sauce-labs-bike-light" # id
    _tShirt = "add-to-cart-sauce-labs-bolt-t-shirt" # id
    _casualJacket = "add-to-cart-sauce-labs-fleece-jacket" # id
    _oneSie = "add-to-cart-sauce-labs-onesie" # id
    _tShirtRed = "add-to-cart-test.allthethings()-t-shirt-(red)" # id
    _goToCart = "shopping_cart_container" # id

    def verifyLoginPage(self):
        element = self.isElementDisplayed(self._login_page, "id")
        assert element == True
        cl.allureLogs("Verified Login Page")

    def userNameBox(self):
        self.sendText("standard_user", self._enterName, "id")
        cl.allureLogs("Name are Entered")

    def passwordBox(self):
        self.sendText("secret_sauce", self._enterPassword, "id")
        cl.allureLogs("Password are Entered")

    def loginButton(self):
        self.clickOnElement(self._clickLogin, "id")
        cl.allureLogs("clicked on Login Button")

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
