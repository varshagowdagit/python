from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

desired_caps = {'platformName': 'Android', 'automationName': 'UiAutomator2', 'platformVersion': '10',
                'deviceName': 'chef_sprout', 'app': (r"C:\Users\vs34\Downloads\Android_Demo_App.apk"),
                'appPackage': 'com.code2lead.kwad', 'appActivity': 'com.code2lead.kwad.MainActivity'}

driver = webdriver.Remote("http://127.0.0.1:4724/wd/hub",desired_caps)

ele_txt = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("ENTER SOME VALUE")')
ele_txt.click()
#OR
# ele_txt = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'text("ENTER SOME VALUE")')
# ele_txt.click()
