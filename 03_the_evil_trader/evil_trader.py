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
	__stocks = []

	def __reduce(self, inStocks):
		""" Removes the unnecesary numbers, for example if we have 1 1 7 1 8 9 1,
		we will need only the ones at the extreams 1 7 8 9 1 """

		red = []
		essentialPos = []

		inserted = {}
		for stock in inStocks:
			if not inserted.get(stock, False):
				# Get only the fisrt and las occurence, in order to remove the rest
				first = len(inStocks)
				last = 0
				for pos in range(0, len(inStocks)):
					if (inStocks[pos] == stock):
						if pos > last:
							last = pos
						if pos < first:
							first = pos

				if (self.__debug):	
					print(str(stock) + ' - ' + str(first) + ' - ' + str(last))

				essentialPos.append(first)
				essentialPos.append(last)
				inserted[stock] = True


		if (self.__debug):	
			print(essentialPos)

		# Create the reduced array without the unnecesary numbers
		for pos in range(0, len(inStocks)):
			if essentialPos.count(pos) > 0:
				red.append(self.__stocks[pos])

		if (self.__debug):	
			print(red)

		return red

	def solve(self):
		"""
		Method that reolves te problem and resturns the solutions in an array of strings
		"""

		reducedStocks = self.__reduce(self.__stocks)

		bestSolution = (0, 0, 0)
		# Check all the possible solutions
		for convination in combinations(reducedStocks, 2):
			gain = convination[1] - convination[0]
			if (gain > bestSolution[2]):
				bestSolution = (convination[0], convination[1], gain)

		return (
			self.__stocks.index(bestSolution[0]), #the fist occurence of the smallest
			len(self.__stocks) - self.__stocks[::-1].index(bestSolution[1]) - 1, # The last occurrence of the bigger number
			bestSolution[2]) # the max gain

	def __init__(self, inInputLines):
		""" Takes and parse the input lines into the internal structure """
		for line in inInputLines:
			self.__stocks.append(int(line))

# I'll use raw_input to get the lines because I can't import fileinput on the test server
fileLines = []
while True:
	try:
		fileLines.append(raw_input())
	except (EOFError):
		break #end of file reached

# Use the Bilateral class to do the calculations
problem = Problem(fileLines)
solution = problem.solve()
print("%d %d %d" % (solution[0] * 100, solution[1] * 100, solution[2]))
