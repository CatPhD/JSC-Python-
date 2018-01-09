filename1 = 'c:/work/moby-dick.txt'
inputFile = open(filename1)
text = inputFile.read()
inputFile.close()

freq = {}
for letter in text:
    if letter.isalpha() == True:
        letter = letter.lower()
        if letter not in freq:
            freq[letter] = 1
        else:
            freq[letter] += 1


for letter in freq:
    print(letter, format(freq[letter], '7'))
