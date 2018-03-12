import urllib.request, urllib.parse, urllib.error

def printWordCounts(wcdict, longestWordLength=20):
    spaces = longestWordLength + 1
    for (key, val) in wcdict.items():
        print("{:<{wspaces}}".format(key, wspaces=spaces), val)


# URL to open
url = "http://data.pr4e.org/intro-short.txt"
# Open url
# It works like a file handle
try:
    urlhand = urllib.request.urlopen(url)
except:
    print("Error : Unable to open URL :", url)
    quit()

# for loop can be used to retrieve the data from the url
# Create a word count dictionary
wordcount = dict()
longestwordlen = 0

for line in urlhand:
    decodedline = line.decode().strip() # Ignore .strip if not required
    words = decodedline.split()
    for word in words:
        wordcount[word] = wordcount.get(word, 0) + 1
        if longestwordlen < len(word):
            longestwordlen = len(word) ; print(word)

print(longestwordlen)
printWordCounts(wordcount, longestwordlen)
