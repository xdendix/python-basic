z = 0  # Inisialisasi variabel z dengan nol
try:  # Blok try untuk menangkap potensi error
    print(1 / z)  # Mencoba membagi 1 dengan z
except ZeroDivisionError:  # Menangkap error pembagian dengan nol
    print("Error: Anda tidak dapat membagi dengan nol.")  # Menampilkan pesan error
