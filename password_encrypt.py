"""
This will use the website as a salt to generate a hashed password for the site when combined
with a provided password
"""

import hashlib

def hashPassword(password, website):
    website = website.hex()
    return hashlib.sha256(website.encode() + password.encode()).hexdigest() + ':' + website

def checkPassword(hashedPassword, userPassword):
    password, websiteHex = hashedPassword.split(':')
    print(f'hashed password: {password}')
    print(f'website hex: {websiteHex}')
    return password == hashlib.sha256(websiteHex.encode() + userPassword.encode()).hexdigest()


password = input('Please enter a password: ')
website = input('Enter the website: ').encode('utf-8')
hashedPassword = hashPassword(password, website)
print(f'Output from hashPassword: {hashedPassword}')

testPass = input('Enter the same password: ')
if checkPassword(hashedPassword, testPass):
    print('Passwords match')
else:
    print('Passwords don\'t match')
