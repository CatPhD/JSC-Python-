filename = 'c:/work/output.txt'
outputFile = open(filename, 'w')
Userinput = input("Enter: ")
content=''
while Userinput != "Q":
    content = content + Userinput + '\n'
    Userinput = input("Enter: ")    
outputFile.write(content)
outputFile.close()
