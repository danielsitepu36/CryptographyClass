letters = "abcdefghijklmnopqrstuvwxyz "
invLetters = {}

numLetters = len(letters)

for i in range(numLetters):
    invLetters[letters[i]] = i

def permTable(password):
    global invLetters
    cols = len(password)
    #create permutation vector
    #use cols as void markers
    perm = [cols for i in range(cols)]
    
    inpw = []
    for i in range(cols):
        #create permutation vector from password
        n = invLetters[password[i]] % cols
        #should not use the same entry
        if n not in inpw:
            inpw.append(n)
            perm[i] = n
            
    #get permutation numbers that have not been taken
    spare = []
    for i in range(cols):
        if i not in inpw:
            spare.append(i)
    
    spareIndex = 0
    #void entries in the permuation vector are filled with the spares
    for i in range(cols):
        if perm[i] == cols: #void
            perm[i] = spare[spareIndex]
            spareIndex += 1
    return perm

def encrypt(plain,password):
    perm = permTable(password)
    partLength = len(perm)

    cipher = ""
    parts = len(plain) // partLength
    if len(plain) > (parts * partLength):
        parts = parts+1

    plainIndex = 0
    for i in range(parts):
        partCipher = [" "]*partLength
        for j in range(partLength):
            partCipher[perm[j]] = plain[plainIndex]
            plainIndex = plainIndex+1
            if plainIndex == len(plain):
                break
        cipher = cipher+ ''.join(partCipher)
    return cipher

def decrypt(cipher,password):
    perm = permTable(password)
    partLength = len(perm)
    invPerm = [0]*partLength
    for i in range(partLength):
        invPerm[perm[i]] = i

    plain = ""
    parts = len(cipher) // partLength

    cipherIndex = 0
    for i in range(parts):
        partPlain = [" "]*partLength
        for j in range(partLength):
            partPlain[invPerm[j]] = cipher[cipherIndex]
            cipherIndex = cipherIndex+1
        plain = plain+ ''.join(partPlain)
    return plain

plain = input("Enter plain text: ")
password = input("Password: ")
cipher = encrypt(plain,password)
print (cipher)
print (decrypt(cipher,password))
