a = float(input('Enter a: '))
b = float(input('Enter b: '))
c = float(input('Enter c: '))

R =((a+b>c) and (b+c>a) and (c+a>b))

print('Is this a triangle?:', R)
