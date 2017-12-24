Level = int(input("소득분위 입력(1~10분위):"))
CulSem = int(input("현재 누적학기:"))
Grade = float(input("학기 평점:"))


R = (Level==1 and Grade >= 3.7) or (Level <=3 and CulSem <8 and Grade >=4.0) 
print("장학금 대상자:", R)
