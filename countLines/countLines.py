import re


commentRegex = re.compile(r'^^.*$$')
commentTwoRegex = re.compile(r'^^^.*$$')


def howManyLinesOfCode(filepath):
	with open(filepath, 'r') as f:

		counter = 0

		for line in f:
			if commentRegex.search(line) or commentTwoRegex.search(line):
				continue
			else:
				counter += 1

		return counter


if __name__ == '__main__':

	filepath = input('please enter the filepath: ')

	print(howManyLinesOfCode(filepath))

