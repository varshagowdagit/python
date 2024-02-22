from appium import webdriver
from time import sleep

# Desired capabilities for the Appium session
desired_caps = {
    'platformName': 'Android',
    'platformVersion': '10',
    'automationName': 'UiAutomator2',
    'deviceName': 'emulator-5554',
    'appPackage': 'com.android.calculator2',
    'appActivity': 'com.android.calculator2.Calculator'
}

# Appium server connection URL
server_url = 'http://localhost:4723/wd/hub'

# Create an Appium WebDriver instance
driver = webdriver.Remote(server_url, desired_caps)

sleep(3)

# Perform addition operation
driver.find_element_by_id('digit_2').click()
driver.find_element_by_id('op_add').click()
driver.find_element_by_id('digit_4').click()
driver.find_element_by_id('eq').click()

# Retrieve the result
result = driver.find_element_by_id('result').text
print('Result: ' + result)

# Close the app and quit the driver
driver.close_app()
driver.quit()
