import facial_recog
from GrabUrl import grabUrl
from GenerateKey import generateKey
from url_regex import urlRegex
import config
from config import getSiteLength
import pyperclip
import cv2  # import for the error catch
import uuid

# -------------------------------------------------------------------------------------------------------------------- #
def run(pin):
    print("Generating Password...\n")

    # This if block should return true in current machine mac address is whitelisted in the config file
    if config.updateConfigFile('MacAddresses', str(hex(uuid.getnode())).encode()):  # Program will only continue to generate a password if mac address is in config
        url = grabUrl()
        parsedURL = urlRegex(url)
        passwordSize = getSiteLength(parsedURL)

        try:
            face = facial_recog.facialRecognition()
        except cv2.error:
            print("ERROR: Camera is not accessible")

        key = generateKey(parsedURL, passwordSize, face, pin)
        # strip b'' from key so it can be read in as string
        keyAsString = str(key)[2:-1]
        pyperclip.copy(keyAsString)
        print("Your password for " + parsedURL + " is: " + keyAsString)
        return "Your unique password for:\n" + parsedURL + "\nhas been copied to clipboard."

# -------------------------------------------------------------------------------------------------------------------- #
