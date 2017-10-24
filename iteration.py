# iteration pattern

# [1, 5, 7, 8, 4, 3]

def iterate(list):
	# standard for loop with range
	# for i in range(0, len(list)):
	#	print list[i]

	# for each loop
	for item in list:
		print item

def print_scores(names, scores):
	for i in range(0, len(names)):
		#print names[i] , "scored" , scores[i]
		print "%s scored %s on the test" % (names[i], scores[i])

# filter pattern
def congratulations(names, scores):
	for i in range(0, len(names)):
		if (scores[i] == 100):
			print "Congratulations %s!  You got a perfect score!" % names[i]

def grades(names, scores):
	for i in range(0, len(names)):
		if (scores[i] >= 90):
			print "%s got an A" % names[i]

		if (90 > scores[i] >= 80):
			print "%s got a B" % names[i]

		if (80 > scores[i] >= 70):
			print "%s got a C" % names[i]

		if (70 > scores[i] >= 60):
			print "%s got a D" % names[i]

		if (scores[i] < 60):
			print "%s failed" % names[i]
