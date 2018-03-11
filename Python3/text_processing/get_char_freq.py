# --------------------------------------------------------------------------
# Function getCharFrequencyInTextFile
# --------------------------------------------------------------------------
# Read a file and get the character frequency 
# Histogram of characters
# --------------------------------------------------------------------------
# @param fname         : File path/name
# @param ignoreAlNum   : True / False | Optional
# @param caseSensitive : True / False <Converts to UPPER case> 
#                        Default=True 
# @param return        : dictionary of character frequency, 
#                        else None if file not found
# --------------------------------------------------------------------------
def getCharFrequencyInTextFile(fname, ignoreAlNum=True, caseSensitive=True) :
    # Read file : Read Only mode
    try :
        fhand = open(fname, 'r')
    except :
        # Quit
        return None
    
    # Initialize a char dictionary
    chardict = dict()
    # Initalize a list for storing words
    wordlist = list()
    # Read file & Loop over lines
    for line in fhand :
        # Strip whitespaces
        if caseSensitive is True :
            no_ws_line = line.strip()
        else :
            no_ws_line = line.upper().strip()
        # Split into words
        wordlist = no_ws_line.split()
        # For each word, get characters, create dictionary
        for word in wordlist :
            for chr in word :
                # Ignore non-alphanumeric charaters
                if ignoreAlNum is True:
                    # Check if character is alnum or not
                    if chr.isalnum():
                        """
                        # Use if-else to check 'key' existence
                        if chr not in chardict :
                            chardict[chr] = 1
                        else :
                            chardict[chr] = chardict[chr] + 1
                        """
                        # OR use default value of key using get() method as 0 if not present
                        chardict[chr] = chardict.get(chr, 0) + 1
                    else:
                        # Don't add to dictionary
                        continue
                else:
                     chardict[chr] = chardict.get(chr, 0) + 1
    # Return dictionary
    return chardict
    # End of Function