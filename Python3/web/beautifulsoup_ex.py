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

# URL to open
url = "http://dr-chuck.com/page2.htm"
# Open url
# It works like a file handle
try:
    urlhand = urllib.request.urlopen(url)
except:
    print("Error : Unable to open URL :", url)
    quit()

# Read all the data
htmldata = urlhand.read()

# Filter errors using beautifulsoup
bsoup = BeautifulSoup(htmldata, 'html.parser')

# Retrieve all anchor tags : 'a' in html is an anchor tag
tags = bsoup('a')
# Loop over the list of anchor tags
for tag in tags:
    # Get Hyperlinks
    hyplink = tag.get('href', None)
    print(hyplink)



