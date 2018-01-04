scores = [72, 56, 89, 34, 100, 78, 12, 88]
tmp = scores
tmp.sort()

print('Scores: ')
for i in tmp:
    print(i)

total = sum(scores)
average = total / len(scores)

print('Total:', total)
print('Average:', average)
