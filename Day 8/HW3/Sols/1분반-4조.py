import random

def randomFruits():
    filename = 'c:/work/fruits.txt'
    inputFile = open(filename)
    fruits = inputFile.read()
    fruitsList = fruits.split('\n')
    fruit = fruitsList[random.randint(0, len(fruitsList)-1)]
    fruit = fruit.lower()
    inputFile.close()
    return fruit 

def hideWord(word):
    index = 0
    hiddenWord = ''
    selectedAlpha = word[random.randint(0, len(word)-1)]
    while index < len(word):
        if word[index] == selectedAlpha:
            hiddenWord = hiddenWord + selectedAlpha
        else:
            hiddenWord = hiddenWord + '_'
        index = index + 1
    return hiddenWord

def openWord(word, hiddenWord, inputAlpha):
    index = 0
    while index < len(word):
        if word[index] == inputAlpha:
            hiddenWord = hiddenWord[0:index] + inputAlpha + hiddenWord[index + 1 : len(word)]
        index = index + 1
    return hiddenWord

def userInput(history):
    inputAlpha = input("Enter a guess: ")
    inputAlpha = inputAlpha.lower()
    while True:
        if (inputAlpha.isalpha() == True) and (len(inputAlpha) ==1) and (inputAlpha not in history):
            return inputAlpha
        else:
            print("Incorrect input")
            inputAlpha = input("Enter a guess: ")


hangmanPics = ['''
            +---+
                |
                |
                |
                |
                |
        -----------''',''''
            +---+
            |   |
                |
                |
                |
                |
        -----------''','''
            +---+
            |   |
            O   |
                |
                |
                |
        -----------''','''
            +---+
            |   |
            O   |
            |   |
                |
                |
        -----------''','''
            +---+
            |   |
            O   |
           /|   |
                |
                |
        -----------''','''
            +---+
            |   |
            O   |
           /|\  |
                |
                |
        -----------''','''
            +---+
            |   |
            O   |
           /|\  |
           /    |
                |
        -----------''','''
            +---+
            |   |
            O   |
           /|\  |
           / \  |
                |
        -----------''']

def printHangman(missCount, hiddenWord, history):
    print(hangmanPics[missCount])
    print(hiddenWord)
    print(history)


def runGame():
    terminated = False
    history =''
    missCount = 0
    fruit = randomFruits()
    hiddenWord = hideWord(fruit)
    while not terminated:
        printHangman(missCount, hiddenWord, history)
        inputAlpha = userInput(history)
        history = history + inputAlpha
        if inputAlpha in fruit:
            hiddenWord = openWord(fruit, hiddenWord, inputAlpha)
        else:
            missCount = missCount + 1
        if hiddenWord == fruit or missCount == 7:
            terminated = True

    printHangman(missCount, hiddenWord, history)            
    if hiddenWord == fruit:
        print('Congratulation')
        print('You saved the hangman!')
    else:
        print('Hangman died...T_T')
        print('The answer is', fruit)
    
    
runGame()
