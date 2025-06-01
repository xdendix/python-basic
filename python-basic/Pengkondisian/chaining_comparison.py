"""

    Chaining Comparison Operators

    1. Di python ada istilah yang disebut dengan chaining comparison operators,
    yaitu cara sederhana untuk membandingkan beberapa nilai sekaligus (dalam satu baris).
    2. Misal kita ingin membuat perbadingan seperti ini:
    x > 3 and x < 10
    3. Maka kita bisa menggunakan chaining comparison operators seperti ini:
    3 < x < 10

"""

print(10 * "=", "Chaining Comparison Operators di statement if", 10 * "=")

x = int(input("Masukkan nilai x: "))

if 3 < x < 100:
    print(f"True! nilai x adalah {x}")
