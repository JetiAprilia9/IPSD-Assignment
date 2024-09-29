# <h1 align="center">Laporan Praktikum Modul Dasar-Dasar Python untuk Sains Data</h1>
<p align="center">Jeti Aprilia</p>

## Dasar Teori

Dalam Modul Pertemuan 1: Dasar-Dasar Python untuk Sains data membahas tentang 
a. Variable dan Tipe Data
Variable adalah tempat dimana kita bisa menyimpan data di memori. Lalu ketentuan untuk type data yakni menggunakan huruf, angka, atau tanda (_), dsb. Adapula tipe-tipe data pada python yaitu integer, float, strung, dan boolean.
b. Operator dan Logika
Operator adalah kode untuk dapat menghitung secara matematis dan logis. Jenis operator adalah Operator aritmatika, Operator Perbandingan, dan Operator Logika. Ketiganya memiliki ketentuan-ketentuan yang harus diikuti agar program dapat berjalan.
c. Fungsi dan Perulangan
"Fungsi adalah blok kode yang dapat digunakan kembali", fungsi sangat penting untuk program perulangan yang akan sering menggunakan fungsi karena dapat digunakan kembali. Adapun jenis-jenis looping yaitu For Loop, While Loop, dan List Comprehension.
d. Percabangan 
Ketika program membutuhkan pengambilan keputusan, maka percabangan akan digunakan sesuai dengan fungsinya. Adapula jenis-jenis percabangan yaitu If, Elif, Else, dan Nested Conditionals.

## Guided 

### 1. Variable dan Tipe Data

```python
print (nilai = 100
print(f'nilai kamu adalah {nilai} dan tipe datanya adalah {type(nilai)}')
nilai = float(nilai)
print(f'nilai kamu adalah {nilai} dan tipe datanya adalah {type(nilai)}'))
```

```python
print (text = "ulang "
multiplied_text = text * 3
print(multiplied_text))
```

### 2. If, Elif, Else

```python
print (username = input("Enter username: ")
if username == "Jono":
    print("Selamat datang {username}")
elif username == "Slamet":
    print(f"Selamat datang {username}")
else:
    print("Nama tidak dikenali"))
```

```python
print (if os.path.exists("example.txt"):
    print("File exists")
else:
    print("File does not exist"))
```

### Pengulangan (Loops)

#### For Loop
```python
print (for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
    print())
```

#### If, Elif, Else

```python
print (num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if num2 != 0:
    print(num1 / num2)
else:
    print("Cannot divide by zero"))
```

### Fungsi

```python
print (start = 1
end = 10
sum_odds = sum(i for i in range(start, end + 1) if i % 2 != 0)
print(f"Sum of odd numbers between {start} and {end} is {sum_odds}"))
```

```python
print (numbers = [1, 2, 2, 3, 4, 4, 4, 5]
unique_numbers = set(numbers)
print(len(unique_numbers)))
```

```python
print (with open("example.txt", "a") as file:
    file.write("\nNew line added."))
```

```python
print (with open("example.txt", "r") as file:
    content = file.read()
    word_count = len(content.split())
    print(word_count))
```

```python
print (import datetime
today = datetime.datetime.now()
print(today.strftime("%A")))
```

### Exception

```python
print (result = 10/0
print(result))
```

```python
print (try:
    result = 10 / 0
except ZeroDivisionError:
    print("Division by zero is not allowed"))
```

### Operator dan Logika

```python
print (import math
def volume(radius):
    return (4/3) * math.pi * radius**3)
```

## Unguided 

### 1. Soal 1: Memecahkan Masalah Unik dengan Loop dan If-Else
**Soal**: Buatlah program yang dapat menghasilkan pola berbentuk angka seperti di bawah ini, dengan syarat angka yang ditampilkan adalah hasil dari penjumlahan bilangan prima sebelumnya:
```
1
2 3
5 7 11
13 17 19 23
...
```
Jumlah angka pada setiap baris bertambah 1, dan bilangan yang ditampilkan adalah bilangan prima.

