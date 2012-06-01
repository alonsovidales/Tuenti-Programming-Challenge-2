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

	__debugLevel = 0
	__problems = []

	def solve(self):
		"""
		Method that reolves te problem and resturns the solutions in an array of strings
		"""

		ret = []

		for problem in self.__problems:
			if self.__debugLevel > 0:
				print('\nNEW PROBLEM!!!!!')
				print(problem)

			# Create a new deck
			deck = []
			for card in range(0, problem['cards']):
				deck.append(card)

			originalDeck = deck[:]

			times = 0

			leftLen = problem['left']
			rightLen = problem['cards'] - problem['left'] 
			leftBigger = leftLen < rightLen

			if leftBigger:
				maxLen = leftLen
				extraCards = problem['cards'] - maxLen * 2 + maxLen
			else:
				maxLen = rightLen
				extraCards = problem['cards'] - maxLen * 2
	
			# Mix the result deks
			while deck != originalDeck or times == 0:
				#if self.__debugLevel >= 2:
				#	print("\nTIMES(%d)" % (times))
				#if self.__debugLevel >= 3:
				#	print(deck)

				times += 1
				if (times % 100000) == 0:
					print(times)
	
				resultDeck = []
				for position in range(1, maxLen + 1):
					resultDeck.append(deck[leftLen - position])
					resultDeck.append(deck[rightLen + leftLen - position])


				if leftBigger:
					cardsLeft = deck[leftLen:extraCards]
				else:
					cardsLeft = deck[:extraCards]

				cardsLeft.reverse()
				resultDeck.extend(cardsLeft)

				deck = resultDeck

			ret.append(times)

		return ret

	def __init__(self, inInputLines):
		""" Takes and parse the input lines into the internal structure """
		for line in inInputLines[1:]:
			info = line.split()
			self.__problems.append({
				'cards': int(info[0]),
				'left': int(info[1])})

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
for count in range(0, len(solutions)):
	print("Case #%d: %d" % (count + 1, solutions[count]))
