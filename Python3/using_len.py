# "len" function returns length of a string OR 
# Number of Characters present in string

# Define a string
exstr = "All iz wellllll" 

# Get the length of "exstr"
length_of_exstr = len(exstr)
# Print
print("Length :", length_of_exstr)

# Get a file and count number of characters
num_char = None
# Open a file
fh = open("..\\mbox_short.txt")
# Read file
fdata = fh.read()
# Get length
num_char = len(fdata)

print("Number of characters :", num_char)