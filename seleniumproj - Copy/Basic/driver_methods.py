import time

from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
assert "Swag Labs" in driver.title
driver.maximize_window()
time.sleep(5)
driver.minimize_window()
time.sleep(5)
driver.maximize_window()

driver.quit()
