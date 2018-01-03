def checkSerial(serial):
    index = serial.find('-')
    valid = (len(serial) == 9)
    valid = valid and (index == 4)
    valid = valid and serial[0:2].isalpha()
    valid = valid and serial[2:index].isdigit()
    valid = valid and serial[index+1:9].isdigit()
    return valid


serial = 'AB12-1234'
print(serial)

if checkSerial(serial):
    print('This is a valid format!')
else:
    print('This is an invalid format!')
