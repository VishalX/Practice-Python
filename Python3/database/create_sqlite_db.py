"""
Create SQLite Data Base using Python
Use: sqlite3 module
"""

# Import SQLite 
import sqlite3

dbname = "mbox.sqlite"
# Open or create a sqlite database
conn = sqlite3.connect(dbname)

# Create a cursor to execute SQLite commands
cur  = conn.cursor()

# Drop table if the database already have any
cur.execute("DROP TABLE IF EXISTS EmailCounts")

# Create New table
cur.execute("CREATE TABLE EmailCounts ( Email TEXT, Count INTEGER )")

# Open email data text file
fname = input("{:<25}".format("[INPUT] Enter file name   :"))
if len(fname) < 1:
    fname = "..\\..\\mbox.txt"

# Open file
try:
    fhand = open(fname)
except:
    print("{:<25}".format("[ERROR] Can't open file"), ":", fname)
    quit()

print("{:<25}".format("[MESSG] File opened"),  ":", fname)

# Read File line by line
for line in fhand:
    # Skip the line if it doesn't start with "From: "
    if not line.startswith("From: "): continue
    # Split into words
    words = line.split()
    email = words[1]
    print("{:<25}".format("[DEBUG] email"), ":", email) 
    # Select Count, with specified email, from the table 
    cur.execute("SELECT Count FROM EmailCounts WHERE Email = ?", (email,))
    # Fetch one row
    row = cur.fetchone()
    if row is None:
        # Insert an entry if email doesn't exist
        cur.execute("INSERT INTO EmailCounts (Email, Count) VALUES (?, 1)", (email,))
    else:
        # Update the Count if email exists
        cur.execute("UPDATE EmailCounts SET Count = Count + 1 WHERE Email = ?", (email,))

# Save the database
print("{:<25}".format("[MESSG] Saving database"),  ":", dbname)
conn.commit()
print("{:<25}".format("[MESSG] Saved database"),  ":", dbname)
# Close Cursor
cur.close()
print("{:<25}".format("[MESSG] Closing Cursor"), ": Done")
# Close file
fhand.close()
print("{:<25}".format("[MESSG] Closed file"), ":", fname)