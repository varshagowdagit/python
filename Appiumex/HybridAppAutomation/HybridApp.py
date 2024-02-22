import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.common import ElementNotSelectableException, ElementNotVisibleException, NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

desired_caps = {'platformName': 'Android', 'automationName': 'UiAutomator2', 'platformVersion': '10',
                'deviceName': 'chef_sprout', 'app': r"C:\Users\vs34\Downloads\google_chrome_115.0.5790.85_androidapksbox.apk",
                'appPackage': 'com.android.chrome', 'appActivity': 'com.google.android.apps.chrome.Main'}
# 1. Create the Driver object
driver = webdriver.Remote("http://127.0.0.1:4728/wd/hub", desired_caps)

# 2. Create WebDriverWait
wait = WebDriverWait(driver,25,poll_frequency=1,ignored_exceptions=[ElementNotVisibleException,ElementNotSelectableException,NoSuchElementException])

# 3. Open the URL in Browser
ele = wait.until(lambda x: x.find_element(AppiumBy.ID,"com.android.chrome:id/signin_fre_dismiss_button"))
ele.click()
time.sleep(4)

ele3 = wait.until(lambda x: x.find_element(AppiumBy.ID,"com.android.chrome:id/search_box_text"))
ele3.click()

ele4 = wait.until(lambda x: x.find_element(AppiumBy.ID,"com.android.chrome:id/url_bar"))
ele4.click()
ele4.send_keys("https://www.google.com/")

driver.press_keycode(66)
time.sleep(4)

# 4. Get the list of Contexts in App
appContexts = driver.contexts
print("AppContexts : ", appContexts)



# 5. switch to webview to perform action on Required URL or on WebView
for appType in appContexts:
    if appType == "WEBVIEW_chrome":
        driver.switch_to.context(appType)

ele_4 = wait.until(lambda x: x.find_element(AppiumBy.ID,"com.android.chrome:id/url_bar"))
ele_4.click()

# 6. Do testing on Webview screen in chrome browser or any if we want
# ele4 = wait.until(lambda  x: x.find_element(AppiumBy.ID,'APjFqb'))
ele4.send_keys("Skill2Lead")

# 7. Switch back to native view to perform action
for appType in appContexts:
    if appType == "NATIVE_APP":
        driver.switch_to.context(appType)

# 8. Do testing on native app screen if we want

ele4 = wait.until(lambda  x: x.find_element(AppiumBy.ID,"com.android.chrome:id/url_bar"))
ele4.click()
ele4.send_keys("https://www.skill2lead.com/")
driver.press_keycode(66)

# 9. Quit or close the driver object

time.sleep(5)
driver.quit()
