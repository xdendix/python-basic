"""

    Else While Loop

    1. di While loop juga kita bisa menambahkan statement else.
    2. Blok kode yang berada di dalam statement else akan dieksekusi ketika kondisi pada while loop menjadi False.

"""

i = 0

while i < 10:
    print(f"Perulangan ke-{i}")
    i += 1  # Increment i untuk menghindari infinite loop
else:
    print("Perulangan selesai, kondisi tidak lagi terpenuhi.")
