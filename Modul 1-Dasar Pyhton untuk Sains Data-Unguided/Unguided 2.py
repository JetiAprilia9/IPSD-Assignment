def filter_and_sort_odd_indices(list1, list2):
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
print(result)