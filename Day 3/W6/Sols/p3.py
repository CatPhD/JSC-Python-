dataList = [4, 3, -8, 1, 0, -2, 10, 5, 7, -1]
negativeDataList = []
i = 0

while i < len(dataList):
    if dataList[i] < 0:
        negativeDataList.append(dataList[i])
    i = i + 1

print('Negative data is', negativeDataList)

