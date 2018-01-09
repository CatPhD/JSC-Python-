i=1

while i <=3:
    ID = input("ID: ")
    PW = input("PW: ")

    if ID == 'yonsei' and PW == 'abc123':
        print("로그인에 성공하였습니다")
        i = 4
        
    elif i == 3:
        print("아이디 혹은 암호가 맞지 않습니다\n")
        print("3번 실패하여 로그인을 종료합니다")
        i = i +1

    else:
        print("아이디 혹은 암호가 맞지 않습니다")
        i = i +1
        
