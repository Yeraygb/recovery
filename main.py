#!/usr/bin/python3
import os
from os import path
import mozilla_history
import chrome_history

def main():
	print("Write the date:")
	age1 = int(input())
	mes1 = int(input())
	day1 = int(input())
	age = int(input())
	mes = int(input())
	day = int(input())

	#Ruta Mac
	user = os.environ.get("USER")
	data_chrome = "/Users/"+user+"/Library/Application Support"

	#Ruta Windows
	#data_chrome = "%LOCALAPPDATA%"

	path_compr = os.path.join(data_chrome, 'Google')
	

	print("GOOGLE CHROME HISTORY \n")
	if os.path.exists(path_compr) == True:
		chrome_history.chrome_history(age1, mes1, day1, age, mes, day)
	else:
		print("You have no instaled Google chrome")
		

	print(" \n \n ---------------------------------  \n \n")
	print("MOZILLA FIREFOX \n")

	#Ruta Mac
	data_firefox = "/Users/"+user+"/Library/Application Support"
	fire_compr = os.path.join(data_firefox, 'Firefox')

	#Ruta Windowws
	#data_firefox = path.expandvars(r'%APPDATA%')
	#data_firefox = "%APPDATA%"
	#fire_compr = os.path.join(data_firefox, 'Mozilla')

	if os.path.exists(fire_compr) == True:
		mozilla_history.mozilla_history(age1, mes1, day1, age, mes, day)
	else:
		print("You have no installed Firefox")

main()


""" def pedirNumeroEntero():
 
	correcto=False
	num=0
	while(not correcto):
		try:
			num = int(input("Chose your election: "))
			correcto=True
		except ValueError:
			print('Error, introduce un numero entero')
	return num
  """



""" salir = False
opcion = 0

while not salir:
	print("MENU \n")
	print ("1. Google Chrome")
	print ("2. Mozilla Firefox")
	print ("4. Salir")

	opcion = int(input("Chose your election: "))
	
	age1 = int(input())
	mes1 = int(input())
	day1 = int(input())
	age = int(input())
	mes = int(input())
	day = int(input())

	if opcion == 1:
		print ("\nGoocgle chrome\n", chrome_history.chrome_history(age1, mes1, day1, age, mes, day))
		salir = True
	elif opcion == 2:
		print ("Opcion 2")
		mozilla_history.mozilla_history()
		salir = True
	elif opcion == 3:
		print("Opcion 3")
	elif opcion == 4:
		salir = True
	else:
		print ("Introduce un numero entre 1 y 3")

print ("Fin")
 """