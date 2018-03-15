"""
Create a Tracks Database from an exported xml music library
"""
import xml.etree.ElementTree as ETree 
import sqlite3


def lookup(d, key):
    found = False
    for child in d:
        if found : return child.text
        if child.tag == 'key' and child.text == key :
            found = True
    return None

# XML Librayr file
xml_music_lib = "..\\..\\Data\\xml\\Library.xml"

# Database file name
tracks_db = "tracksdb.sqlite"

# Coonect to the database file
connection = sqlite3.connect(tracks_db)
# Create an execute cursor
curr = connection.cursor()

# Dump previous data from <tracks_db> database if exists
curr.executescript(
"""
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;
"""
)

# Create new tables
curr.executescript(
'''
CREATE TABLE Artist (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
);
CREATE TABLE Genre (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
);
CREATE TABLE Album (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id INTEGER,
    title TEXT UNIQUE
);
CREATE TABLE Track (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT UNIQUE,
    album_id INTEGER,
    genre_id INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);
'''
)

# Open XML file
try:
    fhand = open(xml_music_lib)
except:
    print("{:<25}".format("[ERROR] Opening file"),":", 
        "Can't open file", xml_music_lib)
    # Save Database
    print("{:<25}".format("[MESSG] Saving database"),  ":", tracks_db)
    connection.commit()
    print("{:<25}".format("[MESSG] Saved database"),  ":", tracks_db)
    # Close Cursor
    curr.close()
    print("{:<25}".format("[MESSG] Closing Cursor"), ": Done")
    quit()

print("{:<25}".format("[MESSG] Opened file"), ":", xml_music_lib)

# Read XML from file handle and pass it to XML parser
xmlTree = ETree.fromstring(fhand.read())

# Parse XML
allentries = xmlTree.findall("dict/dict/dict")
print("{:<25}".format("[DEBUG] All Entries"), ":", len(allentries))

# Go through all entries
for entry in allentries:

    # Look-up the XML entries
    name    = lookup(entry, 'Name')
    artist  = lookup(entry, 'Artist')
    album   = lookup(entry, 'Album')
    genre   = lookup(entry, 'Genre')
    count   = lookup(entry, 'Play Count')
    rating  = lookup(entry, 'Rating')
    length  = lookup(entry, 'Total Time')
    # print(type(count))

    # Continue if anyone of the below is not found
    if name is None or artist is None or album is None or genre is None:  continue

    # print(name, artist, album, count, rating, length)
    
    # Insert Artist name, if already not present, in Artist table
    curr.execute('''INSERT OR IGNORE INTO Artist (name) 
        VALUES ( ? )''', ( artist, ))
    # Select Artist-ID using artist name & fetch it
    curr.execute('SELECT id FROM Artist WHERE name = ? ', (artist, ))
    artist_id = curr.fetchone()[0]
    
    # Insert Genre name, if already not present, in Genre table
    curr.execute('''INSERT OR IGNORE INTO Genre (name)
        VALUES ( ? )''', (genre,))
    # Select Genre-ID using genre name & fetch it
    curr.execute('SELECT id FROM Genre WHERE name = ? ', (genre, ))
    genre_id = curr.fetchone()[0]

    # Insert Album name, if already not present, in Album table
    curr.execute('''INSERT OR IGNORE INTO Album (title, artist_id) 
        VALUES ( ?, ? )''', ( album, artist_id ))
    # Select Album-ID using album name & fetch it
    curr.execute('SELECT id FROM Album WHERE title = ? ', (album, ))
    album_id = curr.fetchone()[0]

    # Insert Track entries, if already not present, in Track table
    curr.execute('''INSERT OR REPLACE INTO Track
        (title, album_id, genre_id, len, rating, count) 
        VALUES ( ?, ?, ?, ?, ?, ? )''', 
        ( name, album_id, genre_id, length, rating, count ))
    
    # End of for loop #########################################################

# Save Database
print("{:<25}".format("[MESSG] Saving database"),  ":", tracks_db)
connection.commit()
print("{:<25}".format("[MESSG] Saved database"),  ":", tracks_db)

# Close Cursor
curr.close()
print("{:<25}".format("[MESSG] Closing Cursor"), ": Done")
# Close xml file
fhand.close()
print("{:<25}".format("[MESSG] Closed file"), ":", xml_music_lib)