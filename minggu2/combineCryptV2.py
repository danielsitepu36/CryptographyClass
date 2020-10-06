import string

letters = string.ascii_letters + " "


def encryptVigenereV2(plain, password):
    global letters
    cipher = ""
    for i in range(len(plain)):
        shift = letters.index(password[i % len(password)])
        index = (letters.index(plain[i]) + shift) % len(letters)
        cipher += letters[index]
    return cipher


def decryptVigenereV2(cipher, password):
    global letters
    plain = ""
    for i in range(len(cipher)):
        shift = letters.index(password[i % len(password)])
        index = (letters.index(cipher[i]) - shift) % len(letters)
        plain += letters[index]
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

    plain = plain.rstrip()
    return plain


plain = input("Masukkan teks: ")
password = input("Password: ")

while(True):
    cols = input("Kolom: ")
    if(cols == '0'):
        print("Kolom tidak boleh 0, silakan input kolom lagi")
    else:
        break

cols = int(cols)

print()
cipherVigenere = encryptVigenereV2(plain, password)
print("Vigenere encryption: ", cipherVigenere)
cipherRect = encryptRect(cipherVigenere, cols)
print("Rectangle encryption: ", cipherRect)

print()
plainRect = decryptRect(cipherRect, cols)
print("Rectangle decryption: ", plainRect)
plainVigenere = decryptVigenereV2(plainRect, password)
print("Vigenere decryption: ", plainVigenere)
