import string

letters = string.ascii_letters + " "
invLetters = {}
numLetters = len(letters)

for i in range(numLetters):
    invLetters[letters[i]] = i


def encryptVigenere(plain, password):
    global letters, invLetters, numLetters
    cipher = ""
    passwordIndex = 0
    for i in range(len(plain)):
        shift = invLetters[password[passwordIndex]]
        index = (invLetters[plain[i]]+shift) % numLetters
        cipher = cipher + letters[index]
        passwordIndex = (passwordIndex+1) % len(password)
    return cipher


def decryptVigenere(cipher, password):
    global letters, invLetters, numLetters
    plain = ""
    passwordIndex = 0
    for i in range(len(cipher)):
        shift = invLetters[password[passwordIndex]]
        index = (invLetters[cipher[i]]-shift) % numLetters
        plain = plain + letters[index]
        passwordIndex = (passwordIndex+1) % len(password)
    return plain


def encryptRect(plain, cols):
    cipher = ""
    numLines = len(plain) // cols
    if(numLines * cols) < len(plain):
        numLines += 1

    block = [[" " for i in range(cols)] for j in range(numLines)]

    i = 0
    j = 0

    for k in range(len(plain)):
        block[i][j] = plain[k]
        j = (j+1) % cols
        if j == 0:
            i = i+1

    for j in range(cols):
        for i in range(numLines):
            cipher = cipher+block[i][j]

    return cipher


def decryptRect(cipher, column):
    plain = ''
    numLines = len(cipher) // column
    if(numLines * column) < len(cipher):
        numLines += 1
    block = [[" " for i in range(numLines)] for j in range(column)]

    i = 0
    j = 0

    for k in cipher:
        block[j][i] = k
        i = (i+1) % numLines
        if i == 0:
            j += 1

    for i in range(numLines):
        for j in range(column):
            plain += block[j][i]

    return plain


plain = input("Masukkan teks: ")
password = input("Password: ")
cols = input("Kolom: ")

cols = int(cols)

print()
cipherRect = encryptRect(plain, cols)
print("Hasil enkripsi Rectangle: ", cipherRect)
cipherVigenere = encryptVigenere(cipherRect, password)
print("Hasil enkripsi Vigenere: ", cipherVigenere)

print()
plainVigenere = decryptVigenere(cipherVigenere, password)
print("Hasil dekripsi Vigenere: ", plainVigenere)
plainRect = decryptRect(plainVigenere, cols)
print("Hasil dekripsi Rectangle: ", plainRect)
