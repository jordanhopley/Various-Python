import random

# Find the probability that the four sided dice have a higher total

# fourSided = [0]*9  rolled nine times
# sixSided = [0]*6   rolled six times

print 'Four sided combinations:', 4**9
print 'Six sided combinations:  ', 6**6

fileObjectFour = open('fourSidedCombinations.txt', 'r')
fileObjectSix = open('sixSidedCombinations.txt', 'r')

fourSidedCombinations = fileObjectFour.read()
sixSidedCombinations = fileObjectSix.read()

fourSidedList = fourSidedCombinations.split('\n')
sixSidedList = sixSidedCombinations.split('\n')

possibleTotals = [i for i in range(6,37)]
actualTotals = []

counter = dict()

for combination in fourSidedList:
    total = 0
    combination = combination.split(', ')
    for die in combination:
        total += int(die)
    actualTotals.append(total)

for x in possibleTotals:
    counter.update({x:actualTotals.count(x)})

print "Four sided"
for x in counter:
    print x, "  ", float(counter[x])/4**9

############################################################
print

possibleTotals = [i for i in range(6,37)]
actualTotals = []

counter = dict()

for combination in sixSidedList:
    total = 0
    combination = combination.split(', ')
    for die in combination:
        total += int(die)
    actualTotals.append(total)

for x in possibleTotals:
    counter.update({x:actualTotals.count(x)})

print "Six sided"
for x in counter:
    print x, "  ", float(counter[x])/6**6
