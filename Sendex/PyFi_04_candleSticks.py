#!/usr/bin/env python
# https://www.youtube.com/watch?v=2BrpKpWwT2A&t=4s

import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
from mpl_finance import candlestick_ohlc
import matplotlib.dates as mdates

style.use('ggplot')

# read in data
df = pd.read_csv('tsla.csv', parse_dates=True, index_col=0)
# df['100ma'] = df['Adj Close'].rolling(window=100, min_periods=0).mean()

# can resample during a time period
# resample window at 10 days
# get the ohlc over 10 days, meaning, 'every 10 days, get the open/high/low/close'
# you can also replace ohlc with 'mean' to get the avg
df_ohlc = df['Adj Close'].resample('10D').ohlc()
# do this w/ vol too, but resample and aggregate by sum
df_volume = df['Volume'].resample('10D').sum()

# now we need to change the date format to matplotlib's date format
# what candlestick_ohlc wants is 'mdates, o,h,l,c' columns.  So need
# to convert dates to mdates by turning dates back into a column (used to be index).
df_ohlc.reset_index(inplace=True)
# convert to mdates
df_ohlc['Dates'] = df_ohlc['Dates'].map(mdates.date2num)

ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)
ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1, sharex=ax1)
# set x axis to this new mdates thing
ax1.xaxis_date()

# plot candle sticks, x axis as mdates, y axis as ohlc values,
# width=2 is width of candlesticks
candlestick_ohlc(ax1, df_ohlc.values, width=2, colorup='g')

# now plot volume.  instead of bars, fill volume
ax2.fill_between(df_volume.index.map(mdates.date2num), df_volume.values, 0)

plt.show()


