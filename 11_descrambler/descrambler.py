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

	__pointsMap = {
		'A': 1,
		'B': 3,
		'C': 3,
		'D': 2,
		'E': 1,
		'F': 4,
		'G': 2,
		'H': 4,
		'I': 1,
		'J': 8,
		'K': 5,
		'L': 1,
		'M': 3,
		'N': 1,
		'O': 1,
		'P': 3,
		'Q': 10,
		'R': 1,
		'S': 1,
		'T': 1,
		'U': 1,
		'V': 4,
		'W': 4,
		'X': 8,
		'Y': 4,
		'Z': 10}

	__maxWordLen = 0
	__problems = []
	__possibleWords = []
	__debug = False

	def __calcScore(self, inWord):
		score = 0
		for charPos in range(0, len(inWord)):
			score += self.__pointsMap[inWord[charPos]]

		return score

	def __isPossible(self, inWord, inLetters, inProblemWord):
		""" Returns true if we can create the word inWord using the letters of
		inLetters, and one of the characters of the string inProblemWord """
		letters = inLetters[:]
		possible = True
		usedProblemWord = False

		for charPos in range(0, len(inWord)):
			if letters.count(inWord[charPos]) > 0:
				letters.pop(letters.index(inWord[charPos]))
			elif inProblemWord.find(inWord[charPos]) != -1 and not usedProblemWord:
				usedProblemWord = True
			else:
				possible = False
				break

		if possible and not usedProblemWord:
			for charPos in range(0, len(inWord)):
				if inProblemWord.find(inWord[charPos]) != -1:
					usedProblemWord = True
				
				
		return possible and usedProblemWord

	def solve(self):
		"""
		Method that reolves te problem and resturns the solutions in an array of strings
		"""

		ret = []

		for problem in self.__problems:
			score = 0
			# Check each word into the possible words dictionary (ordered alphabetic) and in case
			# that we can construct it, and the score of this word is higger than the current hight score, use it
			for word in self.__possibleWords:
				if word[1] > score and self.__isPossible(word[0], problem['letters'], problem['word']):
					score = word[1]
					maxWord = word[0]

			ret.append((maxWord, score))

		return ret

	def __init__(self, inInputLines):
		""" Takes and parse the input lines into the internal structure """
		for line in inInputLines[1:]:
			info = line.split()
			self.__problems.append({
				'letters':  [c for c in info[0]],
				'word': info[1]
			})

		f = open('descrambler_wordlist.txt', 'r')
		wordsList = []
		for word in f.read().split("\n"):
			wordsList.append((word, self.__calcScore(word)))

		# Order the array, in order to obtain the first max score alphabetic ordered
		self.__possibleWords = sorted(wordsList, key=lambda order: order[0])

		f.close()

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
	print("%s %d" % (solution[0], solution[1]))
