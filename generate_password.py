import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

def generatePassword(url, passwordSize, faceEncoding, pin):
    """
    This method will generate a password for the provided website using the URL, face encoding,
    and provided pin
    """
    salt = str(url).encode() + str(pin).encode()
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=passwordSize,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )

    password = base64.urlsafe_b64encode(kdf.derive(faceEncoding))  # Can only use kdf once

    print(f'Your password is: {password}\n')
    return password
