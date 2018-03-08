# Open and Read a file line by line and print all the contents in UPPER case
def filePrintUpperCase(fname):
    # Define a file handle
    fh = None
    # Print file name
    print('File :', fname)
    # Open file
    try:
        fh = open(fname, 'r')
    except:
        print('\nError : No such file or directory')
        quit()

    # Read and Print Contents line by line
    for line in fh:
        # Strip new-line from each line
        nonewline = line.rstrip()
        # Change all characters to upper-case
        nonewline = nonewline.upper()
        # Print line without new line : print automatically appends new-line
        print(nonewline)

# Open and Read a file line by line and print all the contents in LOWER case
def filePrintLowerCase(fname):
    # Define a file handle
    fh = None
    # Print file name
    print('File :', fname)
    # Open file
    try:
        fh = open(fname, 'r')
    except:
        print('\nError : No such file or directory')
        quit()

    # Read and Print Contents line by line
    for line in fh:
        # Strip new-line from each line
        nonewline = line.rstrip()
        # Change all characters to upper-case
        nonewline = nonewline.lower()
        # Print line without new line : print automatically appends new-line
        print(nonewline)

# Count lines in a file
# @param    : File name
# @return   : Total number of lines in the file
def lineCount(fname):
    # Define a file handle
    fh = None
    # Print file name
    print('File :', fname)
    # Open file
    try:
        fh = open(fname, 'r')
    except:
        print('\nError : No such file or directory')
        quit()

    lncount = 0 
    # Read and Print Contents line by line
    for line in fh:
        # Increment count
        lncount = lncount + 1
    return lncount

# Count words in a file : Separated by whitespaces
# @param    : File name
# @return   : Total number of words in the file
def wordCount(fname):
    # Define a file handle
    fh = None
    # Print file name
    print('File :', fname)
    # Open file
    try:
        fh = open(fname, 'r')
    except:
        print('\nError : No such file or directory')
        quit()

    # Read whole data
    fdata = fh.read()
    # Split words separated by whitespaces
    words = fdata.split()
    # Use "len" to count
    # print('\nTotal Words :', len(words))

    wordcount = 0
    # Read and Print Contents line by line
    for word in words:
        # Increment count
        wordcount = wordcount + 1
    return wordcount

if __name__ == "__main__":
    fname = input('\n Enter File name : ')
    # filePrintLowerCase(fname)
    # filePrintUpperCase(fname)
    # lineCount(fname)
    count = wordCount(fname) 
    print('Total words :', count)