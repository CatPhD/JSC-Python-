passwordList = ['abc123', '2017', '!@#$']
doorOpen = False
attemptCount = 0

while (not doorOpen) and (attemptCount < 3):
    userTry = input('Enter a password: ')
    attemptCount = attemptCount + 1
    if userTry in passwordList:
        print('Door opened!')
        doorOpen = True
    else:
        print('Wrong password')

if attemptCount == 3:
    print('Alert! Alert! Intruder!')

## if attemptCount == 3 and doorOpen = False 이어야함.
