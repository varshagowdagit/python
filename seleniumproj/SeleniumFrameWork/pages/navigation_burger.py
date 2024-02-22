from SeleniumFrameWork.base.BasePage import BaseClass
#import SeleniumFrameWork.utilities.customLogger as cl
import time

class BurgerMenu(BaseClass):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators values in Burgerpage
    _username="user-name" #id
    _password="password" #id
    _login="login-button"#id
    _navigate="bm-burger-button"#class
    _allitems="inventory_sidebar_link"
    _about="about_sidebar_link"
    _website="onetrust-accept-btn-handler"
    _scroll_click_sauce="MuiTypography-root MuiTypography-h6 css-1jgtbl0"#class

    def enterName(self):
        self.sendText("standard_user", self._username, "id")

    def enterPassword(self):
        self.sendText("secret_sauce", self._password, "id")

    def clickOnLogin(self):
        self.clickOnElement(self._login, "id")

    """navigation of burgermenu from homepage"""
    def navigate_to_burger_menu(self):
        self.clickOnElement(self._navigate, "class")
        time.sleep(2)

    """Clicking all items in burgermenu"""
    def all_items_menu(self):
        self.clickOnElement(self._allitems,"id")
        time.sleep(2)

    """Clicking about menu in burgermenu"""
    def about_menu(self):
        self.clickOnElement(self._about,"id")
        time.sleep(2)

    """Clicking ok when website menu opens"""
    def website_menu(self):
        self.clickOnElement(self._website, "id")
        time.sleep(2)

    #def scrolling_clicking_sauce(self):
       # self.clickOnElement(self._scroll_click_sauce, "id")
       # time.sleep(2)













