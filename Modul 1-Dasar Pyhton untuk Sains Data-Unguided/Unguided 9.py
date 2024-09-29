class Buku:
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
    print(f"Usia Buku: {usia} tahun\n")
