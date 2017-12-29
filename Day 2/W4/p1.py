x = float(input("X: "))
y = float(input("Y: "))

if y > 0:
    if x > 0:
        Q = 1
    else:
        Q = 2
else:
    if x > 0:
        Q = 4
    else:
        Q = 3
        
print("Quadrant", Q)
