import sqlite3
import os
import sys

numargument = len(sys.argv) -1
if numargument < 1:
	print("Number of argument incorrect")
else:
	con = sqlite3.connect('/Users/ygonzale/Library/Application Support/Google/Chrome/Default/History')
	c = con.cursor()

	c.execute("select url, title, visit_count, last_visit_time from urls")
	results = c.fetchall()

	for r in results:
		print(r)

	c.close()

