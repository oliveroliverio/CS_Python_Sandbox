#!/usr/bin/env python
# https://www.youtube.com/watch?v=2BrpKpWwT2A&t=4s

import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
import time
import os

from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

style.use('ggplot')

#--------timed explanation functions--------------------
#-------------------------------------------------------
def timedMessage(message):
 #   time.sleep(1)
    print("\n")
    print(message)
    # waits for user keyboard enter input
    print("\n\n")
 #   input("press enter to continue")
    # I want to clear the console screen but the bottom doesn't work
    #os.system('clear')

# read in data
df = pd.read_csv('tsla.csv', parse_dates=True, index_col=0)

# make new MA column
df['100ma'] = df['Adj Close'].rolling(window=100).mean()

# drop NAs
df.dropna(inplace=True)

# change the df.MA to below, so that it won't require any number of periods to calculate MA
# it'll just be whatever the current price is
df['100ma'] = df['Adj Close'].rolling(window=100, min_periods=0).mean()

print(df.head())

# plot MA overlayed w/ price
# making plots on top of plots...?
# take grid size, 6 rows, 1 col.  the start point is 0,0
ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)
ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1)

# now that these subplots are generated, we can graph to them
# plot simple line, we have x axis as date, which is the index
# the y axis is the adj close, then another line for 100ma
ax1.plot(df.index, df['Adj Close'])
ax1.plot(df.index, df['100ma'])
# make another plot (actually bars) below as volume
ax2.bar(df.index, df['Volume'])

plt.show()

# quick change
timedMessage("quick change, modify ax2 to sharex=ax1, so that when you zoom, both plots align")
ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)
ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1, sharex=ax1)
ax1.plot(df.index, df['Adj Close'])
ax1.plot(df.index, df['100ma'])
ax2.bar(df.index, df['Volume'])

plt.show()


