class Content:
	def __init__(self, username, groupname, userid, homepath):
		self.username = username
		self.groupname = groupname
		self.userid = userid
		self.homepath = homepath
	def __repr__(self):
		return repr((self.username, self.groupname, self.userid, self.homepath))

	
def sortByGroup(oldFile):
	lineList = []

	with open(oldFile, 'r') as old:
		for line in old:
			content = Content(line.split())
			lineList.append(content)

	sortedList = sorted(lineList, key=attrgetter('groupname', 'userid'))

	with open('newFile.txt', 'w') as new:
		for i in sortedList:
			new.write(i)


	print(new.read())
	
oldFile = input('Please enter the file you would like to sort: ')
print(oldFile)
sortByGoup(oldFile)

