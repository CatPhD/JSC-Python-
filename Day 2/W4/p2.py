weight = float(input("Enter your weight(kg): "))
height = float(input("Enter your weight(cm): "))
height = height/100
BMI = weight/height**2
if BMI < 18.5:
    Level = "Underweight"
elif BMI <= 25:
    Level = "Normal"
else:
    Level = "Overweight"

print('Your BMI value: {:.2f}'.format(BMI))
print(Level)
