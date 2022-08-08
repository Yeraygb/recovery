#!/usr/bin/python3
import os
from os import path
import mozilla_history
import chrome_history
import sys
import open_programs
import chrome_history
import mozilla_history

def main():

	#Ruta Mac
	#user = os.environ.get("USER")
	#data_chrome = "/Users/"+user+"/Library/Application Support"

	#Ruta Windows
	data_chrome = "%LOCALAPPDATA%"

	path_compr = os.path.join(data_chrome, 'Google')
	

	print("GOOGLE CHROME HISTORY \n")
	if os.path.exists(path_compr) == True:
		numargument = len(sys.argv) - 1
		if numargument == 6:
			age1 = int(sys.argv[1])
			mes1 = int(sys.argv[2])
			day1 = int(sys.argv[3])
			age = int(sys.argv[4])
			mes = int(sys.argv[5])
			day = int(sys.argv[6])
			chrome_history.chrome_history(age1, mes1, day1, age, mes, day)
		else:
			chrome_history.without_arg()
	else:
		print("You have no instaled Google chrome")
		

	print(" \n \n ---------------------------------  \n \n")

	#Ruta Mac
	#data_firefox = "/Users/"+user+"/Library/Application Support"
	#fire_compr = os.path.join(data_firefox, 'Firefox')

	#data_firefox = path.expandvars(r'%APPDATA%')
	#Ruta Windows
	data_firefox = "%APPDATA%"
	fire_compr = os.path.join(data_firefox, 'Mozilla')

	if os.path.exists(fire_compr) == True:
		numargument = len(sys.argv) - 1
		if numargument == 6:
			age1 = int(sys.argv[1])
			mes1 = int(sys.argv[2])
			day1 = int(sys.argv[3])
			age = int(sys.argv[4])
			mes = int(sys.argv[5])
			day = int(sys.argv[6])
			mozilla_history.mozilla_history(age1, mes1, day1, age, mes, day)
		else:
			mozilla_history.mozilla_without_arg()
	else:
		print("You have no installed Firefox")

main()

#Start

#get date
def get_date():
	from datetime import date, timedelta
	date_now = date.today()
	return date_now

def get_date_less1():
	from datetime import date, timedelta
	dateless1 = date.today()+timedelta(days=-1)
	return dateless1

#check argument to give date or use default date
numargument = len(sys.argv) - 1
dateargmunet1 = str(sys.argv[1])
dateargmunet2 = str(sys.argv[2])

if dateargmunet1[4] == "/":
	splitslash1 = dateargmunet1.split("/")
	hyphenjoin1 = "-".join(splitslash1)
elif dateargmunet2[4] == "/":
	splitslash2 = dateargmunet2.split("/")
	hyphenjoin2 = "-".join(splitslash2)
elif dateargmunet1[2] == "-":
	split1 = dateargmunet1.split("-")
	join1 = "-".join(reversed(split1))
elif dateargmunet2[2] == "-":
	split2 = dateargmunet2.split("-")
	join2 = "-".join(reversed(split2))
elif dateargmunet1[4] == "-":
	if numargument == 2:
		date_start = sys.argv[1]
	else:
		date_start = get_date_less1()
elif dateargmunet2[4] == "-":
	if numargument == 2:
		date_end = sys.argv[2]
	else:
		date_end = get_date()
else:
	print("Wrong date format")
	
date_start = str(date_start)
date_end = str(date_end)
print(f"The chosen date range is from {date_start} to {date_end}")



#Navegators history------

#Check Mozilla Firefox------
#Ruta Mac
#user = os.environ.get("USER")
#data_chrome = "/Users/"+user+"/Library/Application Support"

#Ruta Windows
data_chrome = "%LOCALAPPDATA%"

chrome_check = os.path.join(data_chrome, 'Google')

#Check google chrome------
#Ruta Mac
#data_firefox = "/Users/"+user+"/Library/Application Support"
#fire_compr = os.path.join(data_firefox, 'Firefox')

#Ruta Windows
data_firefox = "%APPDATA%"
mozila_check = os.path.join(data_firefox, 'Mozilla')

year = date_start.split("-")[0]
month = date_start.split("-")[1]
day = date_start.split("-")[2]
year_final = date_end.split("-")[0]
month_final = date_end.split("-")[1]
day_final = date_end.split("-")[2]

if os.path.exists(chrome_check):
	if numargument == 2:
		chrome_history.chrome_history(year, month, day, year_final, month_final, day_final)
	else:
		chrome_history.without_arg()
else:
	print("You have no instaled Google chrome")

if os.path.exists(mozila_check):
	if numargument == 2:
		mozilla_history.mozilla_history(year, month, day, year_final, month_final, day_final)
	else:
		mozilla_history.mozilla_without_arg()
else:
	print("You have no instaled Mozilla Firefox")

#end navegators history

open_programs.open_programs(date_start, date_end)