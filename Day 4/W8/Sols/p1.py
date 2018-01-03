def encrypt(text, key):
    length = len(text)
    key = key.lower()
    encrypted = ''
    i = 0
    while i < length:
        e = ord(text[i]) ^ ord(key)
        encrypted += chr(e)
        i += 1
    return encrypted
    

plainText = input('Enter plain text to encode: ')
key = input('Enter a key: ')
encryptText = encrypt(plainText, key)
print('Encrypted text: ', encryptText)

##def encrypt(plainText, key):
##    encryptedText = ''
##    for c in plainText:
##        encryptedText += chr(ord(c)^ord(key))
##    return encryptedText
