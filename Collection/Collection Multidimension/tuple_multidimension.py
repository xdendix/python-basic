"""
    Tuple Multidimensional

    1. Tuple adalah struktur data immutable (tidak bisa diubah), tetapi bisa menyimpan koleksi lain sebagai elemennya.
    2. Tuple multidimensi cocok digunakan untuk data yang tidak akan diubah setelah dibuat.
    3. Untuk cara mengaksesnya, sama seperti mengakses List Multidimensi,
    yaitu menggunakan index dengan sebanyak jumlah dimensinya.
    4. Karena Tuple immutable, hal ini menjadi sering mengkombinasikannya dengan list untuk fleksibilitas lebih.
"""

matriks = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)

x1 = matriks[2][1]  # untuk mengambil element kedua dan mengambil index urutan kesatu di dalam tuple
x2 = matriks[2][2]  # untuk mengambil element kedua dan mengambil index urutan kedua di dalam tuple

print(f"x1 hasilnya adalah = {x1}")
print(f"x2 hasilnya adalah = {x2}")
