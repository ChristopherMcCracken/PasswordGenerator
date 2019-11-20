import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


def generateKey(url, passwordSize, face, pin):
    password_provided = face   # This is input in the form of a string
    password = face
    # password = password_provided.encode()  # Convert to type bytes
    salt = str(url).encode() + str(pin).encode()  # might also want to make this unique per each password
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=passwordSize,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )

    key = base64.urlsafe_b64encode(kdf.derive(password))  # Can only use kdf once
    print(f'Your key is: {key}\n')
    return key


#  https://nitratine.net/blog/post/encryption-and-decryption-in-python/
