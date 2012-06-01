#!/usr/bin/env python

""" problem.py: Basic templete to solve the prooblems of the Tuenti Challenge 2 """

import md5

__author__ = "Alonso Vidales"
__email__ = "alonso.vidales@tras2.es"
__date__ = "2012-04-27"

class Problem:
	"""
	Generic class to solve the problems
	"""

	__debug = False
	__problem = {}

	def __addTransforms(self, inOrigin, inTransforms):
		""" apply the transforms in inTransforms into the inOrigin transforms
		array in order to calculate the final transforms """
		finalTrans = {}

		for origChar, origTrans in inOrigin.items():
			finalTrans[origChar] = []
			for trans in origTrans:
				if inTransforms.get(trans, False) != False:
					finalTrans[origChar].extend(inTransforms[trans])
				else:
					finalTrans[origChar].append(trans)

		for char, transform in inTransforms.items():
			if inOrigin.get(char, False) == False:
				finalTrans[char] = transform

		return finalTrans

	def solve(self):
		"""
		Method that reolves te problem and resturns the solutions in an array of strings
		"""

		finalTransforms = self.__problem['transforms'][0]
		for transform in self.__problem['transforms'][1:]:
			finalTransforms = self.__addTransforms(finalTransforms, transform)


		# First do all the transformations, and calculate the result for each character
		joinedTransforms = {}
		for char, transform in finalTransforms.items():
			joinedTransforms[char] = ''.join(transform)

		if self.__debug:
			print(joinedTransforms)
			print('transforms ' + str(len(self.__problem['people'])))

		# Apply each transfor on each character
		result = ''
		for char in self.__problem['people']:
			transformed = joinedTransforms.get(char, False)
			if transformed != False:
				result += transformed
			else:
				result += char

		if self.__debug:
			print(result)

		# Create the MD5 and returns in
		m = md5.new()
		m.update(result)

		return m.hexdigest()

	def __init__(self, inInputLines):
		""" Takes and parse the input lines into the internal structure """
		people = []
		for peopPos in range(0, len(inInputLines[0])):
			people.append(inInputLines[0][peopPos])

		self.__problem = {
			'people': people,
			'transforms': []}

		for line in inInputLines[1:]:
			transformsParsed = {}
			transforms = line.split(',')
			for transform in transforms:
				info = transform.split('=>')
				targets = []
				for targetPos in range(0, len(info[1])):
					targets.append(info[1][targetPos])

				transformsParsed[info[0]] = targets

			self.__problem['transforms'].append(transformsParsed)

		if self.__debug:
			print(self.__problem)

# I'll use raw_input to get the lines because I can't import fileinput on the test server
fileLines = []
while True:
	try:
		fileLines.append(raw_input())
	except (EOFError):
		break #end of file reached

problem = Problem(fileLines)
print(problem.solve())
