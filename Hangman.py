import random

def get_random_word():
    fileObject = open('listOfWords.txt', 'r')
    words = fileObject.read().split()
    randomNumber = random.randint(0, len(words))
    chosenWord = words[randomNumber]
    return chosenWord

def get_blanked_word(blankedWord):
    global score
    score += 1
    guess = get_guess()
    i = 0
    while i < len(chosenWord):
        if guess == chosenWord[i]:
            blankedWord[i] = guess
            score +- 1
        i += 1
    return blankedWord

def get_guess():
    guess = ''

    while (len(guess) != 1 or guess == '_' or guess.isalpha() == False or guess not in guessedLetters):
        guess = raw_input().upper()

    guessedLetters.remove(guess)
    return guess

def game_not_over(blankedWord):
    for x in blankedWord:
        if x == '_':
            return True
    return False

chosenWord = get_random_word()
blankedWord = ['_' for i in range(len(chosenWord))]
guessedLetters = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'.split()
score = 0

print ' '.join(blankedWord) + '     ||||     ' + '  '.join(guessedLetters)

while game_not_over(blankedWord):
    print ' '.join(get_blanked_word(blankedWord))+ '     ||||     ' + '  '.join(guessedLetters)
print score
