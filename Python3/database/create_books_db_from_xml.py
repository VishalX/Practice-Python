"""
Create SQLite database for books
"""
import sqlite3
import xml.etree.ElementTree as xmlET

def getTagText(xtag, key):
    for itag in xtag:
        if itag.tag == key:
            return itag.text

# XML file
xml_fname = "../../Data/xml/books.xml"
xml_data = open(xml_fname).read()
# parse xml
try:
    xml_etree = xmlET.fromstring(xml_data)
except:
    print("[ERROR] XML parsing failed :", xml_fname)
    quit()

# Find "book" tag instance 
books = xml_etree.findall("book")

# print(len(books))
# Create or open database
booksdb = sqlite3.connect("booksdb.sqlite")
# Get execute cursor
curr = booksdb.cursor()
# Drop tables if exist
curr.executescript(
    """
    DROP TABLE IF EXISTS Genre;
    DROP TABLE IF EXISTS Author;
    DROP TABLE IF EXISTS Book;
    """
)
# Create New tables : Schema
curr.executescript(
    """
    CREATE TABLE Genre (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name TEXT UNIQUE
    );
    CREATE TABLE Author (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name TEXT UNIQUE
    );
    CREATE TABLE Book (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        title TEXT,
        description TEXT,
        price REAL, pub_date TEXT,
        author_id INTEGER, genre_id INTEGER   
    );
    """
)

# Get all books
for book in books:
    if book is None: break
    # Get tags
    author  = getTagText(book, "author")
    title   = getTagText(book, "title")
    genre   = getTagText(book, "genre")
    price   = float(getTagText(book, "price"))
    pb_date = getTagText(book, "publish_date")
    descrip = getTagText(book, "description")

    # print(author, title, genre, price, pb_date, descrip)
    curr.execute("INSERT OR IGNORE INTO Genre (name) VALUES (?)", (genre,))
    curr.execute("SELECT id FROM Genre WHERE name = ?", (genre,))
    genre_id = curr.fetchone()[0]
    curr.execute("INSERT OR IGNORE INTO Author (name) VALUES (?)", (author,))
    curr.execute("SELECT id FROM Author WHERE name = ?", (author,))
    author_id = curr.fetchone()[0]
    curr.execute("""
        INSERT OR IGNORE INTO Book (title, description, price, pub_date, author_id, genre_id) VALUES (?, ?, ?, ?, ?, ?)""",
        (title, descrip, price, pb_date, author_id, genre_id)
    )
    # End of for ##########################################################################

curr.execute("SELECT Book.title, Author.name, Genre.name FROM Book, Author, Genre ON Book.author_id = Author.id and Book.genre_id = Genre.id")
all = curr.fetchall()
for one in all:
    print("{:<15}".format(one[2]), "{:<25}".format(one[1]), one[0])

# Save table/database
booksdb.commit()
# Close cursor
curr.close()