from AppiumTesting1.base.BasePage import BasePage

class MyntraPage2(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver=driver

    _filter =  "Filters" #text
    _color = "Color"
    _black = "Black"
    _apply = "APPLY"

    def selectFilter(self):
        self.clickElement(self._filter,"text")

    def selectColorFilter(self):
        self.clickElement(self._color,"text")

    def selectBlackColorFilter(self):
        self.clickElement(self._black,"text")

    def clickApply(self):
        self.clickElement(self._apply,"text")
