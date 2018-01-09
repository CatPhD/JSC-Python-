import re

pattern = r'[A-Za-z]{2}\d{2}-\d{4}'
string = input('Enter a serial: ')
match = re.findall(pattern, string)
if len(match) == 1:
    print('{} is a valid number!'.format(string))
else:
    print('Incorrect!')
