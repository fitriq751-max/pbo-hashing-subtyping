"""
Program Hashing String
Menggunakan konsep OOP dan Subtyping
Mata Kuliah: Pemrograman Berorientasi Objek
"""

from md5_hash import MD5Hash
from sha1_hash import SHA1Hash
from sha256_hash import SHA256Hash
from sha512_hash import SHA512Hash
from hash_manager import HashManager


# Function untuk menampilkan menu pilihan algoritma hashing
def tampilkan_menu():

    print("\n===== PROGRAM HASHING STRING =====")
    print("1. MD5")
    print("2. SHA1")
    print("3. SHA256")
    print("4. SHA512")
    print("5. Keluar")


# Function untuk memilih object algoritma hashing
# berdasarkan input user
def pilih_algoritma(pilihan):

    if pilihan == "1":
        return MD5Hash()

    elif pilihan == "2":
        return SHA1Hash()

    elif pilihan == "3":
        return SHA256Hash()

    elif pilihan == "4":
        return SHA512Hash()

    else:
        return None


# Function utama program
def main():

    # Membuat object manager hashing
    manager = HashManager()

    while True:

        tampilkan_menu()

        pilihan = input("Pilih algoritma hashing: ")

        # Kondisi untuk keluar dari program
        if pilihan == "5":
            print("Program selesai.")
            break

        # Memilih algoritma hashing
        algoritma = pilih_algoritma(pilihan)

        # Validasi jika pilihan tidak tersedia
        if algoritma is None:
            print("Pilihan tidak valid!")
            continue

        # Input text dari user
        text = input("Masukkan text yang ingin di-hash: ")

        # Menentukan algoritma hashing
        manager.set_algorithm(algoritma)

        # Generate hash text
        hasil_hash = manager.generate_hash(text)

        print("\n===== HASIL HASH =====")
        print("Algoritma :", algoritma.name)
        print("Text      :", text)
        print("Hash      :", hasil_hash)


# Menjalankan function utama
if __name__ == "__main__":
    main()