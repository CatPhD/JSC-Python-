Height = int(input("Height: "))

i = 1
total = '*'
while i <= Height:
    print('{:^19}'.format(total))
    total = total +'**'
    i = i+1
