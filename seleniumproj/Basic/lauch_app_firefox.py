# from selenium import webdriver
# driver = webdriver.Firefox()
# driver.get("https://www.saucedemo.com/")
# driver.quit()
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
wait = WebDriverWait(driver, 25, poll_frequency=1, ignored_exceptions=NoSuchElementException)

wait.until(ec.presence_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
wait.until(ec.presence_of_element_located((By.ID, "password"))).send_keys("secret_sauce")
wait.until(ec.presence_of_element_located((By.ID, "login-button"))).click()

# Locate the product element you want to scroll to
product_element = wait.until(ec.presence_of_element_located((By.CLASS_NAME, "social")))
time.sleep(5)
# Scroll to the product element
driver.execute_script("arguments[0].scrollIntoView();", product_element)

# Perform any actions you need with the scrolled-to product element
# For example, you can click on it
# product_element.click()

time.sleep(5)
driver.quit()
