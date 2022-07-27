import sys

numargument = len(sys.argv) - 1
if numargument < 1:
	print("Number of argument incorrect")
else:
	print(numargument)
	print(sys.argv[1])