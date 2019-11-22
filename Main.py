import facial_recog
from GrabUrl import grabUrl
from GenerateKey import generateKey
from url_regex import urlRegex
from config import getSiteLength
import pyperclip
import cv2  # import for the error catch


# -------------------------------------------------------------------------------------------------------------------- #
def run(pin):
    print("Generating Password...\n")
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
    print("Your password for " + url + " is: " + keyAsString)
    return "Your unique password for: \n" + url + "\nhas been copied to clipboard."

# -------------------------------------------------------------------------------------------------------------------- #
