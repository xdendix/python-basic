"""
    Collection Multidimension

    1. Collection Multidimensional adalah Struktur Data yang menyimpan data secara bersarang,
    seperti List di dalam List, Tuple di dalam Tuple dam Dictionary di dalam Dictionary atau kombinasi keduanya.
    2. Ini berguna untuk mengelola data yang lebih kompleks, seperti tabel, matriks, atau data bersarang (nested)
    3. Semua tipe data koleksi bisa menyimpan data bersarang, kecuali tipe koleksi Set.
    Jika ingin menggunakan Set sebagai nested, maka bisa menggunakan fungsi built-in frozenset/ versi immutable dari Set

"""

matriks = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

x1 = matriks[0][2]  # untuk mengambil element pertama dan mengambil index kedua di dalam element
x2 = matriks[2][2]  # untuk mengambil element kedua dan mengambil index kedua di dalam element

print(x1)
print(x2)
