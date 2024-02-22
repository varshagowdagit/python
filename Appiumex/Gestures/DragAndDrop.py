import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.common import ElementNotSelectableException, ElementNotVisibleException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait

desired_caps = {'platformName': 'Android', 'automationName': 'UiAutomator2', 'platformVersion': '10',
                'deviceName': 'chef_sprout', 'app': r"C:\Users\vs34\Downloads\Android_Demo_App.apk",
                'appPackage': 'com.code2lead.kwad', 'appActivity': 'com.code2lead.kwad.MainActivity'}

driver = webdriver.Remote("http://127.0.0.1:4724/wd/hub",desired_caps)

wait = WebDriverWait(driver,25,poll_frequency=2,ignored_exceptions=[ElementNotVisibleException,ElementNotSelectableException,NoSuchElementException])
ele = wait.until(lambda x:x.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiScrollable(new UiSelector()).scrollIntoView(text("DRAGANDDROP"))'))
ele.click()
ele_kw = wait.until(lambda x:x.find_element(AppiumBy.ID,"com.code2lead.kwad:id/ingvw"))


ele_lay = wait.until(lambda x:x.find_element(AppiumBy.ID,"com.code2lead.kwad:id/layout2"))

action = TouchAction(driver)
action.long_press(ele_kw).move_to(ele_lay).release().perform()
time.sleep(4)
driver.quit()
