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

def chrome_history(year_ini, month_ini, day_ini, year_final, month_final, day_final):
	print("GOOGLE CHROME HISTORY \n")
	year_min = int(year_ini)
	month_min = int(month_ini)
	day_min = int(day_ini)
	year_max = int(year_final)
	month_max = int(month_final)
	day_max = int(day_final)

	ts_min = (datetime.datetime(year_min, month_min, day_min, 0, 0) - datetime.datetime(1601,1,1)).total_seconds()
	ts_max = (datetime.datetime(year_max, month_max, day_max, 0, 0) - datetime.datetime(1601,1,1)).total_seconds()

	ts_min = int(ts_min) * 1000000
	ts_max = int(ts_max) * 1000000

	#Ruta para Mac
	#user = os.environ.get("USER")
	#con = sqlite3.connect('/Users/'+user+'/Library/Application Support/Google/Chrome/Default/History')

	#Ruta para Windows
	data = path.expandvars(r'%LOCALAPPDATA%/Google/Chrome/User Data/Default/History')
	con = sqlite3.connect(data)

	c = con.cursor()

	c.execute("select * from urls where last_visit_time between '"+ str(ts_min) +"' and '"+ str(ts_max)  +"'")
	results = c.fetchall()

	for r in results:
		print(r)

	c.close()

def without_arg():
	print("GOOGLE CHROME HISTORY 24H \n")
	year = get_year()
	mes = get_month()
	day = get_day()
	year_less1 = get_yearl_less1()
	month_less1 = get_month_less1()
	day_less1 = get_day_less1()
	ts_min = (datetime.datetime(year_less1, month_less1, day_less1, 0, 0) - datetime.datetime(1601,1,1)).total_seconds()
	ts_max = (datetime.datetime(year, mes, day, 0, 0) - datetime.datetime(1601,1,1)).total_seconds()

	ts_min = int(ts_min) * 1000000
	ts_max = int(ts_max) * 1000000

	#Ruta para Mac
	#user = os.environ.get("USER")
	#con = sqlite3.connect('/Users/'+user+'/Library/Application Support/Google/Chrome/Default/History')

	#Ruta para Windows
	data = path.expandvars(r'%LOCALAPPDATA%/Google/Chrome/User Data/Default/History')
	con = sqlite3.connect(data)

	c = con.cursor()

	c.execute("select * from urls where last_visit_time between '"+ str(ts_min) +"' and '"+ str(ts_max)  +"'")
	results = c.fetchall()

	for r in results:
		print(r)

	c.close()
