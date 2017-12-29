## A = 0
## while A < 25:
##    if (not A <= 10) and (not A >20):
##        print("A=", A)
##    A = A +1
## 10 < A <= 20 같은 표현은 파이썬에서만 통하고
## CL이나 logic의 관점에서는 별로 좋지 않음


##letter = 'A'
##while letter <= 'z':
##    if (letter in "AEIOU") or (letter in "aeiou"):
##        print(letter, end='')
##    letter = chr(ord(letter)+1)

##


n = int(input('Enter an integer: '))

if n % 2 == 0:
    print(n, 'is an even integer')
else:
    print(n, 'is an odd integer')
##

grade = 95

if grade >= 90:
    print('Grade: A')
elif grade >= 80:
    print('Grade: B')
elif grade >= 70:
    print('Grade: C')
elif grade >= 60:
    print('Grade: D')
else:
    print('Grade: F')
##


total = 0
i = 1

while i <= 100:
    if i % 2 == 0:
        total = total + i
    i = i + 1
        
print(total)
