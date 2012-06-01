#!/usr/bin/env python

""" problem.py: Basic templete to solve the prooblems of the Tuenti Challenge 2 """

__author__ = "Alonso Vidales"
__email__ = "alonso.vidales@tras2.es"
__date__ = "2012-04-27"

class Problem:
	"""
	Generic class to solve the problems
	"""

	__problems = []

	def solve(self):
		"""
		Calculate the max number of cake pieces for the given cuts
		"""

		ret = []

		# Ok, let's cut the cake, for more info:
		# http://books.google.es/books?id=Z3TkuH5MVuAC&lpg=PA261&ots=L25GlKFxrX&dq=plane%20cuts%20in%20three%20space&hl=es&pg=PA262#v=onepage&q=plane%20cuts%20in%20three%20space&f=false
		for problem in self.__problems:
			cuts = 1
			for count in range(0, problem + 1):
				cuts += count

			ret.append(cuts)

			#ret.append(((1 + problem) ** (problem + 1)) / 2)

		return ret

	def __init__(self, inInputLines):
		""" Takes and parse the input lines into the internal structure """
		for line in inInputLines[1:]:
			self.__problems.append(int(line))

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
for pos in range(0, len(solutions)):
	print("Case #%d: %d" % (pos + 1, solutions[pos]))
