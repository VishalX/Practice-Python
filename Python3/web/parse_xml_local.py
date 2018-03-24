"""
XML parsing using Python3
"""

# Import xml element tree module
import xml.etree.ElementTree as xmlET

# XML file
# xml_fname = "..\\..\\Data\\xml\\books.xml"
xml_fname = "../../Data/xml/books.xml"

# Open xml file
try:
    xml_fhand = open(xml_fname)
except:
    print("[ERROR] Can't open file :", xml_fname)
    quit()

print("[MESSG] Opened file :", xml_fname)
# Read file
xml_sdata = xml_fhand.read()

# print(len(xml_sdata))
# Create XML element tree
xml_etree = xmlET.fromstring(xml_sdata)

# Find all Tags
books = xml_etree.findall("book")
# print(len(books))

if books is None:
    print("[ERROR] Can't find any books !")
    xml_fhand.close()
    quit()

print("---------------------------------------------------------------------------------------------------------------")
print("{:<10}".format("Book-ID"), "{:<25}".format("Author"), "{:<40}".format("Title"), end="")
print("{:<15}".format("Genre"), "Price")
print("---------------------------------------------------------------------------------------------------------------")

for book in books:
    print("{:<10}".format(book.attrib["id"]), "{:<25}".format(book[0].text), "{:<40}".format(book[1].text), end="")
    print("{:<15}".format(book[2].text), book[3].text)

print("---------------------------------------------------------------------------------------------------------------")
# Close XML file  
xml_fhand.close()
print("[MESSG] Closed file :", xml_fname)
