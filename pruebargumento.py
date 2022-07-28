import sys


numargument = len(sys.argv) - 1
if numargument < 1:
	print("Number of argument incorrect")
else:
	init = sys.argv[2]
	final = sys.argv[3]

	print



	------
	
import sqlite3
import os
import sys

numargument = len(sys.argv) -1
if numargument < 1:
	print("Number of argument incorrect")
else:

	con = sqlite3.connect('/Users/ygonzale/Library/Application Support/Google/Chrome/Default/History')
	c = con.cursor()

	c.execute("select * from urls")
	results = c.fetchall()

	for r in results:
		print(r)

	c.close()


""" 	init = sys.argv[2]
	final = sys.argv[3] """

from datetime import datetime
import sqlite3
import os
import sys

time_init = 5
datetime(time_init * 1000000 + (strftime('%s', '1601-01-01T05:30:00')), 'unixepoch')
print(time_init)

con = sqlite3.connect('/Users/ygonzale/Library/Application Support/Google/Chrome/Default/History')
c = con.cursor()

c.execute("select last_visit_time from urls where last_visit_time between '13303387129409477' and '13303392049545390'")
#datetime(last_visit_time / 1000000 + (strftime('%s', '1601-01-01T05:30:00')), 'unixepoch')
results = c.fetchall()

for r in results:
	print(r)

c.close()
