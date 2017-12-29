grade = 80
if grade >= 90:
    print("참 잘했어요")
else:
    print("NON PASS")
print("점수는", grade)
## :을 까먹지 말것

####

age = int(input("나이: "))

if age <= 2:
    print("Infant")
elif age <=12:
## 여기서 3<age 할 필요는 없음
    print("Child")
elif age < 20:
    print("Teenager")
else:
    print("Adult")



####
note = input("Enter a note: ")
while note not in ("ABCDEF"):
    print('Wrong')
    note = input("Enter a note: ")
print(note)


####
balance = 0
terminated = False

while not terminated:
    choice = input("(D) (W) (B) (T): ")
    if choice == 'D':
        amount = int(input("Amount: "))
        balance = balance + amount
    elif choice == 'W':
        amount = int(input("Amount: "))
        if amount > balance:
            print("Not enough balance")
        else: 
            balance = balance - amount
    elif choice == 'B':
        print(balance)
        
    elif choice == 'T':
        terminated = True

    else:
        print("Wrong input")
