#!/usr/bin/env python

""" problem.py: Basic templete to solve the prooblems of the Tuenti Challenge 2 """

import math
import itertools

__author__ = "Alonso Vidales"
__email__ = "alonso.vidales@tras2.es"
__date__ = "2012-04-27"

class Problem:
	"""
	Generic class to solve the problems
	"""

	__debugLevel = 0
	__problems = []

	def __getAngel(self, inOrigin, inTarget):
		""" Returns the angel between the given two points in radians """
		a = abs(inTarget['y'] - inOrigin['y'])
		b = abs(inTarget['x'] - inOrigin['x'])

		sumAng = 0
		if inTarget['y'] < inOrigin['y']:
			sumAng = math.pi / 2

		if inTarget['x'] < inOrigin['x']:
			return (math.atan2(a, b) + sumAng) * -1

		return (math.atan2(a, b) + sumAng)

	def __calcCorners(self, inCenter, inCorner, inEdges):
		""" Returns an array with all the corners of the regular polygon """
		angelsToMove = math.radians(360 / inEdges)

		a = inCorner['y'] - inCenter['y']
		b = inCorner['x'] - inCenter['x']
		# Calc the radious
		h = math.sqrt((a ** 2) + (b ** 2))
		# The main to calculate the roation of the polygon
		ang = math.atan2(a, b)

		if b < 0:
			ang *= -1

		if self.__debugLevel >= 2:
			print("Triangle: h: %f, ang: %f, a: %f, b: %f" % (h, math.degrees(ang), a, b))

		angles = []

		for edge in range(0, inEdges):
			cornerAng = (angelsToMove * edge) + ang

			newA = math.sin(cornerAng) * h
			newB = math.cos(cornerAng) * h

			angles.append({
				'x': newA + inCenter['x'],
				'y': newB + inCenter['y']})

		return angles

	def __getAbsAngle(self, inAngle):
		""" Returns the absolute angle from the y axe in radians """
		if inAngle < 0:
			return math.radians(360 + math.degrees(inAngle))

		return inAngle

	def __angleInRange(self, inAngle, inRange):
		""" Check if a angle is inside another two angles """
		inRange.sort()
		oneAng = math.degrees(inRange[0])
		twoAng = math.degrees(inRange[1])
		angle = math.degrees(inAngle)

		moveAngles = 0

		moveAngles = 360 - twoAng
		oneAng += moveAngles
		angle = (angle + moveAngles) % 360

		return (
			oneAng < 180 and angle <= oneAng or
			oneAng > 180 and angle >= oneAng)

	def solve(self):
		"""
		Method that reolves te problem and resturns the solutions in an array of strings
		"""

		ret = []

		for problem in self.__problems:
			groups = []

			# Calculate all the angles for all the elements
			ingNum = 0
			for ingredient in problem['ingredients']:
				corners = []
				for pos in ingredient['pos']:
					ingAngs = [self.__calcCorners(pos['center'], pos['vertex'], ingredient['edges'])]
					ingAngs.insert(0, ingNum)
					groups.append(ingAngs)

				ingNum += 1

			if self.__debugLevel >= 1:
				print(groups)
				print("\nStudy all the posibilities...")

			isPossible = False

			possibleGroup = [[]] * len(groups)

			# Distribute the element between the two groups keeping the coherence of type of elements in each group
			for pos in range(0, len(groups) / 2):
				possibleGroup[pos] = groups[pos * 2]
				possibleGroup[pos + (len(groups) / 2)] = groups[(pos * 2) + 1]

			# Check all the possible combinations of elements
			for iters in range(0, len(possibleGroup) / 2):
				aux = possibleGroup[iters]
				
				possibleGroup[iters] = possibleGroup[iters + (len(possibleGroup) / 2)]
				possibleGroup[iters + (len(possibleGroup) / 2)] = aux

				if self.__debugLevel >= 3:
					print("We have a possible group...")
					print(possibleGroup)
					print("\n\n")

				left = self.__getAngel(problem['center'], possibleGroup[0][1][0])
				right = self.__getAngel(problem['center'], possibleGroup[len(possibleGroup) - 1][1][0])
				minAngLeft = left
				maxAngLeft = left
				minAngRight = right
				maxAngRight = right

				for elemPos in range(0, len(possibleGroup) / 2):
					#left group
					for point in possibleGroup[elemPos][1]:
						angle = self.__getAngel(problem['center'], point)
						if angle < minAngLeft:
							minAngLeft = angle

						if angle > maxAngLeft:
							maxAngLeft = angle

					#right group
					for point in possibleGroup[elemPos + (len(possibleGroup) / 2)][1]:
						angle = self.__getAngel(problem['center'], point)
						if angle < minAngRight:
							minAngRight = angle

						if angle > maxAngRight:
							maxAngRight = angle

				# Convert the max angle to absolute angles
				minAngLeft = self.__getAbsAngle(minAngLeft)
				maxAngLeft = self.__getAbsAngle(maxAngLeft)
				sampleAngleLeft = self.__getAngel(problem['center'], possibleGroup[0][1][0])

				minAngRight = self.__getAbsAngle(minAngRight)
				maxAngRight = self.__getAbsAngle(maxAngRight)
				sampleAngleRight = self.__getAngel(problem['center'], possibleGroup[len(possibleGroup) - 1][1][0])

				if self.__debugLevel >= 2:
					print(possibleGroup[:len(possibleGroup) / 2])
					print(possibleGroup[len(possibleGroup) / 2:])

					print("\nExtrem points:")
					print(math.degrees(minAngLeft))
					print(math.degrees(maxAngLeft))
					print(math.degrees(sampleAngleLeft))
					print(math.degrees(minAngRight))
					print(math.degrees(maxAngRight))
					print(math.degrees(sampleAngleRight))

				# Check if between the max angles of the two groups we can create a line who divides both
				if (
					not self.__angleInRange(sampleAngleRight, [minAngLeft, maxAngLeft]) and
					not self.__angleInRange(sampleAngleLeft, [minAngRight, maxAngRight]) and
					#not self.__angleInRange(minAngRight, [minAngLeft, maxAngLeft]) and
					#not self.__angleInRange(maxAngRight, [minAngLeft, maxAngLeft]) and
					not self.__angleInRange(minAngLeft, [minAngRight, maxAngRight]) and
					not self.__angleInRange(maxAngLeft, [minAngRight, maxAngRight])):
					isPossible = True
					break

			ret.append(isPossible)

		return ret

	def __init__(self, inInputLines):
		""" Takes and parse the input lines into the internal structure """

		currLine = 1
	 	for problemPos in range(0, int(inInputLines[0])):
			pizzaInfo = map(float, inInputLines[currLine].split())

			problemInfo = {
				'center': {
					'x': pizzaInfo[0],
					'y': pizzaInfo[1],
				},
				'rad': pizzaInfo[2],
				'ingredients': []}

			currLine += 2
	 		for ingPos in range(0, int(inInputLines[currLine - 1])):
				ingInfo = inInputLines[currLine].split()
				ingredient = {
					'edges': int(ingInfo[1]),
					'pos': []
				}

				currLine += 1
				for inPosPos in range(0, int(ingInfo[2])):
					ingPosInfo = map(float, inInputLines[currLine].split())
					ingredient['pos'].append({
						'center': {
							'x': ingPosInfo[0],
							'y': ingPosInfo[1]
						},
						'vertex': {
							'x': ingPosInfo[2],
							'y': ingPosInfo[3]
						}
					})
					currLine += 1

				problemInfo['ingredients'].append(ingredient)

			self.__problems.append(problemInfo)


		if self.__debugLevel >= 2:
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
for pos in range(0, len(solutions)):
	if solutions[pos]:
		solution = "TRUE"
	else:
		solution = "FALSE"
	print("Case #%d: %s" % (pos + 1, solution))
