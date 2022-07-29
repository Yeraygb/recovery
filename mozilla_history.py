import datetime
from distutils import extension
import sqlite3
import os
import sys
from os import path
import os.path


#user = os.environ.get("USER")

nombre_extension = "/Users/ygonzale/Library/Application Support/Firefox/Profiles/.default"

for archivo in nombre_extension:
	nombre, extension = os.path.splitext(archivo)
	print("El archivo '{}' se llama '{}' y tiene la extensión '{}'".format(
		archivo, nombre, extension))

data_path = os.path.expanduser('~')+"/.mozilla/firefox/t9szfr3w.default"
history_db = os.path.join(data_path, 'places.sqlite')

c = sqlite3.connect(history_db)

cursor = c.cursor()
#select_statement = "select moz_places.url, moz_places.visit_count from moz_places;"
select_statement = "select * from moz_places"
cursor.execute(select_statement)

results = cursor.fetchall()

for url, count in results:
	print(url)

cursor.close()
