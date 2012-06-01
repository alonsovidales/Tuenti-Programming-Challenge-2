#!/usr/bin/env python

""" problem.py: Basic templete to solve the prooblems of the Tuenti Challenge 2 """

__author__ = "Alonso Vidales"
__email__ = "alonso.vidales@tras2.es"
__date__ = "2012-04-27"

class Problem:
	"""
	Generic class to solve the problems
	"""

	__debugLevel = 0
	__problems = []

	def __cleanWord(self, inWord):
		""" Removes all the control bites from a given hamming word
		and return a string with the bites with info """
		charPos = 1
		detectionPos = []
		while charPos <= len(inWord):
			detectionPos.append(charPos - 1)
			charPos *= 2

		result = ''
		# Only bytes out of a power of two position contain info
		for pos in range(0, len(inWord)):
			if detectionPos.count(pos) == 0:
				result += inWord[pos]

		return result

	def __hammingCheckAndCorrect(self, inStr):
		""" Check a string of bites from a given inStr string, and returns it corrected using
		the hamming code correction, for more info:
		http://www.youtube.com/watch?v=gQK9nROFX20&feature=related"""
		checks = []

		test = 1
		while test <= len(inStr):
			testResult = []
			initPos = True
			for pos in range(test, len(inStr) + test, test * 2):
				for count in range(0, test):
					if pos + count - 1 < len(inStr):
						testResult.append(inStr[pos + count - 1])

				initPos = False

			checks.append(testResult)

			test *= 2

		if self.__debugLevel >= 2:
			print(checks)

		errors = []
		for check in checks:
			if check[1:].count('1') % 2 != int(check[0]):
				errors.append('1')
			else:
				errors.append('0')

		errors.reverse()
		try:
			errorPos = int(''.join(errors), 2)
		except:
			return '0'

		if self.__debugLevel >= 2:
			print(''.join(errors))
			print(errorPos)

		if errorPos == 0:
			return inStr

		word = list(inStr)
		if word[errorPos - 1] == '1':
			word[errorPos - 1] = '0'
		else:
			word[errorPos - 1] = '1'

		return ''.join(word)

	def solve(self):
		"""
		Method that reolves te problem and resturns the solutions in an array of strings
		"""

		ret = []

		for problem in self.__problems:
			words = []
			# Use Hamming to check the bites, and remove the control bites
			for word in range(0, len(problem) / 7):
				words.append(self.__cleanWord(self.__hammingCheckAndCorrect(problem[word * 7:(word * 7) + 7])))

			if self.__debugLevel >= 1:
				print(len(''.join(words)))

			sentence = ''.join(words)

			# Check if we have string with a corrent number of bytes (each byte have 8 bites)
			if len(sentence) % 8 == 0:
				finalSent = ''
				for wordPos in range(0, len(sentence) / 8):
					charOrd = int(sentence[wordPos * 8: (wordPos * 8) + 8], 2)

					# Check if we obtained a valid ascii character, if is not a character only add "Error!"
					if charOrd >= 32 and charOrd <= 126:
						finalSent += chr(int(sentence[wordPos * 8: (wordPos * 8) + 8], 2))
					else:
						ret.append("Error!")
						break
	
				ret.append(finalSent)
			else:
				ret.append("Error!")

		return ret

	def __init__(self, inInputLines):
		""" Takes and parse the input lines into the internal structure """
		for line in inInputLines:
			self.__problems.append(line)

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
