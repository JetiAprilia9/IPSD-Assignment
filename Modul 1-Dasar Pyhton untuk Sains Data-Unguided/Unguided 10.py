def binary_search(even_numbers, target):
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
    main()