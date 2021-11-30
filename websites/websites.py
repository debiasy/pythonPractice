def topSites(file):

	tempList = []

	with open(file,'r') as f:
		for line in f:
			tempList.append(line.split())

	del templist[0]

	webDict = {}

	for site in list:
		if site in webDict:
			webDict[site] += 1
		else:
			webDict[site] = 1

	sortSites = sorted(webDict.items(), key=lambda x: x[1])

	counter = 0

	file = open('top5sites.txt', 'a')

	while counter < 5:
		for i in sortSites:
			file.write(i[0] + ',' + i[1], '\n')

	file.close()



if __name__ == '__main__':
	file = input('Please enter file path: ')

	topSites(file)
