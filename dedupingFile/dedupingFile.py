def dedupeFile(file):

	lineList = []

	try:
		with open(file, 'r') as f:

			for line in f:
				if line not in lineList:
					lineList.append(line)
				else:
					continue

	except:
		print('Incorrect file, please try again!')


	with open('dedupeFile.txt', 'w') as d:
		d.write('/n'.join(lineList))
	
