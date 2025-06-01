"""

    Else

    1. else adalah statement jika kondisi if tidak terpenuhi atau False.
    2. Artinya kode di dalam blok else akan dieksekusi jika kondisi if sebelumnya tidak terpenuhi.

"""

print(10 * "=", "IF", 10 * "=")

x = int(input("Masukkan nilai x: "))
y = int(input("Masukkan nilai y: "))

if x > y:
    print("True! x lebih besar dari y")
else:
    print("False! x tidak lebih besar dari y")
