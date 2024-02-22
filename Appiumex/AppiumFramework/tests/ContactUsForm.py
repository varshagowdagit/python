from AppiumFramework.base.DriverClass import Driver
import AppiumFramework.utilities.CustomLogger as cl
from AppiumFramework.base.BasePage import BasePage
from AppiumFramework.pages.ContactUsFormPage import ContactUs
driver1 = Driver()
log = cl.customLogger()

driver= driver1.getDriverMethod()
log.info("Launch app")

cf=ContactUs(driver)
cf.clickContactFormButton()
cf.enterName()
cf.enterEmail()
cf.enterAddress()
cf.enterMobileNumber()
cf.clickSubmit()

# bp = BasePage(driver)

# element = bp.waitForElement("com.code2lead.kwad:id/ContactUs","id")
# element.click()
# bp.screenShot("App")
# element = bp.isDisplayed("com.code2lead.kwad:id/ContactUs",'id')
# print(element)
# bp.clickElement("com.code2lead.kwad:id/ContactUs",'id')
# bp.sendText("Code2lead","Enter Name", "text")
# #bp.clickElement("com.code2lead.kwad:id/Et3")
# bp.sendText("varsha@gmail.com","Enter Email","text")
# #bp.clickElement("com.code2lead.kwad:id/Et6")
# bp.sendText("Bangalore","Enter Address","text")
# #bp.clickElement("com.code2lead.kwad:id/Et7")
# bp.sendText("9876534567","com.code2lead.kwad:id/Et7","id")
#
# bp.clickElement("com.code2lead.kwad:id/Btn2")
# bp.screenShot("sec_ss")
