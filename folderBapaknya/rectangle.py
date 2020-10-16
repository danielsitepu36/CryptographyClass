plain = input("Enter plain text: ")
cols = input("Shift: ")

def encrypt(plain,cols):
    cols = int(cols)
    cipher = ""
    numLines = len(plain) // cols
    if (numLines * cols) < len(plain):
        numLines = numLines + 1

    block = [[" " for x in range(cols)] for y in range(numLines)]
    i = 0
    j = 0
    cipher = ""
    for k in range(len(plain)):
        block[i][j] = plain[k]
        j = (j+1) % cols
        if j == 0:
            i = i+1
    for j in range(cols):
        for i in range(numLines):
            cipher = cipher + block[i][j]
    return cipher

def decrypt(cipher,cols):
    cols = int(cols)
    plain = ""
    numLines = len(cipher) // cols

    block = [[" " for x in range(numLines)] for y in range(cols)]
    i = 0
    j = 0
    plain = ""
    for k in range(len(cipher))::
        block[j][i] = cipher[k]
        i = (i+1) % numLines
        if i == 0:
            j = j+1
    for i in range(numLines):
        for j in range(cols):
            plain = plain + block[j][i]
    return plain

print(encrypt(plain,cols))
print(decrypt(encrypt(plain,cols),cols))
