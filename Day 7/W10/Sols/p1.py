filename = 'c:/work/data.txt'
inputFile = open(filename)
content = []
for line in inputFile:
    content.append(int(line))
inputFile.close()

count = len(content)
total = sum(content)
average = total/count

print("Count: ", count)
print("Total: ", total)
print("Average: ", average)

