# Parsing JSON from web
import urllib.request, urllib.parse, urllib.error
import ssl
import json

# key = ""

# Google Geocoding JSON interface url
google_geocoidng_json = "https://maps.googleapis.com/maps/api/geocode/json?"
# dr_chuck_jeojson = "http://py4e-data.dr-chuck.net/geojson?"
# Ignore security certificates
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input("Enter Address : ")
    if len(address) < 1: break
    
    # Build complete URL with Address and KEY
    url = google_geocoidng_json + urllib.parse.urlencode({"address" : address}) #, {"key" : key})
    # url = dr_chuck_jeojson + urllib.parse.urlencode({"address" : address})#, {"key" : key})
    # URL data handle
    print("Retrieving : ", url)
    try:
        urldatahand = urllib.request.urlopen(url, context=ctx)
    except:
        print("Error : Unable to open URL :", url)
        quit()

    # Read Page
    pagedata = urldatahand.read().decode()
    print("Retrieved", len(pagedata), "Charaters")
    # Get headers to check remaining accesses
    # headers = dict(urldatahand.getheaders())
    # print("Remaining Accesses :", headers)#["x-rate-limit-remaining"])
    # Read JSON data
    try:
        jsondata = json.loads(pagedata)
    except:
        jsondata = None

    if not jsondata or "status" not in jsondata:
        print("---------------------------------------------------")
        print("------------ Failed to retrieve data --------------")
        print("---------------------------------------------------")
        continue
    elif jsondata["status"] == "ZERO_RESULTS":
        print("---------------------------------------------------")
        print("## No Location found named : ", address)
        print("---------------------------------------------------")
        continue
    elif jsondata["status"] != "OK":
        print("---------------------------------------------------")
        print("------------ Failed to retrieve data --------------")
        print("---------------------------------------------------")
        print("Status :", jsondata["status"])
        print("Error  :", jsondata["error_message"], "\n")
        continue

    # Print JSON with formatting
    # print(json.dumps(jsondata, indent=4))

    # Parse & Print data from JSON
    # placeid = jsondata["results"][0]["place_id"]
    # print("Place id", placeid)
    formatted_addr = jsondata["results"][0]["formatted_address"]
    loc_lattitude  = jsondata["results"][0]["geometry"]["location"]["lat"]
    loc_longitude  = jsondata["results"][0]["geometry"]["location"]["lng"]

    print("Formatted Address :", formatted_addr)
    print("Lattitude :", loc_lattitude)
    print("Longitude :", loc_longitude)
    # print(formatted_addr, loc_lattitude, loc_longitude)