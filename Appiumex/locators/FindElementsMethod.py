import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

desired_caps = {'platformName': 'Android', 'automationName': 'UiAutomator2', 'platformVersion': '10',
                'deviceName': 'chef_sprout', 'app': (r"C:\Users\vs34\Downloads\Android_Demo_App.apk"),
                'appPackage': 'com.code2lead.kwad', 'appActivity': 'com.code2lead.kwad.MainActivity'}

driver = webdriver.Remote("http://127.0.0.1:4724/wd/hub",desired_caps)

ele_txt = driver.find_elements(AppiumBy.CLASS_NAME,"android.widget.Button")
for x in ele_txt:
    print(x.text)

for x in ele_txt:
    button = x.text
    if button == "ScrollView":
        x.click()
        break

time.sleep(4)
driver.quit()


