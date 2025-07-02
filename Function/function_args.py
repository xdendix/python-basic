# args (*args) adalah argumen yang tidak diketahui jumlahnya.
# args memungkinkan kita untuk mengirimkan sejumlah argumen ke fungsi tanpa harus menentukan jumlahnya secara eksplisit.

def hitung(*num):
    print(sum(num))


hitung(1, 2, 3, 4, 5)  # Output: 15
hitung(4, 5, 6, 7, 8)  # Output: 30
