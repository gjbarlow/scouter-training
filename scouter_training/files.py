import csv

def readfile(fn):
	try:
		with open(fn, 'r') as fh:
			lines = fh.readlines()
	except:
		print('Input file (%s) does not exist'%fn)
		sys.exit(1)

	data_start = 8
	for n in range(data_start,len(lines)):
			if lines[n][0] == '"':
				data_start = n
				break

	return csv.reader(lines[data_start:], quotechar='"', delimiter=',', quoting=csv.QUOTE_ALL)