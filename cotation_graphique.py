import sqlite3
import datetime
import matplotlib.pyplot as plt
from matplotlib.dates import DayLocator, YearLocator, MonthLocator, DateFormatter, date2num
import datetime
import numpy as np

years = YearLocator()   # every year
months = MonthLocator()  # every month
days = DayLocator()
yearsFmt = DateFormatter('%Y')
monthFmt = DateFormatter('%m')
daysFmt = DateFormatter('%d')

date = datetime.datetime.now()
d = "{2}-{1}-{0}".format(date.day,date.month,date.year)
conn = sqlite3.connect(r'e:\doc\technip.db')
c = conn.cursor()
t = (d,)
#c.execute('select mme20,mme12,mme26 from cotation where date < ? order by date DESC LIMIT 1', t)

d1 = []
c1 = []
mme20 = []
mme12 = []
mme26 = []

for row in c.execute('select date,cotation,mme20,mme12,mme26,volume from cotation'):
    d1.append(row[0])
    c1.append(row[1])
    mme20.append(row[2])
    mme12.append(row[3])
    mme26.append(row[4])

conn.close()

dates = [date2num(datetime.datetime.strptime(i, '%Y-%m-%d')) for i in d1]

fig, ax = plt.subplots()
ax.plot_date(dates, c1, '-')
ax.plot_date(dates, mme20, '-')
ax.plot_date(dates, mme12, '-')
ax.plot_date(dates, mme26, '-')


# format the ticks
ax.xaxis.set_major_locator(months)
ax.xaxis.set_major_formatter(daysFmt)
ax.xaxis.set_minor_locator(days)
ax.autoscale_view()


# format the coords message box
def price(x):
    return '%1.2f' % x
ax.fmt_xdata = DateFormatter('%Y-%m-%d')
ax.fmt_ydata = price
ax.grid(True)

fig.autofmt_xdate()
plt.show()
