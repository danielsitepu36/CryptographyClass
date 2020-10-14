import random


def hash(plain):
    cols = 4
    start_char = 119
    codomain = [0]*cols
    result = ''

    # Random digunakan sebagai padding apabila len(plain)<jumlah kodomain(cols)
    # Menentukan seed fungsi random, agar tidak benar2 acak
    # Dan hasil random tidak berubah pada fungsi hash untuk plain yang sama
    random.seed(len(plain))

    # Membagi string kedalam 4 kolom codomain
    # Lalu enghitung total jumlah ascii character per kolom dimodulo 4
    for i in range(len(plain)):
        modulo = i % cols
        if(i <= len(plain)):
            codomain[modulo] += (ord(plain[i % len(plain)]) % cols)
        # Apabila len(plain)<cols, codomain selanjutnya akan ditambah char random
        # Namun sesuai seed len(plain) yang telah ditentukan
        else:
            codomain[modulo] += (start_char + random.randint(0, 26))

    # Nilai codomain per kolom diubah menjadi string
    for i in range(cols):
        codomain[i] %= cols
        result += chr(start_char+codomain[i])

    return result


# Meminta input dan menampilkan hasil
plain = input("Plain text: ")

digest = hash(plain)
print("Digest: ", end='')
print(digest)
