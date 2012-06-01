#!/usr/bin/env python

""" problem.py: Basic templete to solve the prooblems of the Tuenti Challenge 2 """

from time import *

__author__ = "Alonso Vidales"
__email__ = "alonso.vidales@tras2.es"
__date__ = "2012-04-27"

class Problem:
	"""
	Generic class to solve the problems
	"""

	__debug = False
	# The clock leds, True the led is on and False off
	#   1
	#  ---
	# 0| |2
	#  |6|
	# 5| |3
	#  ---
	#   4
	__numbersLedsMap = {
		-1: { # Number switched off
			0: False,
			1: False,
			2: False,
			3: False,
			4: False,
			5: False,
			6: False
		},
		0: {
			0: True,
			1: True,
			2: True,
			3: True,
			4: True,
			5: True,
			6: False
		},
		1: {
			0: False,
			1: False,
			2: True,
			3: True,
			4: False,
			5: False,
			6: False
		},
		2: {
			0: False,
			1: True,
			2: True,
			3: False,
			4: True,
			5: True,
			6: True
		},
		3: {
			0: False,
			1: True,
			2: True,
			3: True,
			4: True,
			5: False,
			6: True
		},
		4: {
			0: True,
			1: False,
			2: True,
			3: True,
			4: False,
			5: False,
			6: True
		},
		5: {
			0: True,
			1: True,
			2: False,
			3: True,
			4: True,
			5: False,
			6: True
		},
		6: {
			0: True,
			1: True,
			2: False,
			3: True,
			4: True,
			5: True,
			6: True
		},
		7: {
			0: False,
			1: True,
			2: True,
			3: True,
			4: False,
			5: False,
			6: False
		},
		8: {
			0: True,
			1: True,
			2: True,
			3: True,
			4: True,
			5: True,
			6: True
		},
		9: {
			0: True,
			1: True,
			2: True,
			3: True,
			4: False,
			5: True,
			6: True
		}}

	# The difference in number of leds between the two clocks for a single day
	__diffInLedsForAday = 2255477
	__secondsInAday = 24 * 3600
	__problems = []

	def __ledsToSwitchOn(self, inFrom, inTo):
		ledsFrom = self.__numbersLedsMap[inFrom]
		ledsTo = self.__numbersLedsMap[inTo]

		leds = 0

		for ledPos, status in ledsFrom.items():
			if status != ledsTo[ledPos] and ledsTo[ledPos]:
				leds += 1
		
		return leds

	def __getLedsFromZero(self, inTo):
		totalLeds = 0

		for pos in range(0, len(inTo)):
			totalLeds += self.__ledsToSwitchOn(-1, int(inTo[pos]))

		return totalLeds

	def solve(self):
		"""
		Method that reolves te problem and resturns the solutions in an array of strings
		"""

		ret = []

		for problem in self.__problems:
			totalLeds = 0
			fromTime = int(mktime(strptime(problem['from'],"%Y-%m-%d %H:%M:%S")))
			toTime = int(mktime(strptime(problem['to'],"%Y-%m-%d %H:%M:%S")))

			if self.__debug:
				print("FROM: %d TO: %d" % (fromTime, toTime))

			# Clock bootstrap
			lastTimeStr = strftime("%H%M%S", localtime(fromTime))

			# The leds for a day was precalculated, do the calculation directly
			days = (toTime - fromTime) / self.__secondsInAday
			totalLeds = days * self.__diffInLedsForAday
			fromTime += days * self.__secondsInAday

			if self.__debug:
				print('RANGES:')
				print((toTime - fromTime) / self.__secondsInAday)
				print(strftime("%Y-%m-%d %H:%M:%S", localtime(fromTime)))
				print(strftime("%Y-%m-%d %H:%M:%S", localtime(toTime)))
			
			# Calculate the reaining seconds, second a second...
			for time in range(fromTime + 1, toTime + 1):
				currentStr = strftime("%H%M%S", localtime(time))

				ledsToModify = 0
				for pos in range(0, len(lastTimeStr)):
					ledsToModify += self.__ledsToSwitchOn(int(lastTimeStr[pos]), int(currentStr[pos]))

				totalLeds += (self.__getLedsFromZero(currentStr) - ledsToModify)

				if self.__debug:
					print(str(currentStr) + ' - ' + str(totalLeds))

				lastTimeStr = currentStr

			ret.append(totalLeds)

		return ret

	def __init__(self, inInputLines):
		""" Takes and parse the input lines into the internal structure """
		for line in inInputLines:
			datTimes = line.split(' - ')
			self.__problems.append({
				'from': datTimes[0],
				'to': datTimes[1]
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
for solution in solutions:
	print(solution)	
