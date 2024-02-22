import time

from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
import Appium.utilities.CustomLogger as cl
from Appium.utilities.CustomLogger import customLogger
from appium.webdriver.common.touch_action import TouchAction

class BasePage:
    log=cl.customLogger()
    def __init__(self,driver):
        self.driver=driver
        self.log= customLogger()

    def waitForElement(self, locatorValue, locatorType):
        locatorType=locatorType.lower()
        element=None
        #wait = WebDriverWait(self.driver,25,poll_frequency=2,ignored_exceptions=[ElementNotVisibleException,ElementNotSelectableException,NoSuchElementException])
        wait = WebDriverWait(self.driver, 25, poll_frequency=1,
                     ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException,
                                         NoSuchElementException])
        if locatorType == "id":
            element = wait.until(lambda x:x.find_element(AppiumBy.ID,locatorValue))
            return element
        elif locatorType == "class":
            element = wait.until(lambda x:x.find_element(AppiumBy.CLASS_NAME,locatorValue))
            return element
        elif locatorType == "des":
            element = wait.until(lambda x:x.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'UiSelector().description("%s")'% (locatorValue)))
            return element
        elif locatorType == "index":
            element = wait.until(lambda x:x.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'UiSelector().index(%d)'% int(locatorValue)))
            return element
        elif locatorType == "text":
            element = wait.until(lambda x:x.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'text("%s")'%locatorValue))
            return element
        elif locatorType == "xpath":
            element = wait.until(lambda x:x.find_element(AppiumBy.XPATH,'("%s")'%(locatorValue)))
            return element
        else:
            self.log.info("Locator value"+locatorValue+"not found")
        return element

    def getElement(self,locatorValue,locatorType="id"):
        element=None
        try:
            locatorType=locatorType.lower()
            element=self.waitForElement(locatorValue,locatorType)
            self.log.info("Element found with locator type: "+locatorType+ "with locator value: " +locatorValue)
        except:
            self.log.info("Element not found with locator type: "+locatorType+ "with locator value: " +locatorValue)

        return element

    def clickElement(self,locatorValue,locatorType="id"):
        element=None
        try:
            locatorType=locatorType.lower()
            element=self.waitForElement(locatorValue,locatorType)
            element.click()
            self.log.info("clicked on Element found with locator type: "+locatorType+ " with locator value: " +locatorValue)
        except:
            self.log.error("unable to click Element not found with locator type: "+locatorType+ " with locator value: " +locatorValue)

    def sendText(self,text,locatorValue,locatorType="id"):
        element=None
        try:
            locatorType=locatorType.lower()
            element=self.waitForElement(locatorValue,locatorType)
            element.send_keys(text)
            self.log.info("send text on Element found with locator type: "+locatorType+ " with locator value: "+locatorValue)
        except:
            self.log.error("unable to send text on Element not found with locator type: "+locatorType+ " with locator value: "+locatorValue)

    def isDisplayed(self,locatorValue,locatorType="id"):
        element=None
        try:
            locatorType=locatorType.lower()
            element=self.waitForElement(locatorValue,locatorType)
            element.is_displayed()
            self.log.info("Element with locator type: "+locatorType+"with locator value: "+locatorValue+" is displayed")
            return True
        except:
            self.log.info("Element with locator type: "+locatorType+ " with locator value: "+locatorValue+" not displayed")
            return False

    def screenShot(self,screenshotName):
        fileName=screenshotName + " " +(time.strftime("%d_%m_%y_%H_%M_%S"))+".png"
        screenshotDirectory = "../screenshots/"
        screenshotPath = screenshotDirectory+fileName
        try:
            self.driver.save_screenshot(screenshotPath)
            self.log.info("Screenshot save to path : "+screenshotPath)
        except:
            self.log.info("Unable to save screenshot to the path:" +screenshotPath)

    def scrollfromBottomToTop(self):
        deviceSize = self.driver.get_window_size()
        screenWidth = deviceSize['width']
        screenHeight = deviceSize['height']
        startx = screenWidth / 2
        endx = screenWidth / 2
        starty = screenHeight * 8 / 9
        endy = screenHeight / 9

        actions = TouchAction(self.driver)
        actions.long_press(None, startx, starty).move_to(None, endx, endy).release().perform()
        self.log.info("Scrolled up")

    def scrollfromTopToBottom(self):
        deviceSize = self.driver.get_window_size()
        screenWidth = deviceSize['width']
        screenHeight = deviceSize['height']
        startx2 = screenWidth / 2
        endx2 = screenWidth / 2
        starty2 = screenHeight / 9  # Corrected value here
        endy2 = screenHeight * 8 / 9

        actions = TouchAction(self.driver)
        actions.long_press(None, startx2, starty2).move_to(None, endx2, endy2).release().perform()
        self.log.info("Scrolled down")

    def scroll_using_scrollable(self,scroll_text):
        try:
            ele= self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().textContains("' + scroll_text + '"))')
            ele.click()
            self.log.info("scrolling is started")
        except Exception as e:
            self.log.error("Error occurred while scrolling: %s", str(e))

    def tap(self, x, y):
        try:
            action = TouchAction(self.driver)
            action.tap(x=x, y=y).perform()
            self.log.info("Tap gesture performed at coordinates: (%d, %d)", x, y)
        except Exception as e:
            self.log.error("Error occurred while performing tap gesture: %s", str(e))

    def swipe_element_right_to_left(self, element):
        start_x = element.location['x'] + int(element.size['width'] * 0.8)
        end_x = element.location['x'] + int(element.size['width'] * 0.2)
        y = element.location['y'] + int(element.size['height'] * 0.5)

        action = TouchAction(self.driver)
        action.press(x=start_x, y=y).move_to(x=end_x, y=y).release().perform()

    def swipe_element_left_to_right(self, element):
        start_x = element.location['x'] + int(element.size['width'] * 0.2)
        end_x = element.location['x'] + int(element.size['width'] * 0.8)
        y = element.location['y'] + int(element.size['height'] * 0.5)

        action = TouchAction(self.driver)
        action.press(x=start_x, y=y).move_to(x=end_x, y=y).release().perform()










