Input: a file with following content: username groupname userid homepath
Output: a new file sorted by groupname alphabetically
example:
input:
'''
user1 group1 001 /usr/bin/
user2 group3 002 /usr/bin/
user3 group2 003 /usr/bin/
user4 group1 004 /usr/bin/
user5 group2 005 /usr/bin/
'''
output:
'''
user1 group1 001 /usr/bin/
user4 group1 004 /usr/bin/
user3 group2 003 /usr/bin/
user5 group2 005 /usr/bin/
user2 group3 002 /usr/bin/
'''
 
Note: there's a command line to do this "sort -t' ' -k2 filename", but we want you to do this in programming languages

class Content:
	def __init__(self, username, groupname, userid, homepath):
		self.username = username
		self.groupname = groupname
		self.userid = userid
		self.homepath = homepath
	def __repr__(self):
		return repr((self.username, self.groupname, self.userid, self.homepath))

lineList = []

with open('oldFile.txt', 'r') as old:
	for line in old:
		content = Content(line.split())
		lineList.append(content)

sortedList = sorted(lineList, key=attrgetter('groupname', 'userid'))

with open('newFile.txt', 'w') as new:
	for i in sortedList:
		new.write(i)


print(new.read())

