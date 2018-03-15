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
cur.execute("DROP TABLE IF EXISTS Counts")

# Create New table
cur.execute("CREATE TABLE Counts ( org TEXT, count INTEGER )")

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
    # Get email
    email = words[1]
    # Split email (emailID @ domain)
    orgs  = email.split("@")
    # Get org
    domain = orgs[1]
    print("{:<25}".format("[DEBUG] domain"), ":", domain) 
    # Select Count, with specified email, from the table 
    cur.execute("SELECT count FROM Counts WHERE org = ?", (domain,))
    # Fetch one row
    row = cur.fetchone()
    if row is None:
        # Insert an entry if email doesn't exist
        cur.execute("INSERT INTO Counts (org, count) VALUES (?, 1)", (domain,))
    else:
        # Update the Count if email exists
        cur.execute("UPDATE Counts SET count = count + 1 WHERE org = ?", (domain,))

# Order by Counts
cur.execute("SELECT org, count FROM Counts ORDER BY count DESC")
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