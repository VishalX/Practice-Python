# --------------------------------------------------------------------------
# Function vovelHistogram
# --------------------------------------------------------------------------
# Read a file and get the character frequency 
# Histogram of characters
# --------------------------------------------------------------------------
# @param fname         : File path/name
# @param caseSensitive : True / False <Converts to UPPER case> 
#                        Default=True 
# @param return        : dictionary of vovel frequency, 
#                        else None if file not found
# --------------------------------------------------------------------------
def vovelHistogram(fname, caseSensitive=True) :
    # Read file : Read Only mode
    try :
        fhand = open(fname, 'r')
    except :
        # Quit
        return None
    VOVELS = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    # Initialize a char dictionary
    chardict = dict()
    # Initalize a list for storing words
    wordlist = list()
    # Read file & Loop over lines
    for line in fhand :
        # Strip whitespaces
        if caseSensitive is False :
            no_ws_line = line.upper().strip()
        else :
            no_ws_line = line.strip()
        # Split into words
        wordlist = no_ws_line.split()
        # For each word, get characters, create dictionary
        for word in wordlist :
            for ch in word :
                # Check if character is alnum or not
                if ch in VOVELS:
                    """
                    # Use if-else to check 'key' existence
                    if chr not in chardict :
                        chardict[ch] = 1
                    else :
                        chardict[ch] = chardict[ch] + 1
                    """
                    # OR use default value of key using get() method as 0 if not present
                    chardict[ch] = chardict.get(ch, 0) + 1
                else:
                    # Don't add to dictionary
                    continue
    # Return dictionary
    return chardict
    # End of Function