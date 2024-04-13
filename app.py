import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

sys.path.append('./Wordle')
import Wordle.app as wordle

sys.path.append('./Mini Crossword')
import MiniCrossword.app as mini

sys.path.append('./Connections')
import Connections.app as connections



def setupDriver():
    # Driver path // Switch for mac/windows
    #driver_path = "../chromedriver-mac-x64/chromedriver"
    driver_path = "./chromedriver-win64/chromedriver.exe"

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

    return driver

if __name__ == "__main__":
    game = input("Enter the game you'd like to see played: ")
    driver = setupDriver()
    match game:
        case "connections":
            connections.Connections(driver)
        case "wordle":
            wordle.Wordle(driver)
        case "mini":
            mini.MiniCrossWord(driver)
        case "all":
            connections.Connections(driver)
            wordle.Wordle(driver)
            mini.MiniCrossWord(driver)

    driver.quit()