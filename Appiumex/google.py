from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
#Reset strategy: default,noreset,full

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['automationName'] = 'UiAutomator2'
desired_caps['platformVersion'] = '11'
desired_caps['deviceName'] = 'Pixel4'
#desired_caps['app'] = (r"C:\Users\vs34\Downloads\Android_Demo_App.apk")

desired_caps['appPackage'] = 'com.android.chrome'
desired_caps['appActivity'] = 'com.google.android.apps.chrome.Main'
desired_caps['noReset'] = True
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)

