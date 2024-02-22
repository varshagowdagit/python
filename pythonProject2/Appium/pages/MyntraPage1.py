from Appium.base.BasePage import BasePage

class MyntraPage1(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver=driver

    _searchButton = "search"  #des
    _typeText = "search_default_search_text_input" #des
    _selectProduct = "search_autosuggest_product_click_1" #text
    def verifySearchButton(self):
        self.isDisplayed(self._searchButton,"des")

    def clickSearchButton(self):
        self.clickElement(self._searchButton,"des")

    def typeTextInSearchButton(self):
        self.sendText("Tshirts",self._typeText,"des")

    def selectRequiredProduct(self):
        self.clickElement(self._selectProduct,"des")
