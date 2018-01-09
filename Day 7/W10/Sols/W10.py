##filename = 'c:/work/newfile.txt'
##outputfile = open(filename, 'w')
##outputfile.write('Hello world')
##
##outputfile.close()

d = {'USD':1208.00, 'JPY':1033.54, 'EUR':1269.79}
print(d['JPY'])
d['CNY'] =173.18
for key in d.keys():
    print(key, d[key])
print(d.keys())
