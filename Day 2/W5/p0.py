Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
============ RESTART: C:\Users\sang8\Desktop\17-2\Python\W5\p0.py ============
Current temp: 107
Current temp: 120
Current temp: 133
Current temp: 146
Current temp: 159
159
>>> import math
>>> math.sqrt(81)
9.0
>>> math.ceil(8.1)
9
>>> math.floor(8.9)
8
>>> math.round(8.5)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    math.round(8.5)
AttributeError: module 'math' has no attribute 'round'
>>> round(8.5)
8
>>> math.pi
3.141592653589793
>>> import random
>>> random.randint(0, 3)
2
>>> random.randint(0, 3)
2
>>> random.randint(0, 3)
3
>>> random.randint(0, 3)
2
>>> random.randint(0, 3)
0
>>> random.randint(0, 3)
1
>>> import datetime
>>> datetime.date.today().year
2017
>>> datetime.date.today().month
10
>>> datetime.date.today().day
11
>>> import winsound
>>> 
============ RESTART: C:\Users\sang8\Desktop\17-2\Python\W5\p0.py ============
Current temp: 107
Current temp: 120
Current temp: 133
Current temp: 146
Current temp: 159
159
Distance: 10.63014581273465
>>> winsound.PlaySound('SystemExit', winsound.SND_ALIAS)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    winsound.PlaySound('SystemExit', winsound.SND_ALIAS)
NameError: name 'winsound' is not defined
>>> winsound.PlaySound('SystemExit', winsound.SND_ALIAS)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    winsound.PlaySound('SystemExit', winsound.SND_ALIAS)
NameError: name 'winsound' is not defined
>>> import winsound
>>> winsound.PlaySound('SystemExit', winsound.SND_ALIAS)

>>> 
============ RESTART: C:\Users\sang8\Desktop\17-2\Python\W5\p0.py ============
Current temp: 107
Current temp: 120
Current temp: 133
Current temp: 146
Current temp: 159
159
Distance: 10.63014581273465
>>> 
