def displayWord(text):
    splitted = text.split(' ')
    i = 0
    while i < len(splitted):
        print(i, splitted[i])
        i += 1
    
    
text = input('Enter text:')
displayWord(text)
