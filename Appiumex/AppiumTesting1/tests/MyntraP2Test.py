from AppiumTesting1.base.DriverClass import Driver
import AppiumTesting1.utilities.CustomLogger as cl
from AppiumTesting1.base.BasePage import BasePage
from AppiumTesting1.pages.Myntra_page2 import MyntraPage2

driver1 = Driver()
log = cl.customLogger()

driver = driver1.getDriverMethod()

mp2 = MyntraPage2(driver)

mp2.selectFilter()
mp2.selectColorFilter()
mp2.selectBlackColorFilter()
mp2.clickApply()
