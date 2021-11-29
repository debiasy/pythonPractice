import re



def diskUsage(file):

	serverList = []

	serverRegex = re.compile(r'server/d | (\d+(\.\d+)?%)')

	with open(file, 'r') as f:
		for line in f:
			serverList.append(serverRegex.findall(line))

	return serverList


def saveFile(serverList):

	with open('serverList.txt', 'w') as s:
		s.write('/n'.join(serverList))


if __name__ == '__main__':

	file = input('Please enter the server file: ')

	serverList = diskUsage(file)

	saveFile(serverList)


