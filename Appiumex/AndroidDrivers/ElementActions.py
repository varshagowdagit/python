from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import time

desired_caps = {'platformName': 'Android', 'automationName': 'UiAutomator2', 'platformVersion': '10',
                'deviceName': 'chef_sprout', 'app': (r"C:\Users\vs34\Downloads\Android_Demo_App.apk"),
                'appPackage': 'com.code2lead.kwad', 'appActivity': 'com.code2lead.kwad.MainActivity'}

driver =webdriver.Remote("http://127.0.0.1:4724/wd/hub",desired_caps)

ele_id = driver.find_element(AppiumBy.ID,"com.code2lead.kwad:id/EnterValue")
print("Text on the Button ", ele_id.text)
print("Text on the Button ", ele_id.get_attribute("class"))
print("Content Des  of the Button ", ele_id.get_attribute("content-desc"))
ele_id.click()

time.sleep(2)

ele_classname = driver.find_element(AppiumBy.CLASS_NAME,"android.widget.EditText")
ele_classname.send_keys("Skill2Lead")
time.sleep(2)
ele_classname.clear()
time.sleep(2)
ele_classname.send_keys("Skill2Lead")

time.sleep(2)
driver.quit()
