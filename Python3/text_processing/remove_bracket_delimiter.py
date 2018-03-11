def removeBrackets(istring):
    # Return None when istring length is 0
    if len(istring) < 1:
        return None
    # Translation table
    transtable = str.maketrans('', '', ')(][><}{')
    nstr = istring.translate(transtable)
    return nstr