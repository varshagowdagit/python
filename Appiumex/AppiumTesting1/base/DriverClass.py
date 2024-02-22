from appium import webdriver


class Driver:
    def getDriverMethod(self):
        desired_caps = {'platformName': 'Android', 'automationName': 'UiAutomator2', 'platformVersion': '10',
                'deviceName': 'laurel_sprout','appPackage': 'com.myntra.android','noReset':True, 'appActivity': 'com.myntra.android.activities.react.ReactActivity'}

        driver = webdriver.Remote("http://127.0.0.1:4725/wd/hub",desired_caps)

        return driver
