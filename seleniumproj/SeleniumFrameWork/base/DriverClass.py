from selenium import webdriver
import SeleniumFrameWork.utilities.customLogger as cl
class WebDriverClass:
    log = cl.customLogger()
    def get_web_driver(self,browser_name):
        driver = None
        if browser_name== "chrome":
            driver = webdriver.Chrome()
            self.log.info("Chrome driver is initializing")
        elif browser_name== "firefox":
            driver= webdriver.Firefox()
            self.log.info("Firefox driver is initializing")
        return driver