```python
print("def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def generate_primes(count):
    """Generate a list of the first 'count' prime numbers."""
    primes = []
    num = 2  # Start checking for primes from 2
    while len(primes) < count:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes


def print_prime_pattern(rows):
    """Print the prime number pattern."""
    total_primes = sum(range(1, rows + 1))  # Total number of primes needed
    primes = generate_primes(total_primes)

    index = 0
    for row in range(1, rows + 1):
        for _ in range(row):
            print(primes[index], end=' ')
            index += 1
        print()  # Move to the next line


# Example usage
print_prime_pattern(5)")
```
#### Output:
![Screenshot (499)](https://github.com/user-attachments/assets/7f05364c-0773-43d6-b1dc-c8becbdc8d9d)

#### Penjelasan
Fungsi ```is_prime(n)``` berguna untuk memeriksa apakah angka yang dimasukkan pada n adalah bilangan prima. Lalu Fungsi ```generate_primes(count)``` berguna untuk mengeksekusi dan menjawab daftar bilangan prima sebanyak (count). Fungsi ```print_prime_pattern(rows)``` adalah mencetak pola bilangan prima sesuai ketentuan dimana jumlah angka akan bertambah satu pada setiap baris dari baris sebelumnya. Untuk menjalankan program, panggil ```print_prime_pattern(n)``` dan isi n sesuai angka yang diinginkan.


### 2. Buatlah sebuah fungsi yang menerima dua input berupa list angka. Fungsi ini harus mengembalikan sebuah list baru yang berisi elemen dari dua list input yang memiliki indeks ganjil. List baru tersebut juga harus diurutkan secara menurun berdasarkan nilai elemen.

```python
print("def filter_and_sort_odd_indices(list1, list2):
    """Mengembalikan list baru dari elemen dengan indeks ganjil dari dua list yang diurutkan secara menurun."""
    # Mengambil elemen dari indeks ganjil di kedua list
    odd_index_elements = []

    for i in range(1, len(list1), 2):
        odd_index_elements.append(list1[i])

    for i in range(1, len(list2), 2):
        odd_index_elements.append(list2[i])

    # Mengurutkan elemen secara menurun
    odd_index_elements.sort(reverse=True)

    return odd_index_elements


# Contoh penggunaan
list1 = [10, 20, 30, 40, 50]
list2 = [5, 15, 25, 35, 45]
result = filter_and_sort_odd_indices(list1, list2)
print(result)")
```

#### Output
![Screenshot (500)](https://github.com/user-attachments/assets/25b30fc6-932a-4b7a-81ca-b0a784778963)

#### Penjelasan
Pada function ```filter_and_sort_odd_indices(list1, list2)``` akan mengambil elemen dengan indeks ganjil dari kedua list yang menerima argumen (list1, list2), For berfungsi untuk ekstrak elemen pada bilangan ganjil dan menggabungkan elemen indeks ganjil tersebut ke dalam ```odd_index_elements```, serta ```sort(reverse=True) untuk mengurutkan list baru secara menurun.

### 3. Soal 3: Exception Handling dalam Konteks Nyata
**Soal**: Buat sebuah program untuk mensimulasikan transaksi ATM. Program harus:
1. Meminta pengguna memasukkan PIN (dibatasi 3 kali percobaan).
2. Setelah PIN benar, meminta jumlah penarikan.
3. Jika saldo kurang dari jumlah yang ditarik, munculkan pesan kesalahan.
4. Jika penarikan berhasil, tampilkan saldo akhir.

```python
print("def atm_simulation():
    # Inisialisasi PIN dan saldo
    correct_pin = "1234"
    balance = 100000  # Saldo awal
    max_attempts = 3

    # Meminta pengguna memasukkan PIN
    for attempt in range(max_attempts):
        pin = input("Masukkan PIN Anda: ")
        if pin == correct_pin:
            print("PIN benar. Selamat datang!")
            break
        else:
            print(f"PIN salah. Percobaan {attempt + 1} dari {max_attempts}.")
    else:
        print("Anda telah memasukkan PIN yang salah terlalu banyak. Transaksi dibatalkan.")
        return

    # Meminta jumlah penarikan
    try:
        withdrawal_amount = float(input("Masukkan jumlah penarikan: "))
        if withdrawal_amount <= 0:
            raise ValueError("Jumlah penarikan harus lebih besar dari nol.")

        # Memeriksa apakah saldo cukup
        if withdrawal_amount > balance:
            print("Kesalahan: Saldo tidak cukup untuk penarikan tersebut.")
        else:
            balance -= withdrawal_amount
            print(f"Penarikan berhasil. Saldo akhir Anda adalah: Rp{balance:,.2f}")

    except ValueError as ve:
        print(f"Kesalahan: {ve}")

# Menjalankan simulasi ATM
atm_simulation()")
```

#### Output
![Screenshot (501)](https://github.com/user-attachments/assets/070cf457-d6f7-462b-9aee-adae323cc9e3)

#### Penjelasan
Pertama program akan menginisialisasi menggunakan variable ```correct_pin``` untuk menyimpan pin (pin harus benar), variable ```balance``` menyimpan saldo sesuai yang diinputkan pengguna, variable ```max_attemps``` memberi syarat jumlah maksimum percobaan memasukkan pin yaitu 3 kali. Loop for akan meminta pengguna memasukkan pin dengan ketentuan jika pin benar maka program dapat berjalan; jika salah sebanyak 3 kali akan tercetak pesan pemberitahuan "Anda telah memasukkan PIN yang salah terlalu banyak. Transaksi dibatalkan" dan program akan keluar. Try digunakan untuk menangani kemungkinan kesalahan dan jika pengguna memasukkan selain angkan, maka pesan kesalahan akan keluar. Lalu jika benar dan saldo mencukupi program akan memeriksa dan mencetak saldo terbaru; jika tidak, akan ditampilkan pesan kesalahan. ```ValueError``` berfungsi untuk memastikan penarikan sudah sesuai ketentuan.


### 4. Soal 4: Studi Kasus Pengelolaan Data
**Soal**: Anda diberikan file CSV berisi data nilai ujian mahasiswa. Tugas Anda adalah menulis sebuah program yang:
1. Membaca file CSV dan menyimpan datanya ke dalam dictionary.
2. Menghitung rata-rata nilai tiap mahasiswa.
3. Menampilkan mahasiswa dengan nilai tertinggi dan terendah.

```python
print("import csv


def read_csv_to_dict(filename):
    """Membaca file CSV dan mengembalikan data dalam bentuk dictionary."""
    data = {}
    with open(filename, mode='r') as file:
        csv_reader = csv.reader(file)
        # Mengabaikan header
        next(csv_reader)
        for row in csv_reader:
            name = row[0]
            grades = list(map(float, row[1:]))  # Mengonversi nilai ke float
            data[name] = grades
    return data


def calculate_average(grades):
    """Menghitung rata-rata dari daftar nilai."""
    return sum(grades) / len(grades) if grades else 0


def main():
    filename = "C:/Users/DELL/Downloads/siswa_nilai (1).csv"

    # Membaca data dari CSV
    student_data = read_csv_to_dict(filename)

    # Menghitung rata-rata nilai dan menemukan mahasiswa dengan nilai tertinggi dan terendah
    averages = {}
    highest_student = None
    lowest_student = None
    highest_average = float('-inf')
    lowest_average = float('inf')

    for student, grades in student_data.items():
        average = calculate_average(grades)
        averages[student] = average

        # Mencari mahasiswa dengan rata-rata tertinggi dan terendah
        if average > highest_average:
            highest_average = average
            highest_student = student

        if average < lowest_average:
            lowest_average = average
            lowest_student = student

    # Menampilkan hasil
    print("Rata-rata nilai mahasiswa:")
    for student, avg in averages.items():
        print(f"{student}: {avg:.2f}")

    print(f"\nMahasiswa dengan nilai tertinggi: {highest_student} (Rata-rata: {highest_average:.2f})")
    print(f"Mahasiswa dengan nilai terendah: {lowest_student} (Rata-rata: {lowest_average:.2f})")


# Menjalankan program utama
if __name__ == "__main__":
    main()")
```

#### Output
![Screenshot (502)](https://github.com/user-attachments/assets/42304946-7a1e-443b-b590-dcdf4cef4f43)

#### Penjelasan
Fungsi ```read_csv_to_dict(filename)``` untuk membaca file csv dan menyimpan data ke dalam dictionary, lalu fungsi ```calculate_average(grades)``` adalah menghitung nilai rata-rata, fungsi main() unuk membaca file CSV, menghitung rata-rata, menemukan nilai min dan max, dan menampilkan hasil. Pastikan untuk memasukkan file CSV ke dalam program agar program dapat berjalan.

### 5. Soal 5: Kombinasi Logika dan Kreativitas
**Soal**: Buatlah permainan sederhana menggunakan Python, di mana komputer akan memilih sebuah angka secara acak antara 1 hingga 100, dan pengguna harus menebak angka tersebut. Setiap tebakan yang salah akan memberikan petunjuk apakah angka yang ditebak lebih besar atau lebih kecil dari angka sebenarnya. Batasi jumlah percobaan menjadi 5 kali. Setelah permainan selesai, tampilkan apakah pemain menang atau kalah.
```python
print("import random


def guessing_game():
    """Permainan tebak angka antara 1 hingga 100."""
    number_to_guess = random.randint(1, 100)  # Memilih angka acak
    attempts = 5  # Batas percobaan

    print("Selamat datang di permainan tebak angka!")
    print("Saya telah memilih angka antara 1 hingga 100.")
    print(f"Anda memiliki {attempts} percobaan untuk menebak angka tersebut.")

    for attempt in range(1, attempts + 1):
        guess = input(f"Tebakan Anda ke-{attempt}: ")

        # Memeriksa apakah input valid
        try:
            guess = int(guess)
        except ValueError:
            print("Silakan masukkan angka yang valid.")
            continue

        # Memeriksa tebakan
        if guess < number_to_guess:
            print("Tebakan Anda terlalu kecil.")
        elif guess > number_to_guess:
            print("Tebakan Anda terlalu besar.")
        else:
            print(f"Selamat! Anda berhasil menebak angka {number_to_guess} dengan {attempt} percobaan!")
            break
    else:
        print(f"Maaf, Anda kehabisan percobaan. Angka yang benar adalah {number_to_guess}.")


# Menjalankan permainan
if __name__ == "__main__":
    guessing_game()")
```

#### Output
![Screenshot (503)](https://github.com/user-attachments/assets/2941036c-799c-42c0-91fb-6ddb888aed1c)

#### Penjelasan
Import Modul random untuk mengacak nilai, fungsi ```guessing_game()``` memilih angka acak 1-100, mengatur percobaan sebanyak 5 kali, dan memberikan informasi game. For loop disini akan berfungsi sebagai pembatasan percobaan, konersi integer dari input pengguna, menampilkan pesan kesalahan jika nilai input tidak valid, memberikan pesan jika tebakan terlalu besar; terlalu kecil; dan benar. Lalu memberikan informasi jika menang, dan akan dieksekusi oleh fungsi ```guessing_game()``` di dalam blok ```if_name_=="_main_":```


### 6. Soal 6: Rekursi yang Tidak Biasa
**Soal**: Buat fungsi rekursif yang menerima input bilangan bulat `n` dan menghasilkan urutan bilangan seperti berikut ini:
```
Input: n = 4
Output: 1, 1, 2, 6, 24
```
Fungsi ini harus menggunakan konsep rekursi untuk menghitung faktorial setiap angka hingga `n`.

```python
print("def factorial(n):
    """Fungsi rekursif untuk menghitung faktorial dari n."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def generate_factorial_sequence(n):
    """Menghasilkan urutan faktorial dari 1 hingga n."""
    if n < 1:
        return []  # Mengembalikan list kosong jika n < 1
    else:
        # Menggunakan rekursi untuk mendapatkan urutan
        sequence = generate_factorial_sequence(n - 1)  # Panggil rekursif untuk n-1
        sequence.append(factorial(n))  # Tambahkan faktorial n ke urutan
        return sequence

# Contoh penggunaan
n = 4
result = generate_factorial_sequence(n)
print(result)")
```

#### Output
![Screenshot (504)](https://github.com/user-attachments/assets/d6aab1dc-b174-478f-968e-19429ddf62ec)

#### Penjelasan
Fungsi factorial(n) utnuk menghitung faktorial sesuai jumlah n dan ketentuan faktorial dari 0 atau 1 adalah 1, jika tidak maka fungsi mengalikan n dengan faktorial dari n-1. Fungsi ```generate_factorial_sequence(n)```yaitu mengembalikan urutan faktorial dari ke n, jika n kurnag dari 1 maka fungsi dikembalikan, jika tidak fungsi memanggil dirinya (n-1 untuk mendapatkan urutan n-1) dan menambahkan ke list.


### 7. Soal 7: Pemrograman dengan Algoritma Greedy
**Soal**: Buatlah program untuk memecahkan masalah "minimum coin change". Diberikan jumlah uang dan daftar nilai koin yang tersedia (misalnya, 1, 5, 10, 25), tentukan kombinasi minimum koin yang diperlukan untuk mencapai jumlah uang tersebut. Namun, program Anda harus bisa menangani koin-koin yang nilai dan jumlahnya ditentukan pengguna.
```python
print("def min_coins(amount, coin_values):
    """Menghitung kombinasi minimum koin untuk mencapai jumlah tertentu."""
    # Mengurutkan nilai koin dari yang terbesar ke terkecil
    coin_values.sort(reverse=True)

    coins_used = []  # List untuk menyimpan koin yang digunakan
    total_coins = 0  # Menghitung total koin yang digunakan

    for coin in coin_values:
        while amount >= coin:  # Selama jumlah uang masih cukup untuk koin ini
            amount -= coin  # Kurangi jumlah uang dengan nilai koin
            coins_used.append(coin)  # Tambahkan koin ke list
            total_coins += 1  # Tambah jumlah koin yang digunakan

    if amount > 0:  # Jika ada sisa jumlah yang tidak dapat dicapai
        return None  # Tidak ada solusi untuk mencapai jumlah tersebut

    return coins_used, total_coins


def main():
    # Input jumlah uang yang ingin dicapai
    amount = int(input("Masukkan jumlah uang yang ingin dicapai: "))

    # Input nilai koin yang tersedia
    coin_values = input("Masukkan nilai koin yang tersedia (pisahkan dengan spasi): ")
    coin_values = list(map(int, coin_values.split()))  # Mengonversi input menjadi list integer

    # Mencari kombinasi koin minimum
    result = min_coins(amount, coin_values)

    if result is None:
        print("Tidak ada kombinasi koin yang dapat mencapai jumlah tersebut.")
    else:
        coins_used, total_coins = result
        print(f"Kombinasi koin minimum: {coins_used}")
        print(f"Total koin yang digunakan: {total_coins}")


# Menjalankan program utama
if __name__ == "__main__":
    main()")
```

#### Output
![Screenshot (505)](https://github.com/user-attachments/assets/bf9c65ff-5e77-4f97-86f8-a5ba759ced92)

#### Penjelasan
Fungsi ```min_coins(amount, coin_values)``` berguna untuk menghitung kombinasi minimum koin, nilai koin diurutkan dari max ke min dengan memaksimalkan nilai yang lebih besar dahulu (strategi greedy), loop while untuk mengurangi amount hingga amount tidak cukup lagi pada nilai koin tersebut (1, 5, 10, 25), koin yang digunakan akan disimpan dalam list ```coin_used``` dan hitung total koin. Jika terdapat sisa amount, maka kombinasi koin untuk jumlah tersebut tidak dapat tercapai. Fungsi main() akan meminta pengguna memasukkan jumlah uang yang diinginkan dan memanggil min_coins untuk kombinasi koin dan cetak hasil.

### 8. Soal 8: Kombinasi String dan Manipulasi List
**Soal**: Buat sebuah program yang menerima string dari pengguna dan mengonversi string tersebut menjadi sebuah list berisi kata-kata terbalik. Misalnya:
```
Input: "Saya suka Python"
Output: ["ayaS", "akus", "nohtyP"]
```

```python
print("def reverse_words(input_string):
    """Mengonversi string menjadi list berisi kata-kata terbalik."""
    # Memecah string menjadi list kata
    words = input_string.split()

    # Membalik setiap kata dan menyimpannya dalam list baru
    reversed_words = [word[::-1] for word in words]

    return reversed_words


def main():
    # Meminta input dari pengguna
    user_input = input("Masukkan string: ")

    # Mengonversi string menjadi list kata terbalik
    result = reverse_words(user_input)

    # Menampilkan hasil
    print("Output:", result)


# Menjalankan program utama
if __name__ == "__main__":
    main()")
```

#### Output
![Screenshot (506)](https://github.com/user-attachments/assets/d80f12b7-dcd8-4ca8-9b33-a75aa98e9bcf)

#### Penjelasan
Fungsi ```reverse_words(input_string)``` yakni mengambil dan memecah input menjadi list kata (split()), dan menggunakan list comprehension untuk membalik dan slicing tiap kata (word[::-1]) dan menyimpan dalam list baru dan mengembalikan list pada reverse_words. Fungsi main() akan meminta pengguna memasukkan kata atau kalimat dan membalik setiap hurufnya, serta mencetak hasilnya.


### 9. Soal 9: Konsep Class dan Object-Oriented Programming
**Soal**: Buat class bernama `Buku` yang memiliki atribut `judul`, `penulis`, dan `tahun_terbit`. Buat method dalam class untuk menampilkan informasi buku, serta method untuk menghitung usia buku berdasarkan tahun saat ini. Buatlah 3 objek dari class `Buku` dan tampilkan informasi serta usia masing-masing buku.
```python
print("class Buku:
    def __init__(self, judul, penulis, tahun_terbit):
        """Inisialisasi atribut buku."""
        self.judul = judul
        self.penulis = penulis
        self.tahun_terbit = tahun_terbit

    def tampilkan_informasi(self):
        """Menampilkan informasi buku."""
        info = (f"Judul: {self.judul}\n"
                f"Penulis: {self.penulis}\n"
                f"Tahun Terbit: {self.tahun_terbit}")
        print(info)

    def hitung_usia(self, tahun_sekarang):
        """Menghitung usia buku berdasarkan tahun saat ini."""
        return tahun_sekarang - self.tahun_terbit

# Membuat objek dari class Buku
buku1 = Buku("Belajar Python", "John Doe", 2020)
buku2 = Buku("Algoritma Pemrograman", "Jane Smith", 2018)
buku3 = Buku("Data Science untuk Pemula", "Alice Johnson", 2021)

# Tahun saat ini
tahun_sekarang = 2024

# Menampilkan informasi dan usia masing-masing buku
for buku in (buku1, buku2, buku3):
    buku.tampilkan_informasi()
    usia = buku.hitung_usia(tahun_sekarang)
    print(f"Usia Buku: {usia} tahun\n")")
```

#### Output
![Screenshot (507)](https://github.com/user-attachments/assets/699986f2-f77d-4098-acb2-2a11e36c0367)

#### Penjelasan

_init_ disini berfungsi sebagai sebuah method konstruktor untuk menginisialisasi judul, penulis, dan tahun_terbit. Lalu pada bagian tampilkan_informasi dan hitung_usia akan memberikan informasi pada buku dan menerima parameter tahun dengan menghitung tahun_terbit-tahun_sekarang. Program ini juga otomatis akan meng update masing-masing atribut pada buku tergNantung pada penambahan objeknya. Kemudia Loop akan mencetak informasi dan usia buku dengan method tersebut.


### 10. Soal 10: Algoritma dengan Persyaratan Logika Khusus
**Soal**: Buatlah program yang mengimplementasikan algoritma pencarian biner, namun dengan modifikasi: algoritma harus bisa mencari nilai di list yang hanya berisi angka genap, dan jika nilai yang dicari adalah angka ganjil, program harus menampilkan pesan bahwa nilai tersebut tidak bisa ditemukan.
```python
print("def binary_search(even_numbers, target):
    """Melakukan pencarian biner untuk menemukan target dalam list angka genap."""
    left, right = 0, len(even_numbers) - 1

    while left <= right:
        mid = (left + right) // 2

        if even_numbers[mid] == target:
            return mid  # Mengembalikan indeks jika ditemukan
        elif even_numbers[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # Mengembalikan -1 jika tidak ditemukan


def main():
    # List angka genap yang sudah diurutkan
    even_numbers = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

    # Meminta input dari pengguna
    user_input = input("Masukkan angka yang ingin dicari: ")

    try:
        target = int(user_input)  # Mengonversi input ke integer

        # Cek apakah target genap atau ganjil
        if target % 2 != 0:
            print("Nilai yang dicari adalah angka ganjil, tidak dapat ditemukan.")
            return

        # Melakukan pencarian biner
        index = binary_search(even_numbers, target)

        if index != -1:
            print(f"Angka {target} ditemukan di indeks {index}.")
        else:
            print(f"Angka {target} tidak ditemukan dalam list.")

    except ValueError:
        print("Silakan masukkan angka yang valid.")


# Menjalankan program utama
if __name__ == "__main__":
    main()")
```

#### Output
![Screenshot (508)](https://github.com/user-attachments/assets/018499e4-03bc-47fb-b6ac-81cd3164860d)

#### Penjelasan

Pada fungsi ```binary_search(even_numbers, target)``` akan menerima list angka genap yang telah urut, menetapkan batas pencarian dengan left dan right, melakukan pencarian biner dengan menghitung indeks tengah dan membandingkan nilai dengan target; jika nilai ditemukan fungsi mengembalikan indeks dan jika tidak fungsi akan terus mempersempit pencarian hingga batas. Fungsi main() yaitu mendefinisikan list angka genap yang sudah urut, meminta input dan konervsi integer, jika angka adalah ganjil akan ditampilkan pesan kesalahan, jika input benar dan genap maka aka memanggil binary_search untuk mencari angka dan menampilkan hasil.

## Kesimpulan
Python adalah bahasa pemrograman yang menggunakan interpreter untuk menjalankan kode programnya. Interpreter tersebut dapat
menerjemahkan kode secara langsung. Python juga memiliki integrasi dengan sistem database dan mampu membaca serta mengubah file yang disini menggunakan file CSV, sehingga mudah untuk digunakan. Pada modul ini, dikarenakan mempelajari dasar-dasar python untuk sains data maka hal yang dapat dipelajari adalah perbedaan tipe data dan jenis-jenis setiap function, operator, perulangan, dan percabangan beserta fungsinya. Pemahaman lebih dapat dicapai ketika telah eksekusi dan memahami setiap soal yang diberikan untuk menyelesaikan masalah.

## Referensi
[1] Rahman. S, et.al.,(2023), "Python: Dasar dan Pemrograman Berorientasi Objek".

Berikut adalah link referensi:
https://tahtamedia.co.id/index.php/issj/article/view/344

