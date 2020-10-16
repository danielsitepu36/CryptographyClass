letters = "abcdefghijklmnopqrstuvwxyz "
invLetters = {}

numLetters = len(letters)

for i in range(numLetters):
    invLetters[letters[i]] = i

plain = input("Enter plain text: ")
shift = input("Shift: ")

def encrypt(plain,shift):
    global letters, invLetters, numLetters
    cipher = ""
    for i in range(len(plain)):
        index = (invLetters[plain[i]] + int(shift)) % numLetters
        cipher = cipher + letters[index]
    return cipher

def decrypt(cipher,shift):
    global letters, invLetters, numLetters
    plain = ""
    for i in range(len(cipher)):
        index = (invLetters[cipher[i]] - int(shift)) % numLetters
        plain = plain + letters[index]
    return plain


print(encrypt(plain,shift))
print(decrypt(encrypt(plain,shift),shift))
