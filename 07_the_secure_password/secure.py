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

	__passChars = []
	__charsMap = {}
	__solutions = []

	def __appenPredSuc(self, inChar, inCharToAdd):
		try:
			self.__charsMap[inChar].index(inCharToAdd)
		except:
			self.__charsMap[inChar].append(inCharToAdd)

	def __removeChar(self, inChar, inCharsMap):
		""" Remove a character from the list and the antecers """
		result = {}
		for char, connections in inCharsMap.items():
			if char != inChar:
				result[char] = []

				for prev in connections:
					if prev != inChar:
						result[char].append(prev)
		return result

	def __getFirstChars(self, inCharsMap):
		""" Get the character without antecesors """
		charsMap = inCharsMap
		possibleChars = []
		for char, connections in inCharsMap.items():
			if len(connections) == 0:
				possibleChars.append(char)

		return possibleChars

	def __calcSolutions(self, inCharsMap, inCurrentSol = ''):
		""" Recursive method, gets all the possible solutions and store it in self.__solutions """
		if len(inCharsMap) == 0:
			self.__solutions.append(inCurrentSol)
		else:
			chars = self.__getFirstChars(inCharsMap)

			for char in chars:
				self.__calcSolutions(self.__removeChar(char, inCharsMap), inCurrentSol + char)

	def solve(self):
		"""
		Method that reolves te problem and resturns the solutions in an array of strings
		"""

		ret = []

		for passChars in self.__passChars:
			for charPos in range(0, len(passChars)):
				if self.__charsMap.get(passChars[charPos], False) == False:
					self.__charsMap[passChars[charPos]] = []

				for charSubPos in range(0, len(passChars)):
					if charPos > charSubPos:
						self.__appenPredSuc(passChars[charPos], passChars[charSubPos])

		self.__calcSolutions(self.__charsMap)

		return sorted(self.__solutions)

	def __init__(self, inInputLines):
		""" Takes and parse the input lines into the internal structure """
		for line in inInputLines:
			self.__passChars.append(line)

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
