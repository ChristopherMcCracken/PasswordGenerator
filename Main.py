import facial_recog
from GrabUrl import grabUrl
from generate_password import generatePassword
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

    password = generatePassword(parsedURL, passwordSize, face, pin)
    # strip b'' from password so it can be read in as string
    passwordAsString = str(password)[2:-1]
    pyperclip.copy(passwordAsString)
    print("Your password for " + parsedURL + " is: " + passwordAsString)
    return "Your unique password for:\n" + parsedURL + "\nhas been copied to clipboard."
# -------------------------------------------------------------------------------------------------------------------- #
