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
			litters = 0
			knowLists = {}

			if (self.__debug):
				print('New problem...')
				print(problem)

			race = 0
			while race < problem['races']:
				usedKarts = 0
				groupsAdded = 0

				if (self.__debug):
					print('New race : ' + str(race))

				# Add the max number of kart in the group to this race
				while ((usedKarts + problem['goups'][0]) <= problem['karts']) and (groupsAdded < len(problem['goups'])):
					if (self.__debug):
						print('Adding group: ' + str(problem['goups'][0]))

					usedKarts += problem['goups'][0]
					problem['goups'].insert(len(problem['goups']), problem['goups'].pop(0))
					groupsAdded += 1

				# After the race, the number of litters will be the number of used karts
				litters += usedKarts
				race += 1

				# We are using a dictionary as a cache system in order to know if we are in a loop,
				# and in this case, we can calculate how many loops we have til the end, how many litter by loop
				# and only with a simple multiplication, we can advance into the calculation
				hashGroup = ','.join(map(str, problem['goups']))
				if not knowLists.get(hashGroup, False):
					knowLists[hashGroup] = {
						'usedLitters': litters,
						'races': race}
				else:
					littersByLoop = litters - knowLists[hashGroup]['usedLitters']
					raceByLoop = race - knowLists[hashGroup]['races']

					racesToFinish = problem['races'] - race

					race += racesToFinish - (racesToFinish % raceByLoop)
					litters += (racesToFinish / raceByLoop) * littersByLoop

					if (self.__debug):
						print('ISSET ' + str(littersByLoop) + ' - ' + str(raceByLoop) + ' - ' + str(racesToFinish) + ' - ' + str(racesToFinish / raceByLoop))

				if (self.__debug):
					print('USED Karts: ' + str(usedKarts))
					print(problem['goups'])


			ret.append(litters)

		return ret

	def __init__(self, inInputLines):
		""" Takes and parse the input lines into the internal structure """
		for count in range(0, int(inInputLines[0])):
			raceInfo = inInputLines[(count * 2) + 1].split()
			self.__problems.append({
				'races': int(raceInfo[0]),
				'karts': int(raceInfo[1]),
				'goups': map(int, inInputLines[(count * 2) + 2].split())
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
