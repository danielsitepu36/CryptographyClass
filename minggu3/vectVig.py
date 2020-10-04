import string

letters = string.ascii_letters + " "


def encryptVigenere(plain, password):
    global letters
    cipher = ""
    for i in range(len(plain)):
        shift = letters.index(password[i % len(password)])
        index = (letters.index(plain[i]) + shift) % len(letters)
        cipher += letters[index]
    return cipher


def decryptVigenere(cipher, password):
    global letters
    plain = ""
    for i in range(len(cipher)):
        shift = letters.index(password[i % len(password)])
        index = (letters.index(cipher[i]) - shift) % len(letters)
        plain += letters[index]
    return plain


def permVector(password):
    cols = len(password)

    perm = [cols]*cols
    inpw = []
    for i in range(cols):
        n = letters.index(password[i]) % cols
        if n not in inpw:
            inpw.append(n)
            perm[i] = n

    spare = []
    for i in range(cols):
        if i not in inpw:
            spare.append(i)

    spareIndex = 0
    for i in range(cols):
        if perm[i] == cols:
            perm[i] = spare[spareIndex]
            spareIndex += 1

    return perm


def encryptVector(plain, password):
    perm = permVector(password)
    partLength = len(perm)
    cipher = ""
    parts = len(plain) // partLength
    if len(plain) > (parts * partLength):
        parts += 1

    plainIndex = 0
    for i in range(parts):
        partCipher = [" "]*partLength
        for j in range(partLength):
            partCipher[perm[j]] = plain[plainIndex]
            plainIndex += 1
            if plainIndex == len(plain):
                break
        cipher = cipher + "".join(partCipher)

    return cipher


def decryptVector(cipher, password):
    perm = permVector(password)

    partLength = len(perm)
    invPerm = [0]*partLength
    for i in range(partLength):
        invPerm[perm[i]] = i

    plain = ''
    parts = len(cipher) // partLength
    if len(cipher) > (parts * partLength):
        parts += 1

    cipherIndex = 0
    for i in range(parts):
        partplain = [' ']*partLength
        for j in range(partLength):
            partplain[invPerm[j]] = cipher[cipherIndex]
            cipherIndex += 1
            if cipherIndex == len(cipher):
                break
        plain += "".join(partplain)

    return plain


# Meminta input plain dan password
plain = input("Masukkan teks: ")
password = input("Password: ")

# Mencetak hasil program
print()
cipherVigenere = encryptVigenere(plain, password)
print("Hasil enkripsi Vigenere: ", cipherVigenere)
cipherVect = encryptVector(cipherVigenere, password)
print("Hasil enkripsi Rectangle: ", cipherVect)

print("\nHASIL ENKRIPSI FINAL=", cipherVect, '\n')

plainVect = decryptVector(cipherVect, password)
print("Hasil dekripsi Rectangle: ", plainVect)
plainVigenere = decryptVigenere(plainVect, password)
print("Hasil dekripsi Vigenere: ", plainVigenere)

print("\nHASIL DEKRIPSI FINAL=", plainVigenere)
