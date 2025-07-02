"""

     Ternary Operator

     1. Ternary Operator adalah cara singkat untuk menulis pernyataan if-else dalam satu baris.
     2. Ternay bersifat expression, dengan demikian kita bisa menyimpannya ke dalam variabel.
     3. format penulisan:
     value = hasil_jika_kondisi_benar if kondisi else hasil_jika_kondisi_salah

"""

x = int(input("Masukkan nilai: "))

result = "Genap" if x % 2 == 0 else "Ganjil"

print(f"Nilai {x} adalah {result}.")
