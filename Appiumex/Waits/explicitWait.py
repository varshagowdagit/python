import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import ElementNotSelectableException, ElementNotVisibleException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait

desired_caps = {'platformName': 'Android', 'automationName': 'UiAutomator2', 'platformVersion': '10',
                'deviceName': 'chef_sprout', 'app': r"C:\Users\vs34\Downloads\Android_Demo_App.apk",
                'appPackage': 'com.code2lead.kwad', 'appActivity': 'com.code2lead.kwad.MainActivity'}

driver = webdriver.Remote("http://127.0.0.1:4724/wd/hub",desired_caps)

wait = WebDriverWait(driver,25,poll_frequency=2,ignored_exceptions=[ElementNotVisibleException,ElementNotSelectableException,NoSuchElementException])

ele = wait.until(lambda x:x.find_element(AppiumBy.ID,"com.code2lead.kwad:id/EnterValue"))
ele.click()

ele = wait.until(lambda x:x.find_element(AppiumBy.CLASS_NAME,"android.widget.EditText"))
ele.send_keys("oiuyf")

time.sleep(4)
driver.quit()

