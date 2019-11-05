import facial_recog
from GrabUrl import grabUrl
from GenerateKey import generateKey
from url_regex import urlRegex
import pyperclip
from argparse import ArgumentParser
import sys


# -------------------------------------------------------------------------------------------------------------------- #
def run():
    # parser is used for the password_size argument
    parser = ArgumentParser()
    parser.add_argument('--password_size', help='Set the length of the password. Defaults to 32.')

    arguments = parser.parse_args()

    MIN_PASSWORD_LENGTH = 7
    MAX_PASSWORD_LENGTH = 256
    DEFAULT_PASSWORD_LENGTH = 32

    # check if the password_size argument exists
    if arguments.password_size:
        # try to convert the argument to an int
        try:
            passwordSize = int(arguments.password_size)
        # except ValueError, which means the user entered more than just numbers
        except ValueError:
            print('Invalid password size')
            sys.exit(1)

        # check if the password length is too large or small
        if passwordSize < MIN_PASSWORD_LENGTH:
            print('Password length is too small')
            sys.exit(2)
        elif passwordSize > MAX_PASSWORD_LENGTH:
            print('Password length is too large')
            sys.exit(3)
    # if not set the password to the default password length
    else:
        passwordSize = DEFAULT_PASSWORD_LENGTH

    print("Generating Password...\n")
    url = grabUrl()
    parsedURL = urlRegex(url)
    face = facial_recog.facialRecognition()
    key = generateKey(parsedURL, passwordSize, face)  # later on we will pass in more than just url into generateKey

    # strip b'' from key so it can be read in as string
    keyAsString = str(key)[2:-1]

    print("Your password for " + url + " is: " + keyAsString + "\n")
    pyperclip.copy(keyAsString)
# -------------------------------------------------------------------------------------------------------------------- #
