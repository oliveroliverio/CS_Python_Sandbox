import sqlite3

# connect to database.  if doesn't exist, sqlite will create it
conn = sqlite3.connect('tutorial.db')

# create cursor
c = conn.cursor()

# create table
def createTable():
    # cursor does all the executions of things
    # create table called 'stuff2plot'
    # in parens is the columns and the type (unix, type real)
    c.execute('CREATE TABLE IF NOT EXISTS stuff2plot(unix REAL, datestamp TEXT, keyword TEXT, value REAL)')

# setup functions for inputting data
def dataEntry():
    c.execute("INSERT INTO stuff2plot VALUES(12342134, '2019-04-11', 'Python', 5 )")
    # save the entry.  run 'conn.commit()' any time you edit and make changes
    conn.commit()
    # when completely done run the stuff below.  essential for saving memory
    c.close()
    conn.close

createTable()
dataEntry()

# see the data created