matriks = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for m in matriks:  # Mengiterasi setiap baris dalam matriks
    for n in m:  # Mengiterasi setiap elemen dalam baris
        print(n, end=' ')  # Mencetak elemen dengan spasi sebagai pemisah
    print()  # Untuk membuat baris baru setelah setiap baris matriks
