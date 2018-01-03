oldData = [4, 3, 1, 0, 10, 5, 7]
newData = [-3, 4, 5, 6, 7, 9, 8, 3, 12]
duplicatedData = []

print(oldData)
print(newData)

i = 0
while i < len(oldData):
    if oldData[i] in newData:
        duplicatedData.append(oldData[i])
    i = i + 1

print(duplicatedData)
