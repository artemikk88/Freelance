from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Set the path to your ChromeDriver executable
chrome_driver_path = r'C:\Torrents\chromedriver.exe'

# Initialize ChromeDriver
driver = webdriver.Chrome(service=Service(executable_path=chrome_driver_path))

# Open Instagram
driver.get('https://www.instagram.com/')

# Wait for the page to load
time.sleep(10)

# Enter your Instagram credentials and log in
username = driver.find_element(By.NAME ,'username')
password = driver.find_element(By.NAME ,'password')
username.send_keys('your username')
password.send_keys('your password')
password.send_keys(Keys.RETURN)
4
# Wait for the page to load
time.sleep(10)

# Open the DM inbox
driver.find_element(By.XPATH,'//a[contains(@href, "/direct/inbox/")]').click()

# Wait for the page to load
time.sleep(5)

# Open 200 DM threads
for i in range(10):
    try:
        # Click on the first DM thread
        driver.find_element(By.CSS_SELECTOR,'.Igw0E.IwRSH.eGOV_.vwCYk.i0EQd').click()
        # Wait for the DM thread to load
        time.sleep(10)
        # Go back to the DM inbox
        driver.find_element(By.CSS_SELECTOR, '[aria-label="Back"]').click()
        # Wait for the page to load
        time.sleep(10)
    except Exception as e:
        print(e)
# Close the browser

