numberList = []

number = int(input('Enter a number(quit: negative number): '))

while number >= 0 :
    if number in numberList:
        print('Already exists')
    else:
        numberList.append(number)
    print(numberList)
    number = int(input('Enter a number(quit: negative number): '))

    
