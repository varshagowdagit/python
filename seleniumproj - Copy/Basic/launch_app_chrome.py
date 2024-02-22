from selenium import webdriver
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
driver.find_element(By.ID,"user-name").send_keys("standard_user")
driver.find_element(By.ID,"password").send_keys("secret_sauce")
driver.find_element(By.ID,"login-button").click()
# ele = driver.find_elements(By.ID,"user-name")
# for i in ele:
#     print(i.text)


social_element = driver.find_element(By.CLASS_NAME, "social")
actions = ActionChains(driver)
actions.move_to_element(social_element).perform()
time.sleep(5)
driver.quit()


