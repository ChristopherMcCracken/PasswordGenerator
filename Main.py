import facial_recog
from GrabUrl import grabUrl
from GenerateKey import generateKey
from url_regex import urlRegex
from config import getSiteLength
import pyperclip
import cv2          # import for the error catch


# -------------------------------------------------------------------------------------------------------------------- #
def run():
    print("Generating Password...\n")
    url = grabUrl()
    parsedURL = urlRegex(url)
    passwordSize = getSiteLength(parsedURL)

    try:
        face = facial_recog.facialRecognition()
        return face
    except cv2.error:
        print("ERROR: Camera is not accessible")

    key = generateKey(parsedURL, passwordSize, face)  # later on we will pass in more than just url into generateKey
    # strip b'' from key so it can be read in as string
    keyAsString = str(key)[2:-1]

    print("Your password for " + url + " is: " + keyAsString + "\n")
    pyperclip.copy(keyAsString)
# -------------------------------------------------------------------------------------------------------------------- #
