def grillSteak(steakTemp, targetTemp, increaseAmount):
    while steakTemp < targetTemp:
        steakTemp = steakTemp + increaseAmount
        print('Current temp:', steakTemp)
    return steakTemp

finalSteakTemp = grillSteak(94, 155, 13)
print(finalSteakTemp)


## mathplotlib 파이썬에서 그래프를 그릴때의 모듈.
## 기본 장착된 것은 아니고 깔아야함.

## import mathplotlib.pyplot as plt 라고 저장하면
## 불러올때 plt로 축약할 수 있음. 




import math
def getDistance(x1, y1, x2, y2):
    distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    return distance

d = getDistance(2, 1, 10, 8)

print("Distance:", d)

## 이런 함수 저장해뒀다가 library 로 만들어 놓으면 나중에 import 해서 쓸 수 있음
