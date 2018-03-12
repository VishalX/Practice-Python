# Third party Library
# Using Beautiful Soup : Remove Syntax errors from web pages
# crummy.com | Beautiful Soup
# Install from here | https://www.crummy.com/software/BeautifulSoup/ 
# OR #
# Download from 'Dr-Check'
# http://www.py4e.com/code3/bs4.zip
# Unzip in wroking directory

# Import urllib and BeautifulSoup modules
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Input URL
iurl = input("Enter URL: ")
# Input Count
try:
    count = int(input("Enter count: "))
except:
    print("Error : Invalid Count value, must be an integer")
    quit()
# Input Position
try:
    pos = int(input("Enter position: "))
except:
    print("Error : Invalid Position value, must be an integer")
    quit()
    
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# URL to open
url = None
position = pos - 1
# Init tag list
tags = list()
# Init new url
newurl = None

# Loop over count times
for itr in range(count):
    if url is None:
        url = iurl
    else:
        url = newurl
    # Check if it works
    try:
        urlhand = urllib.request.urlopen(url, context=ctx)
    except:
        print("Error : Unable to open URL :", url)
        quit()

    # Read all the data
    htmldata = urlhand.read()

    # Filter errors using beautifulsoup
    bsoup = BeautifulSoup(htmldata, 'html.parser')
    # Loop over the list of anchor tags
    tags = bsoup('a')
    newurl = tags[position].get('href', None)
    print(newurl)