from calendar import month
import datetime
from posixpath import split
import time as datetime
import sys
import chrome_history
import mozilla_history

def dates(fecha_inicio, fecha_final):
	print (fecha_inicio)
	print(fecha_final)
	split_inicio = fecha_inicio.split("/")
	vuelta_incio = "-".join(reversed(split_inicio))
	day = vuelta_incio.split("-")[0]
	month = vuelta_incio.split("-")[1]
	year = vuelta_incio.split("-")[2]
	print("dia", day)
	print("mes", month)
	print("ano", year)
	split_final = fecha_final.split("/")
	vuelta_final = "-".join(reversed(split_final))
	day_final = vuelta_final.split("-")[0]
	month_final = vuelta_final.split("-")[1]
	year_final = vuelta_final.split("-")[2]
	print("dia", day_final)
	print("mes", month_final)
	print("ano", year_final)
	

	chrome_history.chrome_history(year, month, day, year_final, month_final, day_final)
	mozilla_history.mozilla_without_arg()
	chrome_history.without_arg()
	#date = datetime.strptime(vuelta_incio, '%d-%m-%Y')

dates(sys.argv[1], sys.argv[2])
numargument = len(sys.argv) - 1
if numargument == 2:
	TODO EL PROGRAMA CON FECHAS
else:
	el prgroama con fechas por defeccto

