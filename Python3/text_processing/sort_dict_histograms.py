# -------------------------------------------------------------
# Function sortedDictByValue()
# -------------------------------------------------------------
# Sort Dictionary by value
# -------------------------------------------------------------
# @param dictname   : Dictionary Name <class "dict()">
# @param HighToLow  : True / False <class "Bool"> | Optional
# @param return     : Sorted dictionary
# -------------------------------------------------------------
def sortedDictByValue(dictname, HighToLow=False):
    # Initialize a dict
    sortedDict = dict()
    # sorted() method only return list of sorted 'keys' OR 'values'
    # Check o/p of sorted() by returning it
    """
    return 
    sorted(dictname)
    # OR
    sorted(dictname, reverse=True)
    # OR
    sorted(dictname.values())
    # OR
    sorted(dictname.values(), reverse=True)
    """
    # Note: Use list & tuples to generate (val, key) pair
    # and generate sorted dictionary

    # Initialize a list of tuples
    tuplist = list()
    # Dictionary's items() method returns tuples
    for (key, val) in dictname.items() :
        # Append tuple to the list
        tuplist.append((val, key))

    # Note: Now use sorted method to sort list of tuples

    # Sorted list of tuples by value
    stuplist = sorted(tuplist, reverse=HighToLow)

    # Generate sorted dictionary
    for val, key in stuplist :
        sortedDict[key] = sortedDict.get(key, val)

    # Return sorted dictionary
    return sortedDict
    # End of function