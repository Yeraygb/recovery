#encoding: utf-8
 

""" archivo = open("/Users/ygonzale/Library/Application Support/Google/Chrome/Default/History")

linea = archivo.read()

inicio = linea.index("https")
final = linea.index(' ')
subcadena = linea[inicio +1:final +1]
print(subcadena)
while linea != '':

	linea = archivo.read()
	inicio = linea.index("https")
	final = linea.index('')
	subcadena = linea[inicio:final]
	#print(linea)
 """

archivo = open("/Users/ygonzale/Library/Application Support/Google/Chrome/Default/History")

linea = archivo.readline()
#print(linea)
while linea != '':

	linea = archivo.readline()
	#print(linea)
	if find("https"):
		inicio = linea.index("https")
		final = linea.index(' ')
		historial = linea[inicio:final]
		print(historial)

