# OOP String Hashing with Subtyping in Python

Program hashing string menggunakan berbagai algoritma hashing populer dengan konsep Object-Oriented Programming (OOP) dan Subtyping pada Python.

## Algoritma Hashing yang Digunakan

- MD5
- SHA1
- SHA256
- SHA512

---

## Konsep OOP yang Digunakan

Project ini menerapkan konsep:

- Abstraction
- Inheritance
- Polymorphism
- Subtyping
- Encapsulation

---

## Class Diagram

```text
                 HashAlgorithm
                        ▲
     -----------------------------------------
     │               │            │          │
  MD5Hash        SHA1Hash    SHA256Hash  SHA512Hash
                        ▲
                        │
                   HashManager
```

---

## Struktur Project

```text
project/
│
├── main.py
├── hash_algorithm.py
├── hash_manager.py
├── md5_hash.py
├── sha1_hash.py
├── sha256_hash.py
└── sha512_hash.py
```

---

## Penjelasan Program

### 1. HashAlgorithm

Abstract class yang menjadi blueprint untuk semua algoritma hashing.

Method abstract:

```python
hash(text)
```

wajib diimplementasikan oleh seluruh subclass.

---

### 2. Subclass Algoritma Hashing

Subclass:

- MD5Hash
- SHA1Hash
- SHA256Hash
- SHA512Hash

merupakan subtype dari:

```python
HashAlgorithm
```

Setiap subclass mengimplementasikan method:

```python
hash()
```

dengan algoritma hashing yang berbeda.

---

### 3. HashManager

Class untuk mengatur algoritma hashing yang digunakan dan menghasilkan hash text menggunakan konsep polymorphism.

---

## Cara Menjalankan Program

```bash
python main.py
```

---

## Contoh Output

```text
===== PROGRAM HASHING STRING =====
1. MD5
2. SHA1
3. SHA256
4. SHA512
5. Keluar

Pilih algoritma hashing: 3

Masukkan text yang ingin di-hash:
Halo Dunia

===== HASIL HASH =====
Algoritma : SHA256
Text      : Halo Dunia
Hash      : c0fdb...
```

---

## Penerapan Subtyping

Contoh subtyping pada program:

```python
algoritma = SHA256Hash()

manager.set_algorithm(algoritma)
```

Karena:

```python
SHA256Hash <: HashAlgorithm
```

maka object `SHA256Hash` dapat digunakan sebagai `HashAlgorithm`.

---

## Library yang Digunakan

- hashlib
- abc

---

## Author

Fitri Khairani Sitorus
Mahasiswa Teknik Informatika  
UIN SUSKA Riau
