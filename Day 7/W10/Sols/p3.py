filename1 = 'c:/work/fruits.txt'
inputFile = open(filename1)
fruits=[]
for line in inputFile:
    fruits.append(line)
inputFile.close()

print(fruits)

fruits.sort()
content = ''
for line in fruits:
    content = content + line

filename2 = 'c:/work/sorted.txt'
outputFile = open(filename2, 'w')
outputFile.write(content)
outputFile.close()

print(content)
