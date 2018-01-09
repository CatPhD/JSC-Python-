def displayWelcome():
    print("*********************************************")
    print("* 단위 변환 프로그램에 오신 것을 환영합니다 *")
    print("*********************************************")

def displayBye():
    print("*********************************************")
    print("*              안녕히 가세요                *")
    print("*********************************************")


def inputMenu():
    wrong = True
    while wrong:
        select = int(input("<<< Select Menu >>> \n(1) Kg => Pound, (2) Km => Mile (3) 종료: "))
        if select in (1, 2, 3):
            wrong = False
            return select
        else:
            print("올바른 메뉴를 선택하세요")


def inputValue():
    wrong = True
    while wrong:
        value = float(input("변환할 값을 입력하세요: "))
        if value >= 0:
            wrong = False
            return value
        else:
            print("음수는 입력할 수 없습니다.")
        


def displayPound(kg):
    pound = kg*2.204623
    print("{} Kg은 {:.1f} Pound 입니다.".format(kg, pound))


def displayMile(km):
    mile = km*0.62137119
    print("{} Km는 {:.1f} Mile 입니다.".format(km, mile))


terminated = False
displayWelcome()
while terminated == False:
    menu = inputMenu()
    if menu == 1:
        v = inputValue()
        displayPound(v)
    elif menu == 2:
        v = inputValue()
        displayMile(v)
    else:
        terminated = True
        displayBye()
    
    

