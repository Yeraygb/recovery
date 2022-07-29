import os
import sqlite3
import datetime
import sqlite3
import os
import sys
from os import path

def get_year():
	from datetime import datetime, timedelta
	date = datetime.now()
	year = date.year
	return year

def get_month():
	from datetime import datetime, timedelta
	date = datetime.now()
	month = date.month
	return month

def get_day():
	from datetime import datetime, timedelta
	date = datetime.now()
	day = date.day
	return day

def get_yearl_less1():
	from datetime import datetime, timedelta
	dateless1 = datetime.today()+timedelta(days=-1)
	year = dateless1.year
	return year

def get_month_less1():
	from datetime import datetime, timedelta
	dateless1 = datetime.today()+timedelta(days=-1)
	month = dateless1.month
	return month

def get_day_less1():
	from datetime import datetime, timedelta
	dateless1 = datetime.today()+timedelta(days=-1)
	day = dateless1.day
	return day


user = os.environ.get("USER")
print(user)
numargument = len(sys.argv) - 1
if numargument == 6:
	
	year_min = int(sys.argv[1])
	month_min = int(sys.argv[2])
	day_min = int(sys.argv[3])
	year_max = int(sys.argv[4])
	month_max = int(sys.argv[5])
	day_max = int(sys.argv[6])

	ts_min = (datetime.datetime(year_min, month_min, day_min, 0, 0) - datetime.datetime(1970,1,1)).total_seconds()
	ts_max = (datetime.datetime(year_max, month_max, day_max, 0, 0) - datetime.datetime(1970,1,1)).total_seconds()

	ts_min = int(ts_min) * 1000000
	ts_max = int(ts_max) * 1000000
	data = path.expandvars(r'%LOCALAPPDATA%/Google/Chrome/User Data/Default/History')

	# Build Data path
	data_path = "/Users/"+user+"/Library/Application Support/Firefox/Profiles/s943o6hz.default-release-1/"
	history_db = os.path.join(data_path, 'places.sqlite')

	# Make connection with sqlite3 database
	c = sqlite3.connect(history_db)

	# Create cursor object to execute query
	cursor = c.cursor()
	select_statement = "select moz_places.url, moz_places.visit_count from moz_places where last_visit_date between '"+ str(ts_min) +"' and '"+ str(ts_max)  +"'"
	cursor.execute(select_statement)

	# Fetch the result and Prints the result
	results = cursor.fetchall()

	for url, count in results:
		print(url)

	# Close the cursor
	cursor.close()

else:
	year = get_year()
	mes = get_month()
	day = get_day()
	year_less1 = get_yearl_less1()
	month_less1 = get_month_less1()
	day_less1 = get_day_less1()

	ts_min = (datetime.datetime(year_less1, month_less1, day_less1, 0, 0) - datetime.datetime(1970,1,1)).total_seconds()
	ts_max = (datetime.datetime(year, mes, day, 0, 0) - datetime.datetime(1970,1,1)).total_seconds()

	ts_min = int(ts_min) * 1000000
	ts_max = int(ts_max) * 1000000

	# Build Data path
	#Ruta para Mac
	data_path = "/Users/"+user+"/Library/Application Support/Firefox/Profiles/s943o6hz.default-release-1/"
	history_db = os.path.join(data_path, 'places.sqlite')
	#Ruta para Windows
	data_path = "/Users/"+user+"/Appdata/Roaming/Firefox/Profiles/opy8vubs.default-release/"
	history_db = os.path.join(data_path, 'places.sqlite')

	# Make connection with sqlite3 database
	c = sqlite3.connect(history_db)

	# Create cursor object to execute query
	cursor = c.cursor()
	select_statement = "select moz_places.url, moz_places.visit_count from moz_places where last_visit_date between '"+ str(ts_min) +"' and '"+ str(ts_max)  +"'"
	cursor.execute(select_statement)

	# Fetch the result and Prints the result
	results = cursor.fetchall()

	for url, count in results:
		print(url)

	# Close the cursor
	cursor.close()