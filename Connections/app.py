from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import time

# Driver path
driver_path = "./chromedriver-win64/chromedriver.exe"

# Set up Service
service = Service(executable_path=driver_path)

# Options
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

# Create chrome instance
driver = webdriver.Chrome(service=service, options=options)

driver.get('https://www.nytimes.com/games/connections')


# Wait until the page has loaded to click play
try:
    playButton = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-testid="moment-btn-play"]'))
    )
    playButton.click()

    # Now wait until the x can be clicked for the 

    print("Play button clicked")
except:
    print("You can't do that")


# Sleep to see what's going on
time.sleep(5)

# Quit the driver
driver.quit()