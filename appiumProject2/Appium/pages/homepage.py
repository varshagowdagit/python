from Appium.base.base_page import BasePage
import Appium.utilities.CustomLogger as cl
class Homepage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver=driver

    _searchButton = "search"  #des
    _notification = "notification" #des
    _home= "Home" #text
    _hottrends="Hot Trends"#text
    _everydaydeals="Everyday"#text
    _myntraluxe="Luxe"#text
    _profile="Profile"#text

    def verifySearchButton(self):
        self.is_displayed(self._searchButton,"des")
        cl.allureLogs("verified the search button")

    def clickSearchButton(self):
        self.click_element(self._searchButton,"des")
        cl.allureLogs("clicked on search button")

    def verifynotificationIcon(self):
        self.is_displayed(self._notification,"des")
        cl.allureLogs("verified the presence of search button")

    def clickNotificationIcon(self):
        self.click_element(self._notification,"des")
        cl.allureLogs("clicked on notification button")

    def verifyhomeIcon(self):
        self.is_displayed(self._home,"text")
        cl.allureLogs("verified the presence of home icon")

    def clickHomeIcon(self):
        self.click_element(self._home,"text")
        cl.allureLogs("clicked on home icon")

    def verifyHotTrends(self):
        self.is_displayed(self._hottrends,"text")
        cl.allureLogs("verified presence of hot trends")

    def clickHotTrends(self):
        self.click_element(self._hottrends,"text")
        cl.allureLogs("clicked on hot trends icon ")

    def verifyEveryDayDeals(self):
        self.is_displayed(self._everydaydeals,"text")
        cl.allureLogs("verified everyday deals button")

    def clickEverydayDeals(self):
        self.click_element(self._everydaydeals,"text")
        cl.allureLogs("clicked on everyday deals button")

    def verifyMyntraLuxe(self):
        self.is_displayed(self._myntraluxe,"text")

    def clickMyntraLuxe(self):
        self.click_element(self._myntraluxe,"text")

    def verifyprofileIcon(self):
        self.is_displayed(self._profile,"text")

    def clickProfileIcon(self):
        self.click_element(self._profile,"text")

    def verify_notification_button(self):
        self.is_displayed(self._notification,"des")
        self.click_element(self._notification,"des")
