# Parse XML data using urllib and xml modules

import urllib.request, urllib.parse, urllib.error
import ssl
import xml.etree.ElementTree as ETree 

# Get an url
# Sample url = "http://py4e-data.dr-chuck.net/comments_42.xml"
url = "http://py4e-data.dr-chuck.net/comments_82168.xml"

# Ignore security certificates
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# URL data handle
print("Retrieving : ", url)
try:
    urldatahand = urllib.request.urlopen(url, context=ctx)
except:
    print("Error : Unable to open URL :", url)
    quit()

# Read data
xml_data = urldatahand.read().decode()
print("Retrieved", len(xml_data), "characters")
# print(type(xml_data))
# print(xml_data)

# Now use xml.etree to parse XML
xml_data_tree = ETree.fromstring(xml_data)
list_of_names = xml_data_tree.findall('comments/comment/name')
list_of_count = xml_data_tree.findall('comments/comment/count')

print("Count : ", len(list_of_count))

total = 0
for item in list_of_count:
    total += int(item.text) 

print("Sum : ", total)