Clm = int(input("이미지 가로 픽셀: "))
Row = int(input("이미지 세로 픽셀: "))
RGB = int(input("이미지 색상 비트: "))

B =Clm * Row * RGB /8
KB = B/2**10
MB = KB/2**10
Number = 2**24

print("{}X{} 해상도, {}bit(s)의 무압축 이미지 데이터 용량은,".format(Clm, Row, RGB))
print("{:,.0f} B, {:,.1f}KB, {:,.1f}MB 이며,".format(B, KB, MB))
print("표현할 수 있는 색상은 {:,.0f}가지 입니다.".format(Number))
