print("Welcome")

year = int(input("Enter: "))

isLeapYear = (year % 4 == 0) and not( year % 100 == 0) \
             or (year % 400 ==0)

print("{} is a leap year: {}".format(year, isLeapYear))
