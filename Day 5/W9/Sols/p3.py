import re

text = '''1.5 kg all-purpose flour
25 g baking soda
30 g salt
1.2 kg white sugar
10 eggs
25 ml vanilla extract
295 ml buttermilk
'''


pattern = r'\d+\.?\d*'
match = re.findall(pattern, text)
for item in match:
    converted = str(float(item)/2)
    text = text.replace(item, converted)

print(text)