import csv


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
    main()
