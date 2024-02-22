from AppiumFramework.base.BasePage import BasePage

class ContactUs(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver=driver

    _contactFormButton = "com.code2lead.kwad:id/ContactUs" #id
    _enterName="Enter Name" #text
    _enterAddress="Enter Address" #text
    _enterMobNumber="4" #index number
    _enterEmail="Enter Email" #text
    _submitButton="SUBMIT" #text
    _pageTitle="Contact Page"#text

    def clickContactFormButton(self):
        self.clickElement(self._contactFormButton,"id")

    def verifyContactPage(self):
        element=self.isDisplayed(self._pageTitle,"text")
        assert element==True

    def enterName(self):
        self.sendText("Varsha",self._enterName,"text")
    def enterAddress(self):
        self.sendText("Bangalore",self._enterAddress,"text")
    def enterEmail(self):
        self.sendText("Varshagowda@gmail.com",self._enterEmail,"text")
    def enterMobileNumber(self):
        self.sendText("234567890",self._enterMobNumber,"index")
    def clickSubmit(self):
        self.clickElement(self._submitButton,"text")
