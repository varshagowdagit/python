import time
import Appium.utilities.CustomLogger as cl
from Appium.base.base_page import BasePage

class MyntraPage1(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver=driver

    _searchButton = "search"  #des
    _typeText = "search_default_search_text_input" #des
    _women = "Tshirts For Women" #text
    _filter ="FILTER" #" touchable_filter" #des "FILTER" #text
    _color = "Color" #text
    _blackColor = "Black" #text
    _apply = "APPLY" #text or text_apply#des
    _selectProduct = "Bonkers Corner" #text
    _compareProd="Bonkers Corner Black Printed Mickey Mouse Printed Oversized Cotton Longline T-Shirt"#text
    _size="L"
    _addToBag="ADD TO BAG"
    # _done="DONE"#text "buy_done_button"des

    # def verifySearchButton(self):
    #     self.isDisplayed(self._searchButton,"des")

    def clickSearchButton(self):
        self.tap(341,297)
        cl.allureLogs("clicked on search button")

    def typeTextInSearchButton(self):
        self.send_text("Tshirts",self._typeText,"des")
        cl.allureLogs("text typed in search button")

    def selectTshirtsforWomen(self):
        self.click_element(self._women,"text")
        cl.allureLogs("Selected tshirts for women option among various options displayed")

    def applyFilter(self):
        self.click_element(self._filter,"text")
        cl.allureLogs("clicked on filter")

    def applyColor(self):
        self.click_element(self._color,"text")
        cl.allureLogs("clicked on color filter")

    def applyBlackColor(self):
        self.click_element(self._blackColor,"text")
        cl.allureLogs("selected black color filter ")

    def clickOnAPPLY(self):
        self.click_element(self._apply,"text")
        cl.allureLogs("Applied filter")

    def selectRequiredProduct(self):
        self.scroll_using_scrollable(self._selectProduct)
        self.click_element(self._selectProduct,"text")
        self.is_displayed(self._compareProd,"text")
        cl.allureLogs("searched and clicked on the required product")

    def takeScreenshotofTheProduct(self):
        self.screen_shot("product")
        cl.allureLogs("took a screenshot of the desired product")

    def selectsizenAddtoCart(self):
        self.click_element(self._addToBag,"text")
        self.click_element(self._size,"text")
        self.tap(363,1418)
        cl.allureLogs("added product to bag")






