def encrypt(plain,password):
    plainIntVector = []
    for i in range(len(plain)):
        plainIntVector.append(ord(plain[i]))
    passwordIntVector = []
    for i in range(len(password)):
        passwordIntVector.append(ord(password[i]))

    plainIndex = 0
    cipherIntVector = []
    while plainIndex < len(plain):
        for i in range(len(password)):
            if plainIndex == len(plain):
                break
            oneCharCipher = plainIntVector[plainIndex]^passwordIntVector[i]
            cipherIntVector.append(oneCharCipher)
            plainIndex += 1
    return cipherIntVector

def decrypt(cipherIntVector,password):
    passwordIntVector = []
    for i in range(len(password)):
        passwordIntVector.append(ord(password[i]))
    cipherIndex = 0
    plainIntVector = []
    while cipherIndex < len(cipherIntVector):
        for i in range (len(password)):
            if cipherIndex == len(cipherIntVector):
                break
            oneCharPlain = cipherIntVector[cipherIndex]^passwordIntVector[i]
            plainIntVector.append(oneCharPlain)
            cipherIndex += 1
    plain = ''
    for i in range(len(plainIntVector)):
        plain = plain + chr(plainIntVector[i])
    return plain

plain = input("Plain text: ")
password = input("Password: ")

cipher = encrypt(plain, password)
print ("Cipher: ", end='')
print(cipher)

print("Plain: " + decrypt(cipher,password))
