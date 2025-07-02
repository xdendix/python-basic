"""

    1. Set adalah salah satu tipe data collection di Python yang digunakan,
    untuk menyimpan kumpulan element yang unik dan tidak berurutan.
    2. Set mirip dengan himpunan matematika, sehingga tidak ada element yang duplikat di dalamnya.
    3. Karakteristik dari Set adalah, tidak terurut, tidak bisa diubah, dan tidak memiliki index.
    Dengan demikian, element pada Set akan selalu acak posisinya.
    4. Namun walau Set tidak bisa diubah, kita bisa tetap menghapus dan menambah element.
    5. Untuk menggunakan Set, gunakan karakter kurung kurawal {}
    6. Karena Set tidak memiliki nomor index ataupun key, kita tidak bisa mengakses element di dalam Set.
    7. Namun cara mengaksesnya adalah dengan menggunakan perulangan.

"""
from duplicity.log import setverbosity

print(10 * "=", "Cara menambahkan dan menggabungkan element di set dengan add() dan update()", 10 * "=")

colors = {"red", "green", "blue"}

print(colors)

colors.add("white")  # menambahkan element di dalam set

print(colors)

colors_b = {"silver", "purple", "yellow"}

colors.update(colors_b)  # menggabungkan kedua element di set

print(colors)

print(10 * "=", "Cara menghapus element di set dengan remove() dan discard()", 10 * "=")

fruits = {"apple", "banana", "strawberry"}

print(fruits)

fruits.remove("apple")  # untuk menghapus element yg ada di set, jika datanya tidak ada, akan error (raise)

print(fruits)

fruits.discard("banana")  # untuk menghapus element yg ada di set, jika datanya tidak ada, tidak akan error

print(fruits)

"""

    Union
    1. union() akan menggabungkan seluruh element dari kedua Set dan mengembalikan Set yang baru.
    2. Ada cara yang lebih ringkas lagi selain menuliskan method union(), yaitu menggunakan operator pipe(|)
    3. Keduanya akan mengembalikan hasil yang sama.
    4. union() juga bisa menggabungkan beberapa Set sekaligus, dengan memisahkan Set satu dengan yang lainnya,
    menggunakan koma.
    
"""
print(10 * "=", "Cara menggunakan method union() dan pipe() di Set", 10 * "=")

set_a = {1, 2, 3}
set_b = {4, 5, 6}
set_c = set_a.union(set_b)

print("menggabungkan kedua element dengan method union() = ", set_c)

set_d = {7, 8, 9}
set_e = {10, 11, 12}
set_f = set_d | set_e

print("menggabungkan kedua element dengan method pipe() = ", set_f)

print(10 * "=", "Cara menggunakan method multiple union() dan pipe() di Set", 10 * "=")

words_a = {"a", "b", "c"}
words_b = {"d", "e", "f"}
words_c = {"g", "h", "i"}
result = words_a.union(words_b, words_c)

print("menggabungkan kedua element dengan method multiple union() = ", result)

result = words_a | words_b | words_c

print("menggabungkan kedua element dengan method multiple pipe() = ", result)

"""

    intersection
    1. intersection hanya akan menggabungkan kedua Set yang memiliki nilai duplikat.
    2. Kita juga bisa mengganti penulisan method dengan operator AND (&)
    3. Perbedaannya adalah, menggunakan method intersection bisa menggabungkan Set dengan tipe data,
    collection yg lain seperti List dan Tuple. Sedangkan menggunakan operator AND (&) tidak bisa.
    4. method intersection akan mengembalikan Set baru dan tidak akan merubah Set aslinya.
    5. Jika ingin merubah Set aslinya juga, kita bisa menggunakan method intersection_update()

"""
print(10 * "=", "Cara menggunakan method intersection() di Set", 10 * "=")

set_x = {1, 2, 3}
set_y = {1, 2, "ok"}
set_z = {3, 4, 1}

result_x_y = set_x.intersection(set_y)
result_x_z = set_x.intersection(set_z)

print("hasil result x dan y adalah = ", result_x_y)
print("hasil result x dan z adalah = ", result_x_z)

print(10 * "=", "Cara menggunakan method intersection_update() dan AND (&) di Set", 10 * "=")

set_x.intersection_update(set_y)  # untuk mengubah nilai dari element x dan y

print(set_x)

result = set_x & set_y  # untuk menggabungkan kedua variable menggunakan AND (&)

print(result)

"""

    Difference
    1. Metode difference() akan mengembalikan set baru yang hanya berisi item dari set pertama,
    yang tidak ada di set lainnya.
    2. difference() juga memiliki operator sebagai penggantinya, yaitu minus (-)
    3. Jika difference() akan mengembalikan Set baru, ada juga difference_update() untuk mengubah isi dari Set aslinya.

"""

print(10 * "=", "Cara menggunakan method difference(), minus (-) dan difference_update() di Set", 10 * "=")

set_a = {1, 2, 3}
set_b = {1, 2, 4}
set_c = {2, 5, 3}
set_d = set_a.difference(set_b)

print("hasil dari variable a dan b menggunakan difference() adalah = ", set_d)

result = set_a - set_c

print("hasil dari variable a dan c menggunakan minus (-) adalah = ", result)

set_a.difference_update(set_b)  # untuk merubah Set aslinya

print("hasil dari variable a dan b menggunakan difference_update() adalah = ", set_a)

print(set_a)

"""

    symmetric_difference()
    1. symmetric_difference() hanya akan menyimpan element yang tidak ada di kedua Set.
    2. Operator yang bisa digunakan untuk pengganti method adalah ^.
    3. symmetric_difference() akan menciptakan Set baru.
    4. Untuk merubah nilai asli dari Set, kita bisa menggunakan symmetric_update()

"""

print(10 * "=", "Cara menggunakan method symmetric_difference() dan symmetric_update() di Set", 10 * "=")

set_a = {"google", "facebook", "instagram"}
set_b = {"youtube", "facebook", "instagram"}

set_c = set_a.symmetric_difference(set_b)
set_d = set_a ^ set_b

print(set_c)
print(set_d)

set_a.symmetric_difference_update(set_b)  # untuk mengubah nilai aslinya

print(set_a)
