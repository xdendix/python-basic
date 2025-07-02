"""

    Continue While Loop

    1. Continue adalah statement untuk menghentikan iterasi saat ini dari loop dan melanjutkan ke iterasi berikutnya.

"""

i = 0  # Inisialisasi i

while i < 10:  # Kondisi loop
    i += 1  # Increment i setiap iterasi
    if i == 5:  # Jika i sama dengan 5, lanjutkan ke iterasi berikutnya
        continue  # Ini akan melewati print(i) ketika i adalah 5
    print(i)  # Output: 1, 2, 3, 4, 6, 7, 8, 9, 10

print(10 * "=", "Menampilkan bilangan ganjil", 10 * "=")

i = 0  # Inisialisasi i

while i < 10:  # Kondisi loop
    i += 1  # Increment i setiap iterasi
    if i % 2 == 0:  # Jika i adalah bilangan genap, lanjutkan ke iterasi berikutnya
        continue
    print(i)  # Output: 1, 3, 5, 7, 9

print(10 * "=", "Menampilkan bilangan genap", 10 * "=")

i = 0  # Inisialisasi i

while i < 10:  # Kondisi loop
    i += 1  # Increment i setiap iterasi
    if i % 2 != 0:  # Jika i adalah bilangan ganjil, lanjutkan ke iterasi berikutnya
        continue
    print(i)  # Output: 2, 4, 6, 8, 10
