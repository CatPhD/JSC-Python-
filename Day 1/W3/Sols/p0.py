Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> True and False
False
>>> True or False
True
>>> not(True or False)
False
>>> 10 =<20
SyntaxError: invalid syntax
>>> 10<=20
True
>>> 10<5 and 10>9
False
>>> (10<5) and (10>9)
False
>>> 20+1<2
False
>>> 'apple' > 'Apple'
True
>>> 'a' > 'A'
True
>>> 'pple' > 'pple'
False
>>> 'pplea' > 'ppleA'
True
>>> 'a' > '1'
True
>>> int('apple')
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    int('apple')
ValueError: invalid literal for int() with base 10: 'apple'
>>> ord('apple')
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    ord('apple')
TypeError: ord() expected a character, but string of length 5 found
>>> 10+6/2*3
19.0
>>> 12/4.0
3.0
>>> 12//4.0
3.0
>>> 12//4.1
2.0
>>> 3**2**2
81
>>> 3**2**3
6561
>>> 3**8
6561
>>> 9**3
729
>>> 81%2
1
>>> 'Hello' + 'World'
'HelloWorld'
>>> '3.14'+2
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    '3.14'+2
TypeError: must be str, not int
>>> 10+int(5.5)
15
>>> 10+int('5.5')
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    10+int('5.5')
ValueError: invalid literal for int() with base 10: '5.5'
>>> 2 in (1, 2, 3)
True
>>> 'Mon' in ('Sun', 'Mon', 'Tue', 'Wed')
True
>>> 'a' in ('apple', 'banana')
False
>>> 'a' in 'apple'
True
>>> 'pp' in 'apple'
True
>>> -1 not in (0, 1, 2, 3)
True
>>> 20+1<2
False
>>> 
