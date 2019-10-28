from GrabUrl import grabUrl
from GenerateKey import generateKey
import pyperclip


print("Generating Password...\n")
url = grabUrl()
key = generateKey(url)  # later on we will pass in more than just url into generateKey

# strip b'' from key so it can be read in as string
keyAsString = str(key)[2:-1]

print("Your password for " + url + " is: " + keyAsString + "\n")
pyperclip.copy(keyAsString)
