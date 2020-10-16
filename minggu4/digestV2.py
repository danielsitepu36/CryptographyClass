import random


def hash(plain):
    cols = 4
    # Kodomain yang digunakan berupa huruf w/x/y/z (119-122)
    char = ["0", "1", "2", "3", "4", "5", "6", "7",
            "8", "9", "a", "b", "c", "d", "e", "f"]
    startChar = 97
    codomain = [0]*cols
    result = ''

    # Random digunakan sebagai padding apabila len(plain)<jumlah kodomain(cols)
    # Syntax dibawah menentukan seed fungsi random, agar tidak benar2 acak
    # Dan hasil random tidak berubah pada fungsi hash untuk plain yang sama
    random.seed(len(plain))

    # Apabila len(plain)<cols, codomain selanjutnya akan ditambah char random
    # Namun sesuai seed len(plain) yang telah ditentukan
    if len(plain) < cols:
        for i in range(cols - len(plain)):
            if len(plain) >= cols:
                break
            plain += chr(startChar + random.randint(0, 26))

    # Membagi string kedalam 4 kolom codomain
    # Lalu setiap char di kolom tersebut di XOR kan nilai ASCII nya
    for i in range(len(plain)):
        modulo = i % cols
        codomain[modulo] ^= ord(plain[i])

    # Setiap kolom dijadikan char dengan nilai w/x/y/z sesuai hasil xor % 4
    # Ditambah startChar
    for i in range(cols):
        result += chr(startChar + (codomain[i] % cols))

    return result


# Meminta input dan menampilkan hasil
plain = input("Plain text: ")

digest = hash(plain)
print("Digest: ", end='')
print(digest)
