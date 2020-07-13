import string
import random
import math

def create_list_of_numbers():
    numbers = [0, 0]
    while (numbers[0] + numbers[1]) != 6 and numbers[1] <= 4 and numbers[1] >= 0 and numbers[0] >= 0:
        numbers[0] = int(raw_input("How many small numbers? "))
        numbers[1] = int(raw_input("How many big numbers? "))
    return add_to_list(numbers)

def add_to_list(numbers):
    listOfNumbers = list()
    smallNumbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    bigNumbers = (25, 50, 75, 100)

    j = 0
    for x in numbers:
        i = 0
        while i < x and j == 0:
            listOfNumbers.append(random.choice(smallNumbers))
            i += 1
        while i < x and j == 1:
            while number not in listOfNumbers:
                number = random.choice(bigNumbers)
            listOfNumbers.append(number)
            i += 1
        j += 1

    return listOfNumbers


print create_list_of_numbers()














'''

import string
import random
import math

class countdown:

    def __init__(self):
        self.noOfSmall = 0
        self.noOfBig = 0
        self.bigNumbers = (25, 50, 75, 100)
        self.smallNumbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        self.numbersList = list()

    def get_no_of_numbers(self):
        noOfSmall = self.noOfSmall
        noOfBig = self.noOfBig
        numbersList = self.numbersList
        while (int(noOfSmall) + int(noOfBig)) != 6 and noOfBig <= 4 and noOfBig >= 0 and noOfSmall >= 0:
            noOfSmall = raw_input("How many small numbers? ")
            noOfBig = raw_input("How many big numbers? ")
        self.create_list(noOfSmall, self.smallNumbers)
        return self.create_list(noOfBig, self.bigNumbers)

    def create_list(self, amount, options):
        numbersList = self.numbersList
        number = random.choice(options)
        i = 0
        while i < int(amount):
            while number in numbersList:
                number = random.choice(options)
            numbersList.append(number)
            i += 1
        return numbersList

if __name__ == '__main__':
    Countdown = countdown()
    print Countdown.get_no_of_numbers()



'''

'''
def get_number_of_smallandbig():
    noOfSmall = 0
    noOfBig = 0
    while (int(noOfSmall) + int(noOfBig)) != 6 and noOfBig <= 4 and noOfBig >= 0 and noOfSmall >= 0:
        noOfSmall = raw_input("How many small numbers? ")
        noOfBig = raw_input("How many big numbers? ")
    return noOfSmall, noOfBig

def add_to_list(noOfSmall, noOfBig):


noOfSmall, noOfBig = get_number_of_smallandbig()
numbers = list()
number = random.choice(smallNumbers)

i = 0
while i < int(noOfSmall):
    while number in numbers:
        number = random.choice(smallNumbers)
    numbers.append(number)
    i += 1

i = 0
while i < int(noOfBig):
    while number in numbers:
        number = random.choice(bigNumbers)
    numbers.append(number)
    i += 1


print "You have chosen", noOfSmall, "small number(s) and", noOfBig, "big number(s).\nYour numbers are: ",
for x in numbers:
    print x, "",

targetNumber = random.randint(100, 999)
print targetNumber







'''
'''
countdownLetters = tuple()
letters = string.ascii_uppercase

countdownLetters = random.choice(letters), random.choice(letters), random.choice(letters), random.choice(letters), \
random.choice(letters), random.choice(letters), random.choice(letters), random.choice(letters), random.choice(letters)


print countdownLetters

fileO = open('listOfWords2.txt', 'r')
words = fileO.read().split()

for x in words:
    mini = 0
    max = len(x)
    for y in x:
        if y in countdownLetters:
            mini += 1
        if mini == max:
            print x
'''