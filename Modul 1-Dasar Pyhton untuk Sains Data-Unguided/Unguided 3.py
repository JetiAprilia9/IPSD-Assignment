def atm_simulation():
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
atm_simulation()
