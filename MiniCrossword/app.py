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
sys.path.append('../Client')
import Client.client as client # type: ignore

def MiniCrossWord(driver):
    driver.get('https://www.nytimes.com/crosswords/game/mini')

    # Get the url for the json file
    url = 'https://www.nytimes.com/svc/crosswords/v6/puzzle/mini.json'
    answer = client.getMiniCrosswordData(url)

    # Wait until the x can be clicked for the 
    xButton = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[class="xwd__modal--subtle-button"]'))
    )
    xButton.click()
    print("X Button clicked")

    # Scroll into view
    scrollElement = driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Puzzle Settings Menu"]')
    driver.execute_script("arguments[0].scrollIntoView(true);", scrollElement)

    # Let everything load
    time.sleep(1)

    for word in answer:
        ActionChains(driver).send_keys(word).perform()
        ActionChains(driver).send_keys(Keys.TAB).perform()

    # Let it sink in
    time.sleep(5)