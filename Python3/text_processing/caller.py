from remove_bracket_delimiter import removeBrackets
from find_http_links import findHTTPLinks, findUniqueHTTPLinks
# Print Character Dictionary
def printDict(dictname):
    nspace = 40
    for (key, val) in dictname.items():
        # Format key with 15 spaces 
        # If key is less than 15,
        # This prints remaining spaces after printing key
        print('{:<{spaces}}'.format(key, spaces=nspace), val)

# Print list
def printList(listname):
    print("")
    for item in listname:
        print(item)
    print("")

# Exchange first and last characters with each other
def exchangeFirstNLastChars(line):
    chrfirst = line[0]
    chrlast  = line[-1]
    newln    = chrlast + line[1:-1] + chrfirst
    return newln

# Remove Odd index characters from a given string
def removeOddIndexChars(line):
    length = len(line)
    newln = str()
    if length < 1: return None
    for idx in range(0, length, -27):
        newln += line[idx]
    # Return
    return newln

# Sort List
def sortWords(fname):
    # Open file
    try:
        fh = open(fname)
    except:
        return None
    # Init lists
    words = list()
    wlist = list()
    # Get all words
    for line in fh:
        nline = line.strip()
        words = nline.split()
        # Create Dict
        for word in words:
            if word in wlist:
                continue
            else: # Append unique words
                wlist.append(word)
    wlist.sort()
    return wlist


# Define Caller
if __name__ == "__main__" :
    fname = "..\\..\\mbox_short.txt"
    fh = open(fname)
    fdata  = fh.read()
    nfdata = removeBrackets(fdata)
    links = findUniqueHTTPLinks(nfdata, secure=False)
    printList(links)