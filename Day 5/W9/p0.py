import re
pattern = r'apple'
string = 'pineapple, cherry, apple'
match = re.findall(pattern, string)
print(match)
