from SeleniumFrameWork.base.BasePage import BaseClass


class LoginPage(BaseClass):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    # locators value in login page

    _usernamebutton = 'user-name'  # id
    _username = 'user-name'  # id
    _password = 'password'  # id
    _loginbutton = 'login-button'  # id
    _menu = 'react-burger-menu-btn'  # id
    _logoutbutton = 'logout_sidebar_link'  # id
    _VerifyPage = 'login_button_container'  # id
    _Errormsg = '//*[@id="login_button_container"]/div/form/div[3]/h3'
    _blankspace_error = '//*[@id="login_button_container"]/div/form/div[3]'

    def verify_login_page(self):
        self.isElementDisplayed(self._VerifyPage, "id")

    def giveUserName(self):
        self.sendText("standard_user", self._username, "id")

    def givePassword(self):
        self.sendText("secret_sauce", self._password, "id")

    def clickOnLogin(self):
        self.clickOnElement(self._loginbutton, "id")

    def clickOnMenuButton(self):
        self.clickOnElement(self._menu, "id")

    def clickOnLogoutButton(self):
        self.clickOnElement(self._logoutbutton, "id")

    def give_wrong_UserName(self):
        self.sendText("monalisa", self._username, "id")

    def give_wrong_Password(self):
        self.sendText("monalisa@123", self._password, "id")

    def verify_Wrong_UserName_Password(self):
        self.isElementDisplayed(self._Errormsg, "xpath")

    def verify_blank_username_password(self):
        self.isElementDisplayed(self._blankspace_error, "xpath")

    def refreshPage(self):
        self.driver.refresh()

