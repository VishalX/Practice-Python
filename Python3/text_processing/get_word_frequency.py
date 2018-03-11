# Return frequency of words in a sentence
# Doesn't take care of punctuations and other characters
# Use regular expressions for removing these characters
def wordFrequencyInSentence(sentence):
    if len(sentence) < 1:
        return None
    # Init Dictionary
    freq = dict()
    # Split sentence into words
    words = sentence.split()
    # Check all words
    for word in words:
        # Increment count
        freq[word] = freq.get(word, 0) + 1
    # Return
    return freq

# Return frequency of words in a file
# Doesn't take care of punctuations and other characters
# Use regular expressions for removing these characters
def wordFrequencyInFile(fname):
    # Check File existence / readable
    try:
        fhand = open(fname, 'r')
    except:
        return None

    # Init Dictionary
    freq = dict()
    # Read lines
    for line in fhand:
        # Split line in words
        words = line.split()
        # Create Dictionary with words
        for word in words:
            freq[word] = freq.get(word, 0) + 1
    # Return
    return freq