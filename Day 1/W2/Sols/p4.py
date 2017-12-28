FCG = input("Enter the first course grade:")
FCC = input("Enter the first course credit:")
SCG = input("Enter the second course grade:")
SCC = input("Enter the second course credit:")
TCG = input("Enter the third course grade:")
TCC = input("Enter the third course credit:")

FCG = float(FCG)
FCC = int(FCC)
SCG = float(SCG)
SCC = int(SCC)
TCG = float(TCG)
TCC = int(TCC)

GPA = (FCG*FCC+SCG*SCC+TCG*TCC)/(FCC+SCC+TCC)

print('Your GPA is', format(GPA, '.1f'))
