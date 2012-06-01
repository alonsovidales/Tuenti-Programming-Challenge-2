#!/usr/bin/env python

""" problem.p'y': Basic templete to solve the prooblems of the Tuenti Challenge 2 """

__author__ = "Alonso Vidales"
__email__ = "alonso.vidales@tras2.es"
__date__ = "2012-04-27"

class Problem:
	"""
	Generic class to solve the problems
	"""

	__debug = False

	# The initial position where the user have the finger
	__currentPos = {
		'x': 1,
		'y': 3
	}

	__noChars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ' ']

	# A Map with the position into the cell keyboard and the number of times that the user shoudl to press the button
	__characters = {
		'a': {
			'pos': {
				'x': 1,
				'y': 0
			},
			'times': 1
		},
		'b': {
			'pos': {
				'x': 1,
				'y': 0
			},
			'times': 2
		},
		'c': {
			'pos': {
				'x': 1,
				'y': 0
			},
			'times': 3
		},
		'd': {
			'pos': {
				'x': 2,
				'y': 0
			},
			'times': 1
		},
		'e': {
			'pos': {
				'x': 2,
				'y': 0
			},
			'times': 2
		},
		'f': {
			'pos': {
				'x': 2,
				'y': 0
			},
			'times': 3
		},
		'g': {
			'pos': {
				'x': 0,
				'y': 1
			},
			'times': 1
		},
		'h': {
			'pos': {
				'x': 0,
				'y': 1
			},
			'times': 2
		},
		'i': {
			'pos': {
				'x': 0,
				'y': 1
			},
			'times': 3
		},
		'j': {
			'pos': {
				'x': 1,
				'y': 1
			},
			'times': 1
		},
		'k': {
			'pos': {
				'x': 1,
				'y': 1
			},
			'times': 2
		},
		'l': {
			'pos': {
				'x': 1,
				'y': 1
			},
			'times': 3
		},
		'm': {
			'pos': {
				'x': 2,
				'y': 1
			},
			'times': 1
		},
		'n': {
			'pos': {
				'x': 2,
				'y': 1
			},
			'times': 2
		},
		'o': {
			'pos': {
				'x': 2,
				'y': 1
			},
			'times': 3
		},
		'p': {
			'pos': {
				'x': 0,
				'y': 2
			},
			'times': 1
		},
		'q': {
			'pos': {
				'x': 0,
				'y': 2
			},
			'times': 2
		},
		'r': {
			'pos': {
				'x': 0,
				'y': 2
			},
			'times': 3
		},
		's': {
			'pos': {
				'x': 0,
				'y': 2
			},
			'times': 4
		},
		't': {
			'pos': {
				'x': 1,
				'y': 2
			},
			'times': 1
		},
		'u': {
			'pos': {
				'x': 1,
				'y': 2
			},
			'times': 2
		},
		'v': {
			'pos': {
				'x': 1,
				'y': 2
			},
			'times': 3
		},
		'w': {
			'pos': {
				'x': 2,
				'y': 2
			},
			'times': 1
		},
		'x': {
			'pos': {
				'x': 2,
				'y': 2
			},
			'times': 2
		},
		'y': {
			'pos': {
				'x': 2,
				'y': 2
			},
			'times': 3
		},
		'z': {
			'pos': {
				'x': 2,
				'y': 2
			},
			'times': 4
		},
		'0': {
			'pos': {
				'x': 1,
				'y': 3
			},
			'times': 1
		},
		'1': {
			'pos': {
				'x': 0,
				'y': 0
			},
			'times': 2
		},
		'2': {
			'pos': {
				'x': 1,
				'y': 0
			},
			'times': 4
		},
		'3': {
			'pos': {
				'x': 2,
				'y': 0
			},
			'times': 4
		},
		'4': {
			'pos': {
				'x': 0,
				'y': 1
			},
			'times': 4
		},
		'5': {
			'pos': {
				'x': 1,
				'y': 1
			},
			'times': 4
		},
		'6': {
			'pos': {
				'x': 2,
				'y': 1
			},
			'times': 4
		},
		'7': {
			'pos': {
				'x': 0,
				'y': 2
			},
			'times': 5
		},
		'8': {
			'pos': {
				'x': 1,
				'y': 2
			},
			'times': 4
		},
		'9': {
			'pos': {
				'x': 2,
				'y': 1
			},
			'times': 5
		},
		' ': {
			'pos': {
				'x': 0,
				'y': 0
			},
			'times': 1
		},
		'*': { #Represents the change to cap block
			'pos': {
				'x': 2,
				'y': 3
			},
			'times': 1
		}
	}
	__problems = []


	def __moveFingerTime(self, inFromPos, inToPos):
		if (inFromPos['x'] == inToPos['x']) and (inFromPos['y'] == inToPos['y']):
			return 0

		if (inFromPos['x'] == inToPos['x']):
			if (self.__debug):
				print('Move Y ' + str(abs(inFromPos['y'] - inToPos['y'])))
			return 300 * abs(inFromPos['y'] - inToPos['y'])

		if (inFromPos['y'] == inToPos['y']):
			if (self.__debug):
				print('Move X ' + str(abs(inFromPos['x'] - inToPos['x'])))
			return 200 * abs(inFromPos['x'] - inToPos['x'])

		if (inFromPos['y'] > inToPos['y']):
			nextY = inFromPos['y'] - 1
		else:
			nextY = inFromPos['y'] + 1

		if (inFromPos['x'] > inToPos['x']):
			nextX = inFromPos['x'] - 1
		else:
			nextX = inFromPos['x'] + 1

		if (self.__debug):
			print('Move diag')

		# Diagonal movement
		return 350 + self.__moveFingerTime({
			'x': nextX,
			'y': nextY}, inToPos)

	def solve(self):
		"""
		Method that reolves te problem and resturns the solutions in an array of strings
		"""

		ret = []
		initPos = self.__currentPos

		for problem in self.__problems:
			time = 0
			if (self.__debug):
				print('---- PROBLEM -----')

			for char in problem:
				if (self.__currentPos['x'] == char['pos']['x']) and (self.__currentPos['y'] == char['pos']['y']):
					time += 500

				time += self.__moveFingerTime(self.__currentPos, char['pos'])
				time += 100 * char['times']
				self.__currentPos = char['pos']
				if (self.__debug):
					print('CharPuls')
					print(self.__currentPos)

			self.__currentPos = initPos

			ret.append(time)

		return ret

	def __parseLine(self, inLine):
		ret = []
		lower = True
		devString = ''

		for pos in range(0, len(inLine)):
			if (inLine[pos].lower() != inLine[pos]):
				if lower:
					ret.append(self.__characters['*'])
					devString += '*'
				lower = False
			else:
				if self.__noChars.count(inLine[pos]) == 0:
					if not lower:
						ret.append(self.__characters['*'])
						devString += '*'
					lower = True

			devString += inLine[pos].lower()
			ret.append(self.__characters[inLine[pos].lower()])

		if (self.__debug):
			print(devString)

		return ret

	def __init__(self, inInputLines):
		""" Takes and parse the input lines into the internal structure """

		for line in inInputLines[1:]:
			self.__problems.append(self.__parseLine(line))

		if (self.__debug):
			print(self.__problems)

# I'll use raw_input to get the lines because I can't import fileinput on the test server
fileLines = []
while True:
	try:
		fileLines.append(raw_input())
	except (EOFError):
		break #end of file reached

problem = Problem(fileLines)
solutions = problem.solve()

# Send the output to the stdout
for solution in solutions:
	print(solution)	
