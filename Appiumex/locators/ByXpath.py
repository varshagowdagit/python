import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

desired_caps = {'platformName': 'Android', 'automationName': 'UiAutomator2', 'platformVersion': '10',
                'deviceName': 'chef_sprout', 'app': (r"C:\Users\vs34\Downloads\Android_Demo_App.apk"),
                'appPackage': 'com.code2lead.kwad', 'appActivity': 'com.code2lead.kwad.MainActivity'}

driver = webdriver.Remote("http://127.0.0.1:4724/wd/hub",desired_caps)

#ele_txt = driver.find_element(AppiumBy.XPATH,'//android.widget.Button[@content-desc="Btn1"]') using xpath and con-desc
#ele_txt = driver.find_element(AppiumBy.XPATH,'//android.widget.Button[@resource-id="com.code2lead.kwad:id/EnterValue"]')
#ele_txt = driver.find_element(AppiumBy.XPATH,'//android.widget.Button[@text="ENTER SOME VALUE"]')
ele_txt = driver.find_element(AppiumBy.XPATH,'//android.widget.Button[1]')
#ele_txt = driver.find_element(AppiumBy.XPATH,'//android.widget.Button') using class name
ele_txt.click()
time.sleep(3)

ele_xpath = driver.find_element(AppiumBy.XPATH,'//android.widget.EditText')
ele_xpath.send_keys('skill')
time.sleep(4)

driver.quit()
