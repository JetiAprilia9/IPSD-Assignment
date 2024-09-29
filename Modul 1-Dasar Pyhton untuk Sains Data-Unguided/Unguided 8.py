def reverse_words(input_string):
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
    main()