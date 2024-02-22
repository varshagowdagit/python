from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

desired_caps = {'platformName': 'Android', 'automationName': 'UiAutomator2', 'platformVersion': '10',
                'deviceName': 'chef_sprout', 'app': (r"C:\Users\vs34\Downloads\Android_Demo_App.apk"),
                'appPackage': 'com.code2lead.kwad', 'appActivity': 'com.code2lead.kwad.MainActivity'}

driver = webdriver.Remote("http://127.0.0.1:4724/wd/hub",desired_caps)

print("is device locked",driver.is_locked())
print("Current Package",driver.current_package)
print("Current Activity",driver.current_activity)
print("Orientation",driver.orientation)
print("Context",driver.context)
