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

	__debug = False
	__problems = []

	def solve(self):
		"""
		Method that reolves te problem and resturns the solutions in an array of strings
		"""

		ret = []

		for problem in self.__problems:
			if self.__debug:
				print('---- PROBLEM ----')

			totalOnes = 0
			for count in range(0, ((problem + 1) / 2 + 1)):
				# Convert the numbers to a binary string representation, and sum the number os ones
				ones = bin(problem - count).count('1') + bin(count).count('1')
				if ones > totalOnes:
					totalOnes = ones

				if self.__debug:
					print("Nums (%d): %d - %d" % (ones, problem - count, count))

			ret.append(totalOnes)
				

		return ret

	def __init__(self, inInputLines):
		""" Takes and parse the input lines into the internal structure """
		for line in inInputLines[1:]:
			self.__problems.append(int(line))

		if self.__debug:
			print(self.__problems)

# I'll use raw_input to get the lines because I can't import fileinput on the test server
fileLines = []
while True:
	try:
		fileLines.append(raw_input())
	except (EOFError):
		break #end of file reached

# Use the Bilateral class to do the calculations
problem = Problem(fileLines)
solutions = problem.solve()

# Send the output to the stdout
for count in range(0, len(solutions)):
	print("Case #%d: %d" % (count + 1, solutions[count]))
