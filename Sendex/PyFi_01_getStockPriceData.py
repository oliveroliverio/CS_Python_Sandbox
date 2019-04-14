# https://www.youtube.com/watch?v=2BrpKpWwT2A&t=4s

import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web


style.use('ggplot')


# later, how to set 'start' as "3 months from todays date"
start = dt.datetime(2019,4,9)


# later, how to set 'end' as "todays date/time"
end = dt.datetime(2019,4,14)


# import a dataframe from ticker symbol, the website, etc)
df = web.DataReader('AMGN', 'yahoo', start, end)
print(df.head())
