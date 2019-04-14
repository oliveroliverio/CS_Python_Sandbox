import sqlite3

# connect to database.  if doesn't exist, sqlite will create it
conn = sqlite3.connect('tutorial.db')

# create cursor
c = conn.cursor()

