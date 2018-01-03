def normalize(table, avg):
    i = 0
    j = 0
    while i < len(table):
        while j < len(table[i]):
            table[i][j] = table[i][j] - avg
            j = j + 1
        i = i + 1
        j = 0


def displayTable(table):
    print("Data:")
    for row in table:
        for col in row:
            print("{:10.2f} ".format(col), end='')
        print()

def getAverage(table):
    total = 0
    count = 0
    for row in table:
        for col in row:
            total = total + col
            count = count + 1
    avg = total / count
    return avg


data = [[75, 22, 90, 54], [32, 97, 60, 87]]

displayTable(data)
avg = getAverage(data)
print("Average: {:.2f}\n".format(avg))

normalize(data, avg)

displayTable(data)
normalized_avg = getAverage(data)


## 교수님
##
##def getAverage(table):
##    total = 0
##    count = 0
##    for row in table:
##        total = total + sum(row)
##        count = count + len(row)
##
##    return total / count

##
##def normalize(table, avg):
##    for r in range(0, len(table)):
##        for c in range(0, len(table[r])):
##            table[r][c] -= avg

## 이 방식이 나은 것 같다. 굳이 j인덱스 초기화 안 해도 됨.
