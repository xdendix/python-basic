"""

    While Loop

    1. Seperti yang telah dijelaskan sebelumnya, perulangan while adalah perulangan yang dilakukan selama kondisi tertentu terpenuhi.
    2. Sintaks dasar dari perulangan while adalah sebagai berikut:
    while kondisi:
        # blok kode yang akan dieksekusi selama kondisi terpenuhi
    3. Kondisi: Sebuah ekspresi logika (boolean).
    Jika kondisi bernilai True, maka blok kode di dalam while akan dieksekusi. Jika kondisi bernilai False, perulangan akan berhenti.

"""

i = 0

while i < 10:
    print(f"Perulangan ke-{i}")
    i += 1  # Increment i untuk menghindari infinite loop
