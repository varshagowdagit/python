import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select  # Import the Select class
from selenium.webdriver import ActionChains
driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
wait = WebDriverWait(driver, 25, poll_frequency=1, ignored_exceptions=NoSuchElementException)

wait.until(ec.presence_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
wait.until(ec.presence_of_element_located((By.ID, "password"))).send_keys("secret_sauce")
wait.until(ec.presence_of_element_located((By.ID, "login-button"))).click()

# Correct the following line to first locate the element and then click it
ele = wait.until(ec.presence_of_element_located((By.CLASS_NAME, "product_sort_container")))
ele.click()

# Now, create a Select object
dd_option = Select(ele)

dd_v = dd_option.options
# To display the options in output screen
# for dd_val in dd_v:
#     print(dd_val.text)
#by value
dd_option.select_by_value("za")
time.sleep(5)
# #by text
# dd_option.select_by_visible_text("Price (low to high)")

social_element = driver.find_element(By.CLASS_NAME, "social")
actions = ActionChains(driver)
actions.move_to_element(social_element).perform()
time.sleep(5)
driver.quit()


