from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

import time
import json

# Driver path // Switch for mac/windows
driver_path = "../chromedriver-mac-x64/chromedriver"

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

driver.get('https://www.nytimes.com/games/connections')

network_logs = driver.get_log('performance')
for entry in network_logs:
    entryJson = json.loads(entry['message'])
    if (entryJson['message']['method'] == "Network.requestWillBeSent"):
        print(entryJson)
    # if (entry['message']['message']['method'] == "Network.responseReceivedExtraInfo"):
    #     print(entry['message'])

# Wait until the page has loaded to click play
try:
    playButton = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-testid="moment-btn-play"]'))
    )
    playButton.click()
    print("Play button clicked")

    # Now wait until the x can be clicked for the 
    xButton = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'i[class="pz-icon pz-icon-close"]'))
    )
    xButton.click()
    print("X Button clicked")

    # Process network data
    
        # message = entry['message']
        # message_dict = json.loads(message)
        # if 'message' in message_dict['params']:
        #     message_params = message_dict['params']['message']
        #     print(message_params)
        #     if message_params['method'] == 'Network.requestWillBeSent':
        #         request_data = message_params['params']
        #         # Extract relevant information from request_data
        #     elif message_params['method'] == 'Network.responseReceived':
        #         response_data = message_params['params']
        #         # Extract relevant information from response_data
            
except:
    print("You can't do that")


# Sleep to see what's going on
time.sleep(500)

# Quit the driver
driver.quit()