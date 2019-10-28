"""
url_regex.py - uses a regular expression to get the url that will be used to generate the password
Used over the copied URL to prevent inconsistencies of different URLs for the same site
"""

import re

def urlRegex(url):
    """
    uses a regex to get the website and domain name from a provided url
    """
    regex = re.compile(r'''
    (https{0,1}:\/\/){0,1} # group 1 - http(s)://
    (w{3}\.){0,1}          # group 2 - www.
    (.*)                   # group 3 - actual domain name (e.g. google)
    (\.[a-zA-Z]{2,10})     # group 4 - domain (e.g. .com)
    ''', re.VERBOSE)

    # run the regex over the provided url
    regexResults = regex.search(url)

    # try to get the website and domain from the provided url
    try:
        website = regexResults.group(3)
        domain = regexResults.group(4)
    # if there's an AttributeError, then url is not valid
    except AttributeError:
        print('Invalid url provided')
        print(f'Provided url: {url}')
        exit()

    # create the url with just the website and domain
    parsedURL = website + domain

    return parsedURL
