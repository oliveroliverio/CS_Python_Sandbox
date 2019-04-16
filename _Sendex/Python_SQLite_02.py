# now we'll insert variables as parameters
import sqlite3, time, datetime, random

conn = sqlite3.connect('tutorial.db')
c = conn.cursor()

# create table
def createTable():
    c.execute('CREATE TABLE IF NOT EXISTS stuff2plot(unix REAL, datestamp TEXT, keyword TEXT, value REAL)')

def dataEntry():
    c.execute("INSERT INTO stuff3plot VALUES(31442134, '2019-04-12', 'Java', 3 )")
    conn.commit()
    c.close()
    conn.close

def dynamicDataEntry():
    unix = time.time()
    # format your datestamp
    date = str(datetime.datetime.frontimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
    keyword = 'Python'
    value = random.randrange(0,10)
    c.execute("INSERT INTO stuff2plot (unix, datestamp, keyword, value) VALUES (?, ?, ?, ?)",
          (unix, date, keyword, value))
    conn.commit()

for i in range(10):
    dynamicDataEntry()
    time.sleep(1)

c.close
conn.close()

createTable()
dataEntry()