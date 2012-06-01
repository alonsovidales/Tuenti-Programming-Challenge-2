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
			widthStiches = problem['width'] * problem['ct']
			heightStiches = problem['height'] * problem['ct']
			allowedSize = True

			fontSize = 0

			while allowedSize:
				fontSize += 1

				if self.__debug:
					print('\n\nChecking ' + str(fontSize))

				wordWidthHeighStiches = fontSize
				usedWidth = 0
				usedHeight = wordWidthHeighStiches

				if wordWidthHeighStiches > heightStiches:
					if self.__debug:
						print("Height problem")

					allowedSize = False
				else:
					for word in problem['words']:
						if usedWidth > 0: # Are we not in the first word of the line?
							spacedWord = ' ' + word
						else:
							spacedWord = word

						if self.__debug:
							print(
								"Word: \"%s\" Chars: %d wordWidthHeighStiches: %d usedWidth: %d totalWidt: %d" %
								(word, len(spacedWord), wordWidthHeighStiches, usedWidth, widthStiches))

						if (len(spacedWord) * wordWidthHeighStiches) + usedWidth <= widthStiches: # Check if have space in the current line for this word
							usedWidth += len(spacedWord) * wordWidthHeighStiches
							if self.__debug:
								print("ADDDED: " + word + ' - ' + str(usedWidth))
						elif (len(word) * wordWidthHeighStiches <= widthStiches) and (usedHeight + wordWidthHeighStiches <= heightStiches): # Can we add a new line?
							if self.__debug:
								print('NEW LINE')
							usedWidth = len(word) * wordWidthHeighStiches
							usedHeight += wordWidthHeighStiches
						else:
							if self.__debug:
								print('No space left :(')
							allowedSize = False
							break

			fontSize -= 1
			if self.__debug:
				print('MAX FONT SIZE: ' + str(fontSize))

			# OK, we know the font size, and the number of characters, then
			# we can calculate the inches that we will need using the given formula :)
			characters = 0
			for word in problem['words']:
				characters += len(word)

			if self.__debug:
				print('TOTAL Chars: ' + str(characters))

			stiches = characters * ((float(fontSize) ** 2) / 2)
			if self.__debug:
				print('Stiches: ' + str(stiches))
			inches = stiches / problem['ct']
			if self.__debug:
				print('Inches: ' + str(inches))
			ret.append(round(inches))

		return ret

	def __init__(self, inInputLines):
		""" Takes and parse the input lines into the internal structure """
		for problem in range(0, int(inInputLines[0])):
			info = map(int, inInputLines[(problem * 2) + 1].split())
			self.__problems.append({
				'width': info[0],
				'height': info[1],
				'ct': info[2],
				'words': inInputLines[(problem * 2) + 2].split()
			})

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
for counter in range(0, len(solutions)):
	print("Case #%d: %d" % (counter + 1, solutions[counter]))
