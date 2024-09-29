def factorial(n):
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
print(result)