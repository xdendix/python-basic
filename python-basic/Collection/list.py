"""

    1. Data yang disimpan ke dalam List boleh duplikat
    2. Terurut (ordered). Element dalam List disimpan sesuai urutan yang dimasukkan.
    3. Dapat diubah (mutable). Element List dapat diubah, ditambah, dan dihapus.
    4. Tipe data di dalam List boleh berbeda.
    5. Untuk membuat List kita bisa menggunakan kurung siku []

"""

list_1 = ["Dendi", 32, True, "Coding"]

print(list_1)

print(10 * "=", "Mengakses Element Pada List", 10 * "=")

fruits = ["banana", "apple", "orange"]

print(fruits[0])
print(fruits[1])
print(fruits[2])

print(10 * "=", "Mengakses Element Pada List Dengan Index Negatif (-)", 10 * "=")

full_name = ["Dendi", "Prayogo", "Hidayat"]

# mencetak nilai dari urutan belakang
print(full_name[-1])
print(full_name[-2])
print(full_name[-3])

print(10 * "=", "Mengakses Element Pada List Dengan Range of Index", 10 * "=")

list_a = ["a", "b", "c", "d", "e", "f", "g", "h"]

result_1 = list_a[:4]  # mengakses index hanya end saja
result_2 = list_a[4:7]  # mengakses index dengan star:end

print(result_1)
print(result_2)

print(10 * "=", "Mengecek Element Di Dalam List Dengan in dan not in", 10 * "=")

x = [1, 2, 3, 4, 5]

print(5 in x)
print(5 not in x)

print(10 * "=", "Mengubah Element Di Dalam List", 10 * "=")

animals = ["cat", "bird", "dog", "rabbit", "lion"]

animals[1] = "tiger"  # index ke-1 "bird" diganti menjadi "tiger"

print(animals)

print(10 * "=", "Mengubah Element Di Dalam List Dengan Range of Index", 10 * "=")

animals = ["cat", "bird", "dog", "rabbit", "lion"]

animals[2:4] = ["monkey", "dolphin"]

print(animals)

print(10 * "=", "Menambahkan dan Menggabungkan Element Di Dalam List Dengan append(), insert() dan extend()", 10 * "=")

colors = ["red", "green", "blue"]

print(colors)

colors.append("yellow")  # menambahkan element di akhir

print(colors)

colors.insert(1, "orange")  # menambahkan element di antara element yang lain

print(colors)

colors_2 = ["black", "white"]

colors.extend(colors_2)

print("menggabungkan 2 colors dengan extend() = ", colors)

print(10 * "=", "Menghapus Element di Dalam List Dengan remove(), pop(), dan clear()", 10 * "=")

abjad = ["a", "b", "c", "d", "e", "f", "g", "h"]
