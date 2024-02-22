# import time
# from selenium import webdriver
# from selenium.common import NoSuchElementException
# from selenium.webdriver.chrome import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as ec
# driver = webdriver.Chrome()
# driver.get("https://www.saucedemo.com/")
# wait=WebDriverWait(driver,25,poll_frequency=1,ignored_exceptions=NoSuchElementException)
# ele=wait.until(ec.presence_of_element_located(By.ID,"user-name"))
# ele.send_keys("Standard-user")
# time.sleep(5)
# driver.quit()


