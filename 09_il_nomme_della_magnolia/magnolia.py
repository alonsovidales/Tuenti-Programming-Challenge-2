#!/usr/bin/env python

""" ATENTITON: First execute the parser.py in order to create the index files,
the index files should to be inside a directory called "documents" """

import json

__author__ = "Alonso Vidales"
__email__ = "alonso.vidales@tras2.es"
__date__ = "2012-04-27"

class Problem:
	"""
	Generic class to solve the problems
	"""

	__debug = False
	__problems = []
	__files = 800
	__wordsDictionary = {}
	__wordsToFind = []

	def solve(self):
		"""
		Method that reolves te problem and resturns the solutions in an array of strings
		"""

		try:
			ret = []

			for problem in self.__problems:
				ret.append(self.__wordsDictionary[problem['word']][problem['times'] - 1])

			return ret

		except:
			return False

	def __init__(self, inInputLines):
		""" Takes and parse the input lines into the internal structure """
		for line in inInputLines[1:]:
			info = line.split()
			self.__wordsToFind.append(info[0].lower())
			self.__problems.append({
				'word': info[0].lower(),
				'times': int(info[1])
			})

		# Load all the index files into memory and concatenate all in order to increase the search speed
		for fileName in range(1, self.__files + 1):
			if self.__debug:
				print("Processing: documents/" + str(fileName).rjust(4, '0') + ".ind")

			self.__dictWords = {}
			f = open("documents/" + str(fileName).rjust(4, '0') + ".ind", 'r')
			words = json.loads(f.read())
			f.close()

			for word in self.__wordsToFind:
				positions = words.get(word, False)
				if positions != False:
					try:
						self.__wordsDictionary[word].extend(positions)
					except:
						self.__wordsDictionary[word] = positions

			# Check if we can solve the problem, is we can stop the parsing of the input files
			if self.solve() != False:
				break

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
	print("%d-%d-%d" % (solution[0], solution[1] + 1, solution[2] + 1))
