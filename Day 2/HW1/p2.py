MotherHeight = float(input("아버지의 키(cm): "))
FatherHeight = float(input("어머니의 키(cm): "))
Height = float(input("나의 키(cm): "))
Sex = int(input("나의 성별(남(+1), 여(-1)): "))
Prediction = float(format((MotherHeight+FatherHeight+13*Sex)/2,".1f"))


print("나의 예상 키:", Prediction, "cm")
print("나의 실제 키:", format(Height,".1f"), "cm")
print("실제 - 예상 키:", format(Height-Prediction, ".1f"), "cm")
