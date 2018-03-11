def findHTTPLinks(istring, secure=False):
    # Return None when istring length is 0
    if len(istring) < 1:
        return None
    # Break line into words
    words = istring.split()
    # Init list
    httplinks = list()
    for word in words:
        if secure is True: 
            if word.startswith("https"):
                httplinks.append(word)
        elif word.startswith("http"):
            httplinks.append(word)
    # Return list
    return httplinks

def findUniqueHTTPLinks(istring, secure=False):
    # Return None when istring length is 0
    if len(istring) < 1:
        return None
    # Break line into words
    words = istring.split()
    # Init list
    httplinks = list()
    for word in words:
        if secure is True: 
            if word.startswith("https") and word not in httplinks:
                httplinks.append(word)
        elif word.startswith("http") and word not in httplinks:
            httplinks.append(word)
    # Return list
    return httplinks