"""

    Unpacking

    1. Unpacking adalah proses mengambil element-element dari sebuah koleksi,
    (seperti Listm Tuple, atau Dictionary) dan langsung menyimpannya ke dalam variabel-variabel yang terpisah.
    2. Dengan Unpacking, kita dapat mengelola data lebih mudah tanpa perlu mengakses elemen satu per satu.
    3. Jumlah variabel untuk unpacking harus sesuai dengan jumlah elemen dalam koleksi.
    4. Jika ingin menangkap element-element sisa ke dalam satu variabel,
    kita dapat menggunakan tanda bintang (*) sebelum nama variabel tersebut.

"""

data = [10, 20, 30]

x, y, z = data  # Unpacking List

print(x)
print(y)
print(z)

print(10 * "=", "Unpacking List dengan sisa elemen", 10 * "=")

data2 = [10, 20, 30, 40, 50]
x, y, *z = data2  # Unpacking List dengan sisa elemen

print(x)
print(y)
print(z)  # z akan berisi sisa elemen dalam bentuk List

"""
    Unpacking Dictionary
    
    1. Di tipe data Dictionary, kita mengunpack key dan value dengan cara tertentu.
    2. Untuk mengakses keynya saja, cukup buat variabel sejumlah key yang ada.
    3. Untuk mengakses value-nya, kita dapat menggunakan metode `.values()`.

"""
print(10 * "=", "Unpacking Dictionary dengan key dan value", 10 * "=")

data = {
    "name": "Dendi",
    "age": 32,
}

name, age = data  # Unpacking key dari Dictionary
val1, val2 = data.values()  # Unpacking value dari Dictionary

print(name, age)
print(val1, val2)

"""
    Kombinasi Packing dan Unpacking
    
    1. Packing adalah proses sebaliknya, yaitu menggabungkan elemen-elemen ke dalam satu variabel,
    biasanya menggunakan tanda *.
    
"""
print(10 * "=", "Kombinasi Packing dan Unpacking", 10 * "=")

data = [10, 20, 30, 40, 50]

a, *b, c = data  # Packing List

print(a)  # 10
print(b)  # [20, 30, 40]
print(c)  # 50
