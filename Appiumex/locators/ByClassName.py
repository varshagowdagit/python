import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import time
desired_caps = {'platformName': 'Android', 'automationName': 'UiAutomator2', 'platformVersion': '10',
                'deviceName': 'chef_sprout', 'app': (r"C:\Users\vs34\Downloads\Android_Demo_App.apk"),
                'appPackage': 'com.code2lead.kwad', 'appActivity': 'com.code2lead.kwad.MainActivity'}

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
ele_id = driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/EnterValue")
ele_id.click()

time.sleep(5)
ele_cn = driver.find_element(AppiumBy.CLASS_NAME,"android.widget.EditText")
ele_cn.send_keys("sdfd")
