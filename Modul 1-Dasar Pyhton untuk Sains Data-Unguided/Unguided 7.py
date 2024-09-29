def min_coins(amount, coin_values):
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
    main()