# open browser
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
time.sleep(5)
#  go to webpage
driver.get("https://practicetestautomation.com/practice-test-login/")

#Type username student into Username field
username_locator = driver.find_element()


#Type password Password123 into Password field


#Puch Submit button

#Verify new page URL contains practicetestautomation.com/logged-in-successfully/
#Verify new page contains expected text ('Congratulations' or 'successfully logged in')
#Verify button Log out is displayed on the new page

