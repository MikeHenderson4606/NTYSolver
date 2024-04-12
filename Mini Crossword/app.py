from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import requests
import time
from datetime import date

# Import the client
import sys
sys.path.insert(1, '../Client')
import client

# Driver path // Switch for mac/windows
#driver_path = "../chromedriver-mac-x64/chromedriver"
driver_path = "../chromedriver-win64/chromedriver.exe"

# Enable performance logging
caps = DesiredCapabilities.CHROME
caps['goog:loggingPrefs'] = {'performance': 'ALL'}

# Set up Service
service = Service(executable_path=driver_path)

# Options
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

# Create chrome instance
driver = webdriver.Chrome(service=service, options=options)

driver.get('https://www.nytimes.com/crosswords/game/mini')

# Format today's date to get the json file
today = str(date.today())
url = 'https://www.nytimes.com/svc/crosswords/v6/puzzle/mini.json'
answer = client.getMiniCrosswordData(url)

# Wait until the x can be clicked for the 
xButton = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[class="xwd__modal--subtle-button"]'))
)
xButton.click()
print("X Button clicked")

# Let everything load
time.sleep(1)

for word in answer:
    ActionChains(driver).send_keys(word).perform()
    ActionChains(driver).send_keys(Keys.TAB).perform()

# Let it sink in
time.sleep(10)