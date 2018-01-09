import re

pattern = r'01\d-\d{3,4}-\d{4}'
string = input('Enter a phone number: ')
match = re.findall(pattern, string)
if len(match) == 1:
    print('Correct!')
else:
    print('Incorrect!')
