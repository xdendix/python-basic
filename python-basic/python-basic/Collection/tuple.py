"""

    1. Tuple sama seperti List, hanya saja nilai di dalam Tuple tidak bisa diubah (immutable)
    2. Penggunaan Tuple lebih hemat memori dibanding menggunakan List.
    3. Tuple juga sangat aman dari perubahan-perubahan yang tidak disengaja, karena sifat immutablenya.
    4. Untuk membuat Tuple, gunakan tanda kurung buka dan tutup ()

"""

tuple_1 = ("a", "b", "c")

print(tuple_1)

print(10 * "=", "Cara Mengakses Element Di Dalam Tuple Dengan Index", 10 * "=")

print(tuple_1[0])
print(tuple_1[1])
print(tuple_1[2])

print(10 * "=", "Cara Menggunakan count() di Tuple", 10 * "=")

tuple_1 = ("a", "b", "c", "d", "a")

total_count_a = tuple_1.count("a")  # untuk menghitung jumlah element yang ada di tuple

print("jumlah element a adalah = ", total_count_a)

print(10 * "=", "Cara Menggunakan index() di Tuple", 10 * "=")

tuple_1 = ("a", "b", "c", "d", "a")

index_of_d = tuple_1.index("d")  # untuk mencari tau urutan index dari sebuah element di tuple

print("hasil index dari element d adalah = ", index_of_d)
