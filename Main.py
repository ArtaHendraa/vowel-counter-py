# deklarasi variabel sentence untuk menyimpan kalimat yang akan dihitung huruf-hurufnya
sentence = input("Masukan teks: ")

# variabel untuk menghitung jumlah huruf vokal, konsonan, whitespace, dan karakter lain pada kalimat
vowel_count = 0
consonant_count = 0
whitespace_count = 0
other_count = 0

# logika penghitungan huruf vokal, konsonan, spasi, dan karakter lain pada kalimat
for ch in sentence:
    if ch.lower() in "aiueo":
        vowel_count += 1
    elif ch.isalpha():
        consonant_count += 1
    elif ch.isspace():
        whitespace_count += 1
    else:
        other_count += 1

# output
print(f"Jumlah huruf Vokal pada teks adalah: {vowel_count}")
print(f"Jumlah huruf Konsonan pada teks adalah: {consonant_count}")
print(f"Jumlah karakter Whitespace/Spasi pada teks adalah: {whitespace_count}")
print(f"Jumlah Karakter Lain pada teks adalah: {other_count}")
