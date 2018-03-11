# Import Regular Expression module
import re

fname = "regex_sum_82164.txt"
# Open file
try:
    fhand = open(fname)
except:
    print("Error : Can't open file")

# Read file and compute sum
fdata = fhand.read()
sumtotal = 0
# Find all numbers: Start with a digit and 
# find 1 or more digits
numlist = re.findall('[0-9]+', fdata)
# For whole list : sum the numbers
for num in numlist:
    sumtotal += int(num)
# Print
print(sumtotal)


