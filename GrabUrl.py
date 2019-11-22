import time
import keyboard as keyboard
import pyperclip
from selenium import webdriver


def grabUrl():
    # Grab URL
    # keyboard.press_and_release('alt+tab')  # alt+tab will open most recent window
    # time.sleep(.1)
    # keyboard.press_and_release('alt+d')
    # time.sleep(.1)
    # keyboard.press_and_release('ctrl+c')
    # time.sleep(.1)
    # keyboard.press_and_release('alt+tab')
    # time.sleep(.1)

    #selenium to grab current URL from Chrome browser
    # put chromewebdriver.exe inside of python scripts folder to run this, however this solution
    #driver = webdriver.Chrome()     #leave blank to have it search within PATH to find chromedriver
    #url = driver.getCurrentUrl()

    #firefox implementation
    #firefox_driver = webdriver.Firefox()
    #firefox_url = driver.getCurrentUrl()

    # Store URL
    url = pyperclip.paste()
    print("Your current url is: " + url + "\n")
    return url
