P = input("Enter P: ") == 'T'
Q = input("Enter Q: ") == 'T'

R = (not (P and Q) and (P or Q))

print("P XOR Q:", R) 
