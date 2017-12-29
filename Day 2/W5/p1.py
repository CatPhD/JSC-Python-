def max(n1, n2, n3):
    if n1 > n2:
        big = n1
    else:
        big = n2
    if n3 > big:
        big = n3
    return big

print('The biggest:', max(4, -9, 10))

    
    
