import string

# Daniel Suranta Sitepu
# 18/424185/PA/18290

# Metode yang digunakan tidak membutuhkan dictionary
# Karena shifting dilakukan langsung menggunakan posisi huruf di 'letters'
letters = string.ascii_letters + " "

# Fungsi enkripsi dengan metode Vigenere
def encryptVigenere(plain, password):
    global letters
    cipher = ""
    # Menggeser char pada plain
    for i in range(len(plain)):
        # Mendapatkan nilai shift untuk penggeseran (Nilai Char ke i(dimodulo panjang password) pada password)
        shift = letters.index(password[i % len(password)])
        # Mendapatkan index huruf setelah ditambah shift dan di modulo panjang letters
        index = (letters.index(plain[i]) + shift) % len(letters)
        # Menambahkan huruf ke-index kedalam cipher
        cipher += letters[index]
    return cipher

# Fungsi dekripsi dengan metode Vigenere
def decryptVigenere(cipher, password):
    global letters
    plain = ""
    # Menggeser char pada cipher
    for i in range(len(cipher)):
        # Mendapatkan nilai shift untuk penggeseran (Nilai Char ke i(dimodulo panjang password) pada password)
        shift = letters.index(password[i % len(password)])
        # Mendapatkan index huruf setelah dikurangi shift dan di modulo panjang letters
        index = (letters.index(cipher[i]) - shift) % len(letters)
        # Menambahkan huruf ke-index kedalam plain       
        plain += letters[index]
    return plain

# Fungsi enkripsi dengan metode Rectangle
def encryptRect(plain, cols):
    cipher = ""
    # Mendapatkan jumlah baris, jika baris*kolom kurang dari panjang plain,
    # Jumlah baris akan ditambah 1
    numLines = len(plain) // cols
    if(numLines * cols) < len(plain):
        numLines += 1

    # Membuat bentuk tabel dengan jumlah kolom cols dan baris numLines
    # Diisi dengan ' ' (spasi)
    block = [[" " for i in range(cols)] for j in range(numLines)]

    i = 0
    j = 0

    # Untuk setiap sel yang ada diisi character plain text dengan urutan 
    # Baris 1, kiri ke kanan, baris 2 kiri ke kanan dst
    for k in range(len(plain)):
        block[i][j] = plain[k]
        j = (j+1) % cols
        if j == 0:
            i = i+1

    # Mengambil isi setiap sel dengan urutan
    # Kolom 1 dari atas kebawah, kolom 2 dari atas kebawah, dst
    for j in range(cols):
        for i in range(numLines):
            cipher = cipher+block[i][j]

    return cipher

# Fungsi dekripsi dengan metode Rectangle
def decryptRect(cipher, column):
    plain = ''
    numLines = len(cipher) // column
    # Mendapatkan jumlah baris, jika baris*kolom kurang dari panjang plain,
    # Jumlah baris akan ditambah 1
    if(numLines * column) < len(cipher):
        numLines += 1
    
    # Membuat bentuk tabel dengan jumlah kolom cols dan baris numLines
    # Diisi dengan ' ' (spasi)
    block = [[" " for i in range(numLines)] for j in range(column)]

    i = 0
    j = 0
    
    # Untuk setiap sel yang ada diisi character cipher text dengan urutan
    # Kolom 1 dari atas kebawah, kolom 2 dari atas kebawah, dst
    for k in cipher:
        block[j][i] = k
        i = (i+1) % numLines
        if i == 0:
            j += 1

    # Mengambil isi setiap sel dengan urutan
    # Baris 1, kiri ke kanan, baris 2 kiri ke kanan dst
    for i in range(numLines):
        for j in range(column):
            plain += block[j][i]

    # Memotong spasi sisa enkripsi yang ada pada bagian paling kanan plain text
    plain = plain.rstrip()
    return plain

# Meminta input plain dan password
plain = input("Masukkan teks: ")
password = input("Password: ")

# Meminta input kolom
# Mengecek agar jumlah kolom tidak 0 atau negatif atau bukan angka
# Karena akan menyebabkan error
while(True):
    try:
        cols = input("Kolom: ")
        # Mengubah variable cols dari string menjadi integer agar bisa digunakan untuk looping
        cols = int(cols)
        if(cols <= 0):
            print("Kolom tidak boleh 0 atau negatif, silakan input kolom lagi")
        else:
            break
    except ValueError:
        print("Kolom harus berupa angka, silakan input kolom lagi")

# Mencetak hasil program
print()
cipherVigenere = encryptVigenere(plain, password)
print("Hasil enkripsi Vigenere: ", cipherVigenere)
cipherRect = encryptRect(cipherVigenere, cols)
print("Hasil enkripsi Rectangle: ", cipherRect)

print("\nHASIL ENKRIPSI FINAL=", cipherRect, '\n')

plainRect = decryptRect(cipherRect, cols)
print("Hasil dekripsi Rectangle: ", plainRect)
plainVigenere = decryptVigenere(plainRect, password)
print("Hasil dekripsi Vigenere: ", plainVigenere)

print("\nHASIL DEKRIPSI FINAL=", plainVigenere)
