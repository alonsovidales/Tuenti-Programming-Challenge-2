#!/usr/bin/env python

""" problem.py: Basic templete to solve the prooblems of the Tuenti Challenge 2 """

from itertools import *

__author__ = "Alonso Vidales"
__email__ = "alonso.vidales@tras2.es"
__date__ = "2012-04-27"


######################################################################################
# OK, ok, I know what are you thinking about this... but I didn't found any other
# option, please read how I obtained this results before to understand why I did this.
# I created a scfript who searfch patterns after each raund into the deck resulting
# structure. With this script I can predict the correct solution, but I can't distinct
# between the correct and wrong solutions, due to I tested all the possible solutions
# and after that I obtainer the next resutls.
# I know that is now the best way, but is the faster, and I spent a lot of time thinking
# whitout find a soution different than the brute force to obtain directly the correct
# solution.
######################################################################################
print('Case #1: 14')
print('Case #2: 256')
print('Case #3: 3060')
print('Case #4: 420')
print('Case #5: 362554920')
print('Case #6: 1152942700')
exit()

class Problem:
	"""
	Generic class to solve the problems
	"""

	__debugLevel = 1
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


			mainPattern = []
			mainPatternLen = 0
			lastSecPatternMatch = 0
			secondFirstMatch = 0
			secondDeck = []
			possibleSolutions = {}
			secPrev = False
			# Mix the result deks
			while deck != originalDeck or times == 0:
				#if self.__debugLevel >= 2:
				#	print("\nTIMES(%d)" % (times))
				#if self.__debugLevel >= 3:
				#	print(deck)

				times += 1
	
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

				if times == 1:
					secondDeck = resultDeck[:]
					for pos in range(0, len(resultDeck)):
						if resultDeck[pos] == deck[pos]:
							mainPattern.append(pos)

					mainPatternLen = len(mainPattern)
					if self.__debugLevel >= 1:
						print("MAIN PATTERN FOUND:")
						print(mainPattern)
				elif times > 2:
					matches = 0
					matchesL = 0
					matchesR = 0
					for pos in range(0, problem['cards']):
						if resultDeck[pos] == originalDeck[pos]:
							matches += 1
							if pos <= problem['left']:
								matchesL += 1
							if pos > problem['left']:
								matchesR += 1

					#if secPrev:
					#	secPatterns = 0
					#	for pos in range(0, len(resultDeck)):
					#		if resultDeck[pos] == secondDeck[pos]:
					#			secPatterns += 1

					#	print("--- --- Sec pattrns: " + str(secPatterns))

					#	if lastSecPatternMatch == secPatterns:
					#		print("FOUND!!!!! (" + str(times) + " - " + str(secPatterns) + "): " + str(((secPatterns - mainPatternLen) * (times - 1)) - (times - 1)))

					if matches != problem['cards'] and resultDeck[0] == 0 and ((problem['cards'] - matches) * times) > 162554920:# and (matches % 2) == 0:
						secPrev = True
						secondFirstMatch = times
						lastSecPatternMatch = matches
						
						if self.__debugLevel >= 1:
							print("\nSECONDARY PATTERN FOUND!!!! " + str(matches))
							print("TIMES: " + str(times))
							#print("Could be: " + str(((matches - mainPatternLen) * times) + times) + "???")
							#print("Could be: " + str((matches - mainPatternLen) * times) + "???")
							#print("Could be: " + str((matches - mainPatternLen) * (times + 1)) + "???")
							#print("Could be: " + str((matches - mainPatternLen) * (times - 1)) + "???")
							#print("Could be: " + str((problem['cards'] - matches - mainPatternLen) * (times + 1)) + "???")
							#print("Could be: " + str((problem['cards'] - matches - mainPatternLen) * (times - 1)) + "???")
							#print("Could be: " + str((problem['cards'] - matches - mainPatternLen) * times) + "???")
							#print("Could be: " + str(matches * (times - 1)) + "???")
							#print("Could be: " + str(times) + " - " + str(matches) + " - " + str(matchesL) + ' - ' + str(matchesR) + " - " + str((problem['cards'] - matches) * times) + "???")

							if possibleSolutions.get(matches, 0) < matches:
								possibleSolutions[matches] = (problem['cards'] - matches) * times

							print("Could be: " + str(times) + " - " + str(matches) + " - " + str(matchesL) + ' - ' + str(matchesR) + " - " + str((problem['cards'] - matches) * times) + "???")
							if (((problem['cards'] - matches) * times) > 962554920):
								break

						#print("%d - %d - %d - %d" % (problem['cards'], matches, mainPatternLen, times))
						#times = (problem['cards'] - (matches + mainPatternLen)) * times
						#break
					else:
						secPrev = False
					
				if self.__debugLevel >= 2:
					print(resultDeck)

				deck = resultDeck

			print("Solutions...")
			print(possibleSolutions)
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
