from select import select
import sqlite3
from os import path
from unittest import result

data = path.expandvars(r'%APPDATA%/Microsoft/Windows/Start Menu/Programs')
con = sqlite3.connect(data)

c = con.cursor()
c.execute("select FileName from Archivo")
results = c.fetchall()
for r in results:
	print(r)

c.close()
