import time

from selenium.webdriver.common.by import By
from SeleniumFrameWork.base.BasePage import BaseClass
import SeleniumFrameWork.utilities.customLogger as cl
from selenium.webdriver.support.ui import Select
class Filter_Dropdown(BaseClass):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators val

    _username = "user-name"  # id
    _password = "password"  # id
    _login = "login-button"   #id
    _filter = "product_sort_container"  #class
    _item0 ="item_0_title_link" #id
    _item1 ="item_1_title_link" #id
    _item2 ="item_2_title_link" #id
    _item3 ="item_3_title_link" #id
    _item4 ="item_4_title_link" #id
    _item5 ="item_5_title_link" #id
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

    def clickOnFilterButton(self):
        #Click on the filter button and wait for the options to be present.
        self.clickOnElement(self._filter,"class")
        cl.allureLogs("clicked on filter button")
        self.waitForElement(self._filter,"class")
        cl.allureLogs("waited for the options present in the filter menu")

    def clickPriceLowToHigh(self):
        #Select the 'Price (Low to high)' filter and scroll from product item1 to item5.
        self.selectDropdownOption(self._filter,"Price (low to high)","class")
        cl.allureLogs("selected low to high filter")
        self.scrollTo(self._item1,"id")
        time.sleep(3)
        self.scrollTo(self._item5,"id")
        cl.allureLogs("scrolled from product item1 to item5")
        time.sleep(3)

    def clickPriceHighToLow(self):
        #Select the 'Price (high to low)' filter and scroll from product item5 to item1.
        self.selectDropdownOption(self._filter,"Price (high to low)","class")
        cl.allureLogs("selected high to low filter")
        self.scrollTo(self._item5,"id")
        time.sleep(3)
        self.scrollTo(self._item1,"id")
        cl.allureLogs("scrolled from product item5 to item1")
        time.sleep(3)

    def clickFilterA_Z(self):
        #Select the 'Name (A to Z)' filter and scroll from product item1 to item3
        self.selectDropdownOption(self._filter,"Name (A to Z)","class")
        cl.allureLogs("selected Name A-Z order filter")
        self.scrollTo(self._item1,"id")
        time.sleep(3)
        self.scrollTo(self._item3,"id")
        cl.allureLogs("scrolled from product item1 to item3")
        time.sleep(3)

    def clickFilterZ_A(self):
        #Select the 'Name (Z to A)' filter and scroll from product item3 to item1
        self.selectDropdownOption(self._filter,"Name (A to Z)","class")
        cl.allureLogs("selected Name Z-A order filter")
        self.scrollTo(self._item3,"id")
        time.sleep(3)
        self.scrollTo(self._item1,"id")
        cl.allureLogs("scrolled from product item3 to item1")



