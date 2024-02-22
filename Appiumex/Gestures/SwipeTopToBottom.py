import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.common import ElementNotSelectableException, ElementNotVisibleException, NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

desired_caps = {'platformName': 'Android', 'automationName': 'UiAutomator2', 'platformVersion': '10',
                'deviceName': 'chef_sprout', 'app': r"C:\Users\vs34\Downloads\Android_Demo_App.apk",
                'appPackage': 'com.code2lead.kwad', 'appActivity': 'com.code2lead.kwad.MainActivity'}

driver = webdriver.Remote("http://127.0.0.1:4727/wd/hub",desired_caps)

wait = WebDriverWait(driver,25,poll_frequency=2,ignored_exceptions=[ElementNotVisibleException,ElementNotSelectableException,NoSuchElementException])
ele = wait.until(lambda  x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'text("ScrollView")'))
ele.click()

print("Device Width and Height : ",driver.get_window_size())
deviceSize = driver.get_window_size()
screenWidth = deviceSize['width']
screenHeight = deviceSize['height']

###### Swipe from Bottom to Top  #######
startx = screenWidth/2
endx = screenWidth/2
starty = screenHeight*8/9
endy = screenHeight/9


###### Swipe from Top to Bottom #######
startx2 = screenWidth/2
endx2 = screenWidth/2
starty2 = screenHeight*2/9
endy2 = screenHeight*8/9

actions = TouchAction(driver)
actions.long_press(None,startx,starty).move_to(None,endx,endy).release().perform()
time.sleep(2)
actions.long_press(None,startx2,starty2).move_to(None,endx2,endy2).release().perform()
