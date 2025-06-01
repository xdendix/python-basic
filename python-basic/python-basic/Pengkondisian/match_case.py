"""

    Match Case

    1. Match-Case adalah fitur baru di Python 3.10 yang memungkinkan kita untuk melakukan pencocokan pola (pattern matching) pada objek.
    2. Match-Case digunakan untuk mencocokkan nilai atau pola tertentu dengan beberapa kemungkinan kasus.
    3. Namun jika tidak ada yang cocok, kita bisa gunakan wiildcard _(underscore) untuk menangani kasus yang tidak terduga.
    4. Dengan Match-Case ini membuat kode yang membutuhkan banyak if-elif-else menjadi lebih ringkas dan mudah dibaca.
    5. Di bahasa pemrograman lain, seperti switch-case di C, Java, atau JavaScript.

"""

grade = input("Masukkan Grade Anda (A, B, C, D, E): ")

match grade:
    case 'A':
        print("Nilai Anda Sangat Baik")
    case 'B':
        print("Nilai Anda Baik")
    case 'C':
        print("Nilai Anda Cukup")
    case 'D':
        print("Nilai Anda Kurang")
    case 'E':
        print("Nilai Anda Sangat Kurang")
    case _:
        print("Grade Tidak Dikenal, Silakan Masukkan Grade yang Valid")
