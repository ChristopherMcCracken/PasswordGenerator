"""
config.py - used to parse a config file that will hold the password lengths for different websites.
The file can be modified incase users want a longer or shorter password
"""

import configparser
from os import path

CONFIG_FILE_NAME = 'config.ini'
MIN_PASSWORD_LENGTH = 7
MAX_PASSWORD_LENGTH = 256
DEFAULT_PASSWORD_LENGTH = 32

def getSiteLength(site):
    """
    attempts to get the site length from the config file. If it is unable to, it will update or
    create the config file and store the length for the site.
    """
    if not path.isfile(CONFIG_FILE_NAME):
        createConfigFile()

    config = configparser.ConfigParser()
    config.read(CONFIG_FILE_NAME)

    if site in config['Sites']:
        try:
            siteLength = config.getint('Sites', site)
        except ValueError:
            print(f'Invalid length for {site}.\nSite length must be an integer value.')
            exit()

        if siteLength > MAX_PASSWORD_LENGTH:
            return MAX_PASSWORD_LENGTH
        elif siteLength < MIN_PASSWORD_LENGTH:
            return MIN_PASSWORD_LENGTH
        else:
            return siteLength
    else:
        updateConfigFile('Sites', site)
        return DEFAULT_PASSWORD_LENGTH


def updateConfigFile(type, data):
    """
    updates the config file with the site length
    """
    configUpdate = configparser.RawConfigParser()
    configUpdate.read(CONFIG_FILE_NAME)
    print(data)
    # This block is not entered when desired
    if data in configUpdate[type]:
        return True

    if type is 'Sites':
        configUpdate.set(type, data, DEFAULT_PASSWORD_LENGTH)

    elif type is 'MacAddresses':
        configUpdate.set(type, data)

    with open(CONFIG_FILE_NAME, 'w') as configfile:
        configUpdate.write(configfile)



def createConfigFile():
    """
    creates the config file if it doesn't exist
    """
    configCreation = configparser.RawConfigParser()

    configCreation.add_section('Sites')

    with open(CONFIG_FILE_NAME, 'w') as configfile:
        configCreation.write(configfile)
