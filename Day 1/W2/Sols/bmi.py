weight = float(input('Enter weight(kg): '))
height = float(input('Enter hegith(cm): '))
bmi = weight/((height/100)**2)
print('Your BMI: ', format(bmi, '.1f'))
