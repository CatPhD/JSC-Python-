Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> name = input('What is your name?')
What is your name?LSW
>>> name
'LSW'
>>> age = input(name + ', what is your age?')
LSW, what is your age?24
>>> age
'24'
>>> print(name, 'is', age)
LSW is 24
>>> print('Next year, ', name, 'will be', int(age)+1)
Next year,  LSW will be 25
>>> int(10.9)
10
>>> int('10')
10
>>> int('10.9')
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    int('10.9')
ValueError: invalid literal for int() with base 10: '10.9'
>>> float('10.9')
10.9
>>> float(10.9)
10.9
>>> ord('A')
65
>>> ord('Z')-ord('A')
25
>>> ord('A') > ord('a')
False
>>> chr(65)
'A'
>>> chr(ord('A'))
'A'
>>> chr(108)+chr(111)+chr(118)+chr(101)
'love'
>>> format(15, 'X')
'F'
>>> format(15, '2X')
' F'
>>> format(15, '02X')
'0F'
>>> format(65, 'b')
'1000001'
>>> format(65, '08b')
'01000001'
>>> weight = float(input('Enter weight(kg): '))
Enter weight(kg): 65
>>> height = float(input('Enter height(m): '))
Enter height(m): 1.73
>>> bmi= weight / (height **2)
>>> print('Your BMI: ', format(bmi, '.1f'))
Your BMI:  21.7
>>> 
