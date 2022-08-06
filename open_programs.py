import os
import sqlite3
import datetime
import json
from sqlite3 import Error

def create_connection(db_file):
	""" create a database connection to the SQLite database
		specified by the db_file
	:param db_file: database file
	:return: Connection object or None
	"""
	conn = None
	try:
		conn = sqlite3.connect(db_file)
	except Error as e:
		print(e)

	return conn


def select_task_by_type(conn, priority, date_start, date_end):
	"""
	Query tasks by priority
	:param conn: the Connection object
	:param priority:
	:return:
	"""
	cur = conn.cursor()
	cur.execute("SELECT StartTime, Payload, AppId FROM Activity WHERE ActivityType=?", (priority,))

	rows = cur.fetchall()

	#fecha_ini = input("Ingrese fecha inicial (AAAA-MM-DD): ")
	#fecha_fin = input("Ingrese fecha final (AAAA-MM-DD): ")
	fecha_ini = date_start
	fecha_fin = date_end
	utc_time_strt = datetime.strptime(fecha_ini, "%Y-%m-%d")
	utc_time_end = datetime.strptime(fecha_fin, "%Y-%m-%d")
	fecha_ini_x = (utc_time_strt - datetime(1970, 1, 1)).total_seconds()
	fecha_fin_x = (utc_time_end - datetime(1970, 1, 1)).total_seconds() + (24*60*60)

	for row in rows:
		cadena = row[1].decode()
		fecha = row[0]
		dt = datetime.fromtimestamp(row[0])
		if fecha >= fecha_ini_x and fecha <= fecha_fin_x:
			cadena2 = json.loads(row[1])
			cadena_app = json.loads(row[2])
			cadena_app_2 = cadena_app[0]
			res = {cadena2[key] for key in cadena2.keys() & {'appDisplayName'}}
			res2 = {cadena_app_2[key] for key in cadena_app_2.keys() & {'application'}}
			#print(dt, *res2, *res)
			dt_new = dt.strftime("%Y-%m-%d %H:%M:%S")
			file = open("04_open_programs.txt", "a")
			file.write(dt_new)
			file.write("\t")
			file.write(*res2)
			file.write("\n")
			#file.write(*res)
			file.close()

def open_programs(date_start, date_end):
	database = r"C:\\Users\\" + os.getlogin() + "\\AppData\\Local\\ConnectedDevicesPlatform\\L." + os.getlogin() + "\\ActivitiesCache.db"

	# create a database connection
	conn = create_connection(database)
	
	with conn:
		print("\nFichero de programas ejecutados creado")
		#select_task_by_type(conn, 5)
		select_task_by_type(conn, 6, date_start, date_end)
