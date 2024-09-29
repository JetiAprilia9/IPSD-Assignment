import random


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
    guessing_game()