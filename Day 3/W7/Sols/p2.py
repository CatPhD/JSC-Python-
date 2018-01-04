def second(lst):
    sec = min(lst)
    for i in lst:
        if sec < i < max(lst):
            sec = i
    return sec

numbers = [4, -1, 5, 8, 9, 3, 4]

print(numbers)
print('Second largest number:', second(numbers))
