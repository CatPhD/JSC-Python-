import random

def inputUserGuess():
    userGuess = int(input('Take a guess: '))
    while userGuess < 0 or userGuess > 100:
        print('Wrong Guess')
        userGuess = int(input('Take a guess: '))
    return userGuess

computerGuess = random.randint(0, 100)
userGuess = inputUserGuess()

while computerGuess != userGuess:
    if computerGuess > userGuess:
            print('Too Low')
    else:
            print('Too high')
    userGuess = inputUserGuess()

print('You got it')
