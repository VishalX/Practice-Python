######################################################
# Simple Ciphers
######################################################

# ----------------------------------------------------
# Ceasar Cipher
# ----------------------------------------------------
# Plaintext Cipher, Works with a numeric key which 
# works like a shift for the characters in the input 
# phrase.
# Key must be in range(26)
# ----------------------------------------------------
def encCeasar(phrase, key):
    # Check length of phrase
    if phrase is None or len(phrase) < 1:
        # Return None if no input 
        return None
    if key is None or key not in range(26):
        # Return None if key is invalid
        print("\nError : Invalid Key!")
        return None
    # Encrypt the phrase
    # Strip whitespaces from start and end
    tstr = phrase.strip()
    # Convert to upper case and remove spaces
    tstr = tstr.upper() # .replace(' ', '')
    encText = ''
    # Encrypt each character with key
    for ch in tstr:
        if ch.isalpha():
            ich = (ord(ch) - 65 + key) % 26
            nch = chr(ich + 65)
            encText += nch
        else:
            encText += ch
            continue
    # Return Encoded phrase
    return encText

def decCeasar(phrase, key):
        # Check length of phrase
    if phrase is None or len(phrase) < 1:
        # Return None if no input 
        return None
    if key is None or key not in range(26):
        # Return None if key is invalid
        print("\nError : Invalid Key!")
        return None
    # Decrypt the phrase
    # Strip whitespaces from start and end
    tstr = phrase.strip()
    # Convert to upper case and remove spaces
    tstr = tstr.upper() # .replace(' ', '')
    decText = ''
    # Encrypt each character with key
    for ch in tstr:
        if ch.isalpha():
            ich = (ord(ch) - 65 - key) % 26
            nch = chr(ich + 65)
            decText += nch
        else:
            decText += ch
            continue
    # Return Decrypted phrase
    return decText
