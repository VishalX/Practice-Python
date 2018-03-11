# Find the longest word in a list of words

def longestWord(words):
    longest_word = None
    longest_len = 0
    # Check word by word
    for word in words:
        wlength = len(word)
        if longest_len < wlength:
            longest_len  = wlength
            longest_word = word
    # Return
    return longest_word
        