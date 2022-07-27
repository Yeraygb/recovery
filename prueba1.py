import datetime
import sqlite3
import os
import sys

#epoch_time_min = datetime.datetime(2021, 7, 26, 0, 0).strftime('%s')
#epoch_time_max = datetime.datetime(2021, 7, 27, 0, 0).strftime('%s')
year_min = int(sys.argv[1])
month_min = int(sys.argv[2])
day_min = int(sys.argv[3])
year_max = int(sys.argv[4])
month_max = int(sys.argv[5])
day_max = int(sys.argv[6])
#ts_min= (datetime.datetime(2022,7,26,0,0) - datetime.datetime(1601,1,1)).total_seconds()
ts_min= (datetime.datetime(year_min, month_min, day_min, 0, 0) - datetime.datetime(1601,1,1)).total_seconds()
#ts_max= (datetime.datetime(2022,7,27,0,0) - datetime.datetime(1601,1,1)).total_seconds()
ts_max= (datetime.datetime(year_max, month_max, day_max, 0, 0) - datetime.datetime(1601,1,1)).total_seconds()


ts_min = int(ts_min) * 1000000
ts_max = int(ts_max) * 1000000

#print(int(ts) * 1000000)

#print(epoch_time_min)
#print(epoch_time_max)


con = sqlite3.connect('/Users/ygonzale/Library/Application Support/Google/Chrome/Default/History')
c = con.cursor()


c.execute("select * from urls where last_visit_time between '"+ str(ts_min) +"' and '"+ str(ts_max)  +"'")
#c.execute("select datetime(last_visit_time / 1000000 + (strftime('%s', '1601-01-01')), 'unixepoch', 'localtime') from urls")
results = c.fetchall()

for r in results:
	print(r)

c.close()
