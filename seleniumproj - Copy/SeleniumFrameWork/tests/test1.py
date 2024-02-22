import time
from SeleniumFrameWork.base.DriverClass import WebDriverClass
from SeleniumFrameWork.base.BasePage import BaseClass
from selenium.webdriver.support.ui import Select
from SeleniumFrameWork.pages.filter import Filter_Dropdown
wd = WebDriverClass()

driver = wd.get_web_driver("chrome")
bp = BaseClass(driver)
fd = Filter_Dropdown(driver)
bp.launchWebPage("https://www.saucedemo.com/","Swag Labs")

fd.enterUsername()
fd.enterPassword()
fd.clickLoginButton()
fd.clickOnFilterButton()

# fd.clickFilterA_Z()
# fd.clickFilterZ_A()
fd.clickPriceLowToHigh()
# fd.clickPriceHighToLow()



# #ele=bp.isElementDisplayed("user-name","id")
# ele=bp.sendText("standard_user","user-name","id")
# ele=bp.sendText("secret_sauce","password","id")
# ele=bp.clickOnElement("login-button","id")
#
#
# ele1=bp.clickOnElement("product_sort_container","class")
# ele1=bp.waitForElement("product_sort_container","class")
# dd_option = Select(ele1)
# dd_v = dd_option.options
# #dd_option.select_by_value("za")
# dd_option.select_by_visible_text("Price (low to high)")
# # # To display the options in output screen
# # for dd_val in dd_v:
# #     print(dd_val.text)

        # filter_dropdown_element = self.driver.find_element(By.CLASS_NAME, self._filter)
        #
        # # Create a Select object
        # filter_dropdown = Select(filter_dropdown_element)
        #
        # # Select an option by visible text
        # filter_dropdown.select_by_visible_text("Price (low to high)")
time.sleep(5)
driver.quit()
