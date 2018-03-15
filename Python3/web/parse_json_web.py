# Parsing JSON from web
import urllib.request, urllib.parse, urllib.error
import ssl
import json

# Get an url
# Sample url = "http://py4e-data.dr-chuck.net/comments_42.json"
url = "http://py4e-data.dr-chuck.net/comments_82169.json"
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
json_data = urldatahand.read().decode()
print("Retrieved",  len(json_data), "characters")
#print(json_data)
# Parse json data
json_data_dict = json.loads(json_data)
users = list(json_data_dict["comments"])

total = 0
# Print data
for user in users: 
    # print("{:<15}".format(user["name"]), user["count"])
    total += int(user['count'])
# Total Users
#print("---------------------")
print("Count :", len(users))
print("Sum :", total)
