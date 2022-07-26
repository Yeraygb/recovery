
""" import sqlite3

#con = sqlite3.connect('C:\Users\$user\AppData\Local\Google\Chrome\User Data\Default\History')
con = sqlite3.connect('/Users/ygonzale/Library/Application Support/Google/Chrome/Default')

#/Users/ygonzale/Library/Application Support/Google/Chrome/Default

c = con.cursor()

c.execute("select url, title, visit_count, last_visit_time from urls")
results = c.fetchall()

for r in results:
	print(r)

c.close() """

archivo = open("/Users/ygonzale/Library/Application Support/Google/Chrome/Default/History")

linea = archivo.readline()
while linea != '':

	linea = archivo.readline()
	#linea = linea.split('')
	print(linea)
