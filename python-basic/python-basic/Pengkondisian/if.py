"""

    if

    1. if adalah statement yang akan mengecek nilai variabel di dalamnya memenuhi kriteria suatu kondisi atai tidak.
    2. Jika memenuhi kriteria, kondisi tersebut bernilai True.
    3. Jika tidak memenuhi kriteria, kondisi tersebut bernilai False.
    4. Jika kondisi if bernilai True, maka statement di dalamnya akan dieksekusi.
    5. if adalah kode blok, sehingga di dalam blok if perlu indentasi.

"""

print(10 * "=", "IF", 10 * "=")

x = int(input("Masukkan nilai x: "))
y = int(input("Masukkan nilai y: "))

if x > y:
    print("True! x lebih besar dari y")
