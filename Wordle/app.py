from selenium import webdriver
from selenium.webdriver.common.by import By
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

driver.get('https://www.nytimes.com/games/wordle')

# Format today's date to get the json file
today = str(date.today())
url = "https://www.nytimes.com/svc/wordle/v2/" + today + ".json"

# Get request to the url to get the json values for the current connections
word = client.getWordleData(url)

# Wait until the page has loaded to click play
playButton = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-testid="Play"]'))
)
playButton.click()
print("Play button clicked")

# Now wait until the x can be clicked for the 
xButton = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, 'svg[data-testid="icon-close"]'))
)
xButton.click()
print("X Button clicked")

# Wait for everything to render appropriately
time.sleep(1)

# Insert the solution to the puzzle
for char in word:
    selectorString = 'button[data-key="' + char + '"]'
    correctChar = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, selectorString))
    )
    correctChar.click()

# Click the submit button
submitButton = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[aria-label="enter"]'))
)
submitButton.click()

time.sleep(20)