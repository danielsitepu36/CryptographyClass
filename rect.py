def encrypt(plain, cols):
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


def decrypt(cipher, column):
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


plain = input("Enter plain text: ")
cols = input("Cols: ")
cols = int(cols)

cipher = encrypt(plain, cols)
plains = decrypt(cipher, cols)
print("Ciper: " + cipher)
print("Plain: " + plains)
