import datetime
import sqlite3
import os
import sys

""" #epoch_time_min = datetime.datetime(2021, 7, 26, 0, 0).strftime('%s')
#epoch_time_max = datetime.datetime(2021, 7, 27, 0, 0).strftime('%s')


#Ruta de Firefox
con = sqlite3.connect('/Users/ygonzale/Library/Application Support/Firefox/Profiles/xxxxxxxx.default')
#ruta de chrome
#con = sqlite3.connect('/Users/'+user+'/Library/Application Support/Google/Chrome/Default/History')
#Users/$user/AppData/Local/Google/Chrome/User Data/Default/History
c = con.cursor()


c.execute("select url, title, visit_count, last_visit_time from urls")
#c.execute("select datetime(last_visit_time / 1000000 + (strftime('%s', '1601-01-01')), 'unixepoch', 'localtime') from urls")
results = c.fetchall()

for r in results:
	print(r)

c.close() """

archivo = open("/Users/ygonzale/Library/Application Support/Firefox/Profiles/xxxxxxxx.default")
linea = archivo.readline()

while linea != '':
	linea = archivo.readline()
	print(linea)
