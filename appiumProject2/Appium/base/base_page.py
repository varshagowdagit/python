"""
contains the library
"""
import time
import allure
import Appium.utilities.CustomLogger as cl
from allure_commons.types import AttachmentType
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.common import ElementNotVisibleException,WebDriverException
from selenium.common import ElementNotSelectableException
from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from Appium.utilities.CustomLogger import customLogger
class BasePage:
    """Base class for page objects.
    This class provides common functionality and methods that can be used
    by other page classes to interact with the web or mobile application.
    Attributes:
        log: An instance of a custom logger for logging messages."""
    log=cl.customLogger()

    def __init__(self,driver):
        self.driver=driver
        self.log= customLogger()
        self.action=TouchAction(self.driver)

    def wait_for_element(self, locator_value, locator_type):
        """Wait for and return an element identified by the provided locator.
    Args:
        locator_value (str): The value of the element's locator.
        locator_type (str): The type of locator.
    Returns:
        WebElement or None: The located element, or None if not found"""
        element=None
        try:
            locator_type=locator_type.lower()

            wait = WebDriverWait(self.driver, 25, poll_frequency=1,
                     ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException,
                                         NoSuchElementException])
            if locator_type == "id":
                element = wait.until(lambda x: x.find_element(AppiumBy.ID, locator_value))

            elif locator_type == "class":
                element = wait.until(lambda x: x.find_element(AppiumBy.CLASS_NAME, locator_value))

            elif locator_type == "des":
                element = wait.until(lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                            f'UiSelector().description("{locator_value}")'))
            elif locator_type == "index":
                element = wait.until(lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                            f'UiSelector().index({int(locator_value)})'))
            elif locator_type == "text":
                element = wait.until(lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                                          f'text("{locator_value}")'))
            elif locator_type == "xpath":
                element = wait.until(lambda x: x.find_element(AppiumBy.XPATH, f'({locator_value})'))
            else:
                self.log.info("Locator value %s not found", locator_value)
        except NoSuchElementException:
            self.log.error("Element not found with locator type: %s and locator value: %s",
                       locator_type, locator_value)
        except WebDriverException as exc:
            self.log.error("WebDriver error occurred while waiting for element: %s", str(exc))

        return element
    def get_element(self, locator_value, locator_type="id"):
        """
    Find and return an element identified by the provided locator.

    Args:
        locator_value (str): The value of the element's locator.
        locator_type (str, optional): The type of locator (default is "id").

    Returns:
        WebElement or None: The located element, or None if not found.
    """
        try:
            locator_type = locator_type.lower()
            element = self.wait_for_element(locator_value, locator_type)
            self.log.info("Element found with locator type: %s with locator value: %s",
                      locator_type, locator_value)
        except NoSuchElementException:
            self.log.error("Element not found with locator type: %s and locator value: %s",
                       locator_type, locator_value)
            element = None
        except WebDriverException as exc:
            self.log.error("WebDriver error occurred while getting element: %s", str(exc))
            element = None
        return element

    def click_element(self,locator_value,locator_type="id"):
        """
    Click on an element identified by the provided locator.
    Args:
        locator_value (str): The value of the element's locator.
        locator_type (str, optional): The type of locator (default is "id").
    Returns:
        None
    """
        element=None
        try:
            locator_type=locator_type.lower()
            element=self.wait_for_element(locator_value,locator_type)
            element.click()
            self.log.info("clicked on Element found with locator type: "+
                          locator_type+ " with locator value: " +locator_value)
        except NoSuchElementException:
            self.log.error("Element not found with locator type: %s and locator value: %s",
                       locator_type, locator_value)
            self.take_screenshot(locator_type)
            assert False
        except WebDriverException as exc:
            self.log.error("WebDriver error occurred while clicking: %s", str(exc))
            self.take_screenshot(locator_type)
            assert False

    def send_text(self,text,locator_value,locator_type="id"):
        """
Send text to an input element found using the provided locator.
    Args:
        text (str): The text to be sent to the input element.
        locator_value (str): The value of the element's locator.
        locator_type (str, optional): The type of locator (default is "id").
    Returns:
        None
        """
        element=None
        try:
            locator_type=locator_type.lower()
            element=self.wait_for_element(locator_value,locator_type)
            element.send_keys(text)
            self.log.info("send text on Element found with locator type: "+
                          locator_type+ " with locator value: "+locator_value)
        except NoSuchElementException:
            self.log.error("Element not found with locator type: %s and locator value: %s",
                       locator_type, locator_value)
            self.take_screenshot(locator_type)
            assert False
        except WebDriverException as exc:
            self.log.error("WebDriver error occurred while sending text: %s", str(exc))
            self.take_screenshot(locator_type)
            assert False

    def is_displayed(self,locator_value,locator_type="id"):
        """
    Check if an element is displayed on the page.

    Args:
        locator_value (str): The value of the element's locator.
        locator_type (str, optional): The type of locator (default is "id").

    Returns:
        bool: True if the element is displayed, False otherwise.
    """
        element=None
        try:
            locator_type=locator_type.lower()
            element=self.wait_for_element(locator_value,locator_type)
            element.is_displayed()
            return True
        except NoSuchElementException:
            self.log.info("Element with locator type: %s with locator value: %s not displayed",
                      locator_type, locator_value)
            return False
        except WebDriverException as exc:
            self.log.error("WebDriver error occurred while checking element visibility: %s"
                           , str(exc))
            return False

    def screen_shot(self, screenshot_name):
        """
        Capture a screenshot and save it to the specified directory.
 Args:
        screenshot_name (str): The base name for the screenshot.
Returns:
        None
    """
        file_name = f"{screenshot_name} {time.strftime('%d_%m_%y_%H_%M_%S')}.png"
        screenshot_directory = "../screenshots/"
        screenshot_path = screenshot_directory + file_name
        try:
            self.driver.save_screenshot(screenshot_path)
            self.log.info("Screenshot saved to path: %s", screenshot_path)
        except WebDriverException as exc:
            self.log.error("Unable to save screenshot to the path: %s", screenshot_path)
            self.log.exception(exc)

    def scroll_using_scrollable(self,scroll_text):
        """
    Scroll to find and click an element with the specified text using scrollable view.

    Args:
        scroll_text (str): The text to search for in the scrollable view.

    Returns:
        None
    """
        try:
            ele= self.driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                '.scrollIntoView(new UiSelector().textContains("' + scroll_text + '"))')
            ele.click()
            self.log.info("scrolling is started")
        except WebDriverException as exc:
            self.log.error("Error occurred while performing tap gesture: %s", str(exc))

    def swipe_right_to_left(self):
        """
    Perform a swipe gesture from right to left on the screen.

    This method simulates a swipe action from the right side of the screen to the left side.
    It uses the self.action object to execute the swipe action.

    Raises:
        ElementNotVisibleException: If an element is not visible.
        ElementNotSelectableException: If an element is not selectable.
        NoSuchElementException: If a required element is not found.
        TimeoutException: If the operation times out.

    Returns:
        None
    """
        try:
        # Get Screen Size
            screen_size = self.driver.get_window_size()
            screen_width = screen_size["width"]
            screen_height = screen_size["height"]

        # Swipe right to left
            start_x2 = screen_width / 9
            end_x2 = screen_width * 8 / 9
            start_y2 = screen_height / 2
            end_y2 = screen_height / 2
            self.action.long_press(None, start_x2, start_y2).move_to(
                None, end_x2, end_y2).release().perform()
            self.log.info("Successfully Swapped from  right to left")

        except (ElementNotVisibleException, ElementNotSelectableException,
                NoSuchElementException, TimeoutException):
            self.screen_shot("screenshot_scroll_element")
            self.log.info("unSuccessfully Swapped from right to left")

    def tap(self, x_co, y_co):
        """
    Perform a tap gesture at the specified coordinates.
    Args:
        x (int): The x-coordinate of the tap gesture.
        y (int): The y-coordinate of the tap gesture.
    Returns:
        None
        """
        try:
            action = TouchAction(self.driver)
            action.tap(x=x_co, y=y_co).perform()
            self.log.info("Tap gesture performed at coordinates: (%d, %d)", x_co, y_co)
        except WebDriverException as exc:
            self.log.error("Error occurred while performing tap gesture: %s", str(exc))

    def take_screenshot(self,text):
        """
    Take a screenshot of the current state of the driver and attach it to the allure report.
    Args:
        text (str): A description or label for the screenshot.
    Returns:
        None
    """
        allure.attach(
            self.driver.get_screenshot_as_png(),
            name="text",
            attachment_type= AttachmentType.PNG
        )
