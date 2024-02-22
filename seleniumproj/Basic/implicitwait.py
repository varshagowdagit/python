from selenium.webdriver.common.by import By
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
driver.implicitly_wait(10)
driver.find_element(By.ID,"user-name").send_keys("standard_user")
driver.find_element(By.ID,"password").send_keys("secret_sauce")
time.sleep(5)
driver.quit()
