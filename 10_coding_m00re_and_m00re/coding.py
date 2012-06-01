#!/usr/bin/env python

""" problem.py: Basic templete to solve the prooblems of the Tuenti Challenge 2 """

from itertools import *

__author__ = "Alonso Vidales"
__email__ = "alonso.vidales@tras2.es"
__date__ = "2012-04-27"

class Problem:
	"""
	Generic class to solve the problems
	"""

	__possibleOperators = ['@', '$', '&', '#', 'mirror', 'dance', 'conquer']
	__possibleActions = ['breadandfish', 'fire']
	__problems = []
	__debug = False

	def solve(self):
		"""
		Method that reolves te problem and resturns the solutions in an array of strings
		"""

		ret = []

		for problem in self.__problems:
			if self.__debug:
				print("\n\nNEW PROBLEM:")
				print(problem)

			for action in problem['actions']:
				if action == '@':
					numOne = problem['numbers'].pop(0)
					numTwo = problem['numbers'].pop(0)

					problem['numbers'].insert(0, numOne + numTwo)

					if self.__debug:
						print('@ %d + %d = %d' % (numOne, numTwo, numOne + numTwo))
						print(problem['numbers'])

				elif action == '$':
					numOne = problem['numbers'].pop(0)
					numTwo = problem['numbers'].pop(0)

					problem['numbers'].insert(0, numOne - numTwo)

					if self.__debug:
						print('$ %d - %d = %d' % (numOne, numTwo, numOne - numTwo))
						print(problem['numbers'])

				elif action == '&':
					numOne = problem['numbers'].pop(0)
					numTwo = problem['numbers'].pop(0)

					problem['numbers'].insert(0, numOne / numTwo)

					if self.__debug:
						print('& %d / %d = %d' % (numOne, numTwo, numOne / numTwo))
						print(problem['numbers'])

				elif action == '#':
					numOne = problem['numbers'].pop(0)
					numTwo = problem['numbers'].pop(0)

					problem['numbers'].insert(0, numOne * numTwo)

					if self.__debug:
						print('# %d * %d = %d' % (numOne, numTwo, numOne * numTwo))
						print(problem['numbers'])

				elif action == 'mirror':
					problem['numbers'].insert(0, problem['numbers'].pop(0) * -1)

					if self.__debug:
						print('mirror %d' % (problem['numbers'][0]))
						print(problem['numbers'])

				elif action == 'dance':
					numOne = problem['numbers'].pop(0)
					numTwo = problem['numbers'].pop(0)

					problem['numbers'].insert(0, numOne)
					problem['numbers'].insert(0, numTwo)

					if self.__debug:
						print('Dance')
						print(problem['numbers'])

				elif action == 'conquer':
					numOne = problem['numbers'].pop(0)
					numTwo = problem['numbers'].pop(0)

					problem['numbers'].insert(0, numOne % numTwo)

					if self.__debug:
						print('conquer')
						print(problem['numbers'])

			ret.append(problem['numbers'][0])

		return ret

	def __init__(self, inInputLines):
		""" Takes and parse the input lines into the internal structure """
		for line in inInputLines:
			parts = line.split()
			problem = {
				'numbers': [],
				'actions': []}

			numbers = 0
			numbersList = []
			for part in parts:
				if part != '.':
					if self.__possibleActions.count(part) > 0: # Basic actions into the numbers list
						if part == 'breadandfish':
							numbersList.insert(len(numbersList), numbersList[len(numbersList) - 1])
							if self.__debug:
								print('breadandfish')
								print(numbersList)
						elif part == 'fire':
							numbersList.pop()
							if self.__debug:
								print('fire')
								print(numbersList)
		
					elif self.__possibleOperators.count(part) > 0: #A new operation, add the numbers
						if len(numbersList) > 2:
							numbersList.reverse()
						problem['numbers'].extend(numbersList)
						problem['actions'].append(part)
						numbers = 0
						numbersList = []
					else:
						numbers += 1
						numbersList.append(int(part))

			if len(numbersList) > 0:
				if len(numbersList) > 2:
					numbersList.reverse()
				problem['numbers'].extend(numbersList)
				numbers = 0
				numbersList = []

			self.__problems.append(problem)

		if self.__debug:
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
