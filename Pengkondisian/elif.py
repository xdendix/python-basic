"""

    Elif

    1. elif adalah kependekan dari else if, yang digunakan untuk mengecek kondisi lain jika kondisi sebelumnya tidak terpenuhi.
    2. elif statement berada di posisi setelah if.
    3. elif statement dapat dibuat lebih dari satu kali dalam sebuah if statement.

"""

print(10 * "=", "IF", 10 * "=")

x = int(input("Masukkan nilai x: "))
y = int(input("Masukkan nilai y: "))

if x > y:
    print("True! x lebih besar dari y")
elif x == y:
    print("x sama dengan y")
else:
    print("False! x tidak lebih besar dari y")
