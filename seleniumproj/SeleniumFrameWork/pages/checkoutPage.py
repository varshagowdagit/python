from SeleniumFrameWork.base.BasePage import BaseClass
import SeleniumFrameWork.utilities.customLogger as cl
import re
class Checkout(BaseClass):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver



    # locators value in login page
    _usernamebutton = 'user-name' #id
    _username = 'user-name' #id
    _password = 'password' #id
    _loginbutton = 'login-button' #id
    _VerifyPage ='login_button_container' #id
    _AddtoCart ='add-to-cart-sauce-labs-backpack' #id
    _CartLink = 'shopping_cart_link' #class
    _CheckOut = 'checkout' #id
    _EnterYourFirstName = 'first-name' #id
    _EnterYourLastName = 'last-name' #id
    _EnterPinCode = 'postal-code' # id
    _PressContinue = 'continue' # id
    _finish = 'finish' #id


    def verify_login_page(self):
        self.isElementDisplayed(self._VerifyPage, "id")
        cl.allureLogs("the web page is verified")

    def giveUserName(self):
        self.sendText("standard_user",self._username, "id")
        cl.allureLogs("entered username successfully")

    def givePassword(self):
        self.sendText("secret_sauce",self._password, "id")
        cl.allureLogs("password have been successfully fetched ")

    def clickOnLogin(self):
        self.clickOnElement(self._loginbutton,"id")
        cl.allureLogs("clicked login button")

    def addtoCart(self):
        self.clickOnElement(self._AddtoCart,"id")
        cl.allureLogs("the product is added to the cart successfully")

    def openCart(self):
        self.clickOnElement(self._CartLink, "class")
        cl.allureLogs("checking the added product into the cart")

    def checkOut(self):
        self.clickOnElement(self._CheckOut,'id')
        cl.allureLogs("verify checkout")

    def firstName(self):
        self.sendText("Robart",self._EnterYourFirstName,'id')
        cl.allureLogs("enter buyers first name")

    def lastName(self):
        self.sendText("junior",self._EnterYourLastName,'id')
        cl.allureLogs("enter buyers lastname")

    def pinCode(self):
        pattern = r'^\d{1,6}$'  # Corrected the regular expression pattern
        entered_pincode = 560055
        self.clickOnElement(self._EnterPinCode, 'id')
        if re.match(pattern, str(entered_pincode)):  # Corrected the usage of re.match()
            self.sendText(str(entered_pincode), self._EnterPinCode, 'id')  # Converted uip to string
            cl.allureLogs("enter postal code")
        else:
            self.log.error("invalid pincode")

    def PressContinue(self):
        self.clickOnElement(self.PressContinue, 'id')
        cl.allureLogs("enter continue to complete order")

    def pressFinal(self):
        self.clickOnElement(self._finish, 'id')
        cl.allureLogs("finish the order after checking the entered coustomer's details.")
