""" 
Create a SQLite database using the data available in json stored locally.
json file contains the users, courses and the roles of the users.
"""

# Import required modules
import json         # to parse json
import sqlite3      # to create sqlite db
import sys          # to get coomand line arguments

# Get command line arguments
def print_cmd_line_args():
    print(sys.argv)

# print_cmd_line_args()

# Get File name
json_fname = sys.argv[1]

# Open & read json data as string
try:
    with open(json_fname, "r") as json_fhand:
        json_str = json_fhand.read()
except:
    print("[ERROR]", json_fname, ": No such file or directory.")
    
# print("[DEBUG] JSON Data string :\n---------------------------")
# print(json_str)

# Parse json data
json_data_list = json.loads(json_str)

print(len(json_data_list))

# Create/open database
roster_db = sqlite3.connect("roster.sqlite")

# Get command cursor
curr = roster_db.cursor()

# Drop/Wipe-out existing tables, if exist  
curr.executescript(
    """
    DROP TABLE IF EXISTS Users;
    DROP TABLE IF EXISTS Course;
    DROP TABLE IF EXISTS Member;
    """
)

# Create new tables
curr.executescript(
    """
    CREATE TABLE Users (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name TEXT UNIQUE
    );
    CREATE TABLE Course (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        title TEXT UNIQUE
    );
    CREATE TABLE Member (
        user_id INTEGER,
        course_id INTEGER,
        role INTEGER,
        PRIMARY KEY (user_id, course_id)
    )
    """
)

# Fill database with data
for item in json_data_list:
    user_name    = item[0]
    course_title = item[1]
    user_role    = int(item[2])

    # print("[DEBUG]", "{:<15}{:<10}{:}".format(user_name, course_title, user_role))
    
    # Insert user
    curr.execute("insert or ignore into Users (name) values (?)", (user_name,))
    # Get user ID
    curr.execute("select id from Users where name = ?", (user_name,))
    user_id = curr.fetchone()[0]
    
    # Insert course
    curr.execute("insert or ignore into Course (title) values (?)", (course_title,))
    # Get course ID
    curr.execute("select id from Course where title = ?", (course_title,))
    course_id = curr.fetchone()[0]
    
    # Insert role, user_id & course_id in Member table
    curr.execute("insert or replace into Member (user_id, course_id, role) values (?, ?, ?)", (user_id, course_id, user_role))

# Done : End of for loop

# Commit/Save database to Filesystem
roster_db.commit()
# Close cursor
curr.close()
