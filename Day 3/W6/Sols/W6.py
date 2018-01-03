##number[0:2]라고 하면 0번부터 2번 직전까지 뽑겠다는 뜻임
##
##0은 생략 가능 numbers[:2]
##
##뒤쪽 index 생략하면 모두 다 뽑음 numbers[4:]
##
##다른 언어에서는 data type을 섞을 수 없는데 파이썬에서는 됨
##
##추가, 삽입,삭제에서 삭제만 명령어 형태가 다름


## lotto

import random

def generateOneNumber(lottoNumbers):
    number = random.randint(1, 45)
    while number in lottoNumbers:
        number = random.randint(1, 45)
    return number
##중복 되는지 안 되는지 체크하려면 random.randint의 마지막 parameter를
##end로 주고 end값을 6으로 바꿔주는 식으로 체크해봄
##원래 프로그래밍할 때 상수를 주는 것은 별로 안 좋음
##Semantic을 주는 것이 좋음


def generateLottoNumbers():
    lottoNumbers = []
    i = 0
    while i < 6:
        number = generateOneNumber(lottoNumbers)
        lottoNumbers.append(number)
        i = i + 1
    return lottoNumbers
    





lottoNumbers = generateLottoNumbers()
print('Your Number:', lottoNumbers)
