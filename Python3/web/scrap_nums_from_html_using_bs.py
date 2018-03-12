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
url = "http://py4e-data.dr-chuck.net/comments_82166.html"
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

# Retrieve all <span> tags
tags = bsoup('span')
# Loop over the list of span tags
# Sum all numbers
total = 0

for tag in tags:
    # Get Hyperlinks
    num = int(tag.contents[0]) # int(tag.text)
    total += num

print(total)



