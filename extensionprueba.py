import os
import re
carpetas = os.listdir("/Users/ygonzale/Library/Application Support/Firefox/Profiles/")
i = -1
while carpetas[i]:
	i+=1
	if carpetas == 's943o6hz.default-release-1':
		print(carpetas)


import fnmatch
import os
def get_pdfs():
	directory_current = "/Users/ygonzale/Library/Application Support/Firefox/Profiles/s943o6hz.default-release-1"
	for file in os.listdir(directory_current):
		if os.path.isfile(directory_current + "/" + file):
			if fnmatch.fnmatch(file, '*.sqlite'):
				i = 0
				if file == 'places.sqlite':
					database = file
					return database
archivo = get_pdfs()
print (archivo)