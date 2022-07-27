import datetime
import sqlite3
import os
import sys

user = os.environ.get("USER")

year_min = int(sys.argv[1])
month_min = int(sys.argv[2])
day_min = int(sys.argv[3])
year_max = int(sys.argv[4])
month_max = int(sys.argv[5])
day_max = int(sys.argv[6])

ts_min = (datetime.datetime(year_min, month_min, day_min, 0, 0) - datetime.datetime(1601,1,1)).total_seconds()
ts_max = (datetime.datetime(year_max, month_max, day_max, 0, 0) - datetime.datetime(1601,1,1)).total_seconds()

ts_min = int(ts_min) * 1000000
ts_max = int(ts_max) * 1000000

#Ruta para Mac
con = sqlite3.connect('/Users/'+user+'/Library/Application Support/Google/Chrome/Default/History')
#Ruta para Windows
#con = sqlite3.connect('/Users/IEUser/AppData/Local/Google/Chrome/User Data/Default/History')
c = con.cursor()

c.execute("select * from urls where last_visit_time between '"+ str(ts_min) +"' and '"+ str(ts_max)  +"'")
results = c.fetchall()

for r in results:
	print(r)

c.close()
