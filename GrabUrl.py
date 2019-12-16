import time
import keyboard
import pyperclip

def grabUrl():
    # Grab URL using automation
    keyboard.press_and_release('alt+tab')  # alt+tab will open most recent window
    time.sleep(.1)
    keyboard.press_and_release('alt+d')
    time.sleep(.1)
    keyboard.press_and_release('ctrl+c')
    time.sleep(.1)
    keyboard.press_and_release('alt+tab')
    time.sleep(.1)

    # Store URL
    url = pyperclip.paste()
    print("Your current url is: " + url + "\n")
    return url
