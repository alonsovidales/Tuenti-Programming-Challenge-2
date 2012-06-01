#!/usr/bin/env python

""" parser.py this file only reads all the files, and creates a JSON output with all the words ready to search
IMPORTANT: The documents should be in a directory called "documents" inside the same directory of this script
Usage: ./parser.py > wordsIndex """

__author__ = "Alonso Vidales"
__email__ = "alonso.vidales@tras2.es"
__date__ = "2012-04-27"

import json

class Parser:
	"""
	Generic class to solve the problems
	"""

	__dictWords = {}
	__files = 800

	def parseAndWriteJson(self):
		"""
		Read all the files, and create the index
		"""

		for fileName in range(1, self.__files + 1):
			self.__dictWords = {}
			f = open("documents/" + str(fileName).rjust(4, '0'), 'r')
			lines = f.read().split("\n")

			for line in range(0, len(lines)):
				words = lines[line].split()
				for word in range(0, len(words)):
					lowWord = words[word].lower()
					try:
						self.__dictWords[lowWord].append([int(fileName), line, word])
					except:
						self.__dictWords[lowWord] = [[int(fileName), line, word]]

			f.close()
			fo = open("documents/" + str(fileName).rjust(4, '0') + ".ind", 'w')
			fo.write(json.dumps(self.__dictWords))
			fo.close()

problem = Parser()
problem.parseAndWriteJson()
