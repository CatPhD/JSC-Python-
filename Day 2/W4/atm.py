terminated = False
balance = 0

print("Welcome, how can we help?")

while(terminated == False):
    customer = input("(D) (W) (B) (T): ")
    if customer == 'D':
        deposit = int(input("How much?: "))
        balance = balance + deposit
    elif customer == 'W':
        withdraw = int(input("How much?: "))
        if withdraw <= balance:
            balance = balance - withdraw
        else:
            print("Not enough")
    elif customer == 'B':
        print('Balance: {}'.format(balance))
    elif customer == 'T':
        terminated = True
    else:
        print('Wrong input')


    
