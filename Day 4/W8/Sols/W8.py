x= 'pop'

x.index('o')

##x.index('z')

x.find('z')
##=> -1이 반환됨

##여러개 있으면 가장 먼저 찾은게 반환 됨

x.replace('p', 'm')
## 'mom'이라고 나오나 x하면 pop이 나옴. Data 는 read-only이기 때문에
## data를 바꿀 수는 없고 mom을 반환하기만 함

y=' corn '

##y.strip(s)

## 앞 뒤로 s를 지움

## split도 문자열 자체를 바꾸는 것이 아니라 복사본을 바꾸는 것

## is.alpha()에는 사실 한글도 포함이 됨

## is.lower(), is.upper()도 있음

z = ' corn,rice, potato '

z = z.strip(" ")

w = z.split(",")

a = input("enter values: ").split(",")
## 이렇게 여러개의 data를 받고 나눌수도 있음

b = input("enter: ").upper()

###

## 주민등록번호

def validRRN(rrn):
    dashIndex = rrn.find("-")
    valid = (dashIndex == 6)
    valid = valid and len(rrn) == 14
    valid = valid and rrn[:dashIndex].isdigit()
    valid = valid and rrn[dashIndex+1:].isdigit()
    return True


def getRRNfromUser():
    rrn = input('Enter: ')
    while not validRRN(rrn):
        print('Wrong')
        rrn = input('Enter: ')
    return rrn





def printDateOfBirth(rrn):
    dob = rrn[0:2] + '-' + rrn[2:4] + '-' + rrn[4:6]
    print("Dob:", dob)


def printGender(rrn):
    if rrn[7] == '1':
        print("Gender: Male")
    else:
        print("Gender: Female")



rrn = getRRNfromUser()
printDateOfBirth(rrn)
printGender(rrn)








## 숫자에 대해 XOR 연산을 한다는 것은 비트단위로 0을 False 1을 True로 보고
## 각 자리수별로 계산한 것인듯















