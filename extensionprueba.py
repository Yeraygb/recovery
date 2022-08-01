import os
import re
pre_path = "/Users/ygonzale/Library/Application Support/Firefox/Profiles/"
directorys = os.listdir(pre_path)
for x in range(len(directorys)):
	path = os.path.join(pre_path, directorys[x])
	final_path = os.path.join(path, 'places.sqlite')
	if os.path.exists(final_path) == True:
		print("ole!" + final_path)


""" import fnmatch
import os
def get_pdfs():
	patata = "/Users/ygonzale/Library/Application Support/Firefox/Profiles/"
	directorys = os.listdir(patata)
	for x in range(len(directorys)):
		path = os.path.join(patata, directorys[x])
		for file in os.listdir(path):
			if os.path.isfile(path + "/" + file):
				if fnmatch.fnmatch(file, '*.sqlite'):
					i = 0
						database = file
						return database
archivo = get_pdfs()
print (archivo) """

""" import fnmatch
import os
def get_pdfs():
	directory_current = "/Users/ygonzale/Library/Application Support/Firefox/Profiles/"
	for file in os.listdir(directory_current):
		if os.path.isfile(directory_current + "/" + file):
			if fnmatch.fnmatch(file, '*.sqlite'):
				i = 0
				if file == 'places.sqlite':
					database = file
					return database
archivo = get_pdfs()
print (archivo) """