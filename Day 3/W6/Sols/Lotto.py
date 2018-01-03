import random

def generateRandom(lst):
    number = random.randint(1, 45)
    while number in lst:
        number = random.randint(1, 45)
    return number


def lotto():
    numberList = []
    i = 0
    while i < 6:
        number = generateRandom(numberList)
        numberList.append(number)
        i += 1
    numberList.sort()
    print(numberList)

lotto()
