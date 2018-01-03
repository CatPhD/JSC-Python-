##x = [2, 1, 3]
##
#### x.sort(x) 안됨. x.sort()라고 해야함
## x = x.sort()따위도 안 됨
## average 도 안 됨

## for x in list 에서
## x는 list에 있는 값을 복사해서 쓰는 것이므로
## x를 변경한다고 list 값이 변경되지는 않음
##
##list = [10, 20, 30, 40, 50]
##
##i = 0
##while i < len(list):
##    print(list[i])
##    i = i +1
##
##for item in list:
##    print(item)

##    def displayList(wishList):
##    print("My wish list")
##    i = 0
##    for item in wishList:
##        i = i + 1
##        print("{:>2}. {}".format(i, item))
##
##    def addWish(wishList):
##    wish = input("Wish: ")
##    wishList.append(wish)
##
##    def deleteWish(wishList):
##    i = int(input("Index: ")) -1
##    del wishList[i]
##
##    def insertWish(wishList):
##    wish = input("Wish: ")
##    i = int(input("Index: ")) -1
##    wishList.insert(i, wish)
##
##    def getUserInput():
##    choice = input('Enter(ADIQ): ')
##    return choice
##
##
##
##
##    wishList = []
##    terminated = False
##    while not terminated:
##    displayList(wishList)
##    choice = getUserInput()
##    if choice == 'A':
##        addWish(wishList)
##    elif choice == 'D':
##        deleteWish(wishList)
##    elif choice == 'I':
##        insertWish(wishList)
##    elif choice == 'Q':
##        terminated = True


## 7.3
##
##score = [[90, 95], [87, 91]]
##
##row = 0
##col = 0
##while row < len(score):
##    while col < len(score[row]):
##        print(score[row][col], end = ' ')
##        col = col + 1
##    print('')
##    row = row + 1
##    col = 0
##
##
##
##score = [[90, 95, 100],
##         [87, 91, 200],
##         [20, 30, 40],
##         [90, 80, 93]]
##
##total = 0
##avg = 0
##for row in score:
##    for col in row:
##        total = total + col
##        avg = total / len(row)
##    total = 0
##    print(avg)
##

##


## 실습 review

def getSecond(numbers):
    biggest = max(numbers)
    second = min(numbers)
    for n in numbers:
        if n > second and n < biggest:
            second n
    return second

##

year = int(input('출생연도: '))

index = (year - 1900)%12

##












        

