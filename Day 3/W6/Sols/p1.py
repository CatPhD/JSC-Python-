numbers = [4, 2, 5, 7, 7, 10, 1, 7, 2, 8]

def getSum(data):
    i = 0
    total = 0
    while i < len(data):
        total = total + data[i]
        i = i + 1
    return total

print(numbers)
print('Total:', getSum(numbers))
