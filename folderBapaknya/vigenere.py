letters = "abcdefghijklmnopqrstuvwxyz "
invLetters = {}

numLetters = len(letters)

for i in range(numLetters):
    invLetters[letters[i]] = i

plain = input("Enter plain text: ")
password = input("Password: ")

def encrypt(plain,password):
    global letters, invLetters, numLetters
    cipher = ""
    passwordIndex = 0
    for i in range(len(plain)):
        shift = invLetters[password[passwordIndex]]
        index = (invLetters[plain[i]] + shift) % numLetters
        cipher = cipher + letters[index]
        passwordIndex = (passwordIndex + 1) % len(password)
    return cipher

def decrypt(cipher,shift):
    global letters, invLetters, numLetters
    plain = ""
    passwordIndex = 0
    for i in range(len(cipher)):
        shift = invLetters[password[passwordIndex]]
        index = (invLetters[cipher[i]] - shift) % numLetters
        plain = plain + letters[index]
        passwordIndex = (passwordIndex + 1) % len(password)
    return plain


print(encrypt(plain,password))
print(decrypt(encrypt(plain,password),password))
