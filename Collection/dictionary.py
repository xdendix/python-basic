"""

    Dictionary
    1. Dictionary adalah tipe data collection yang digunakan untuk menyimpan data,
    dalam bentuk pasangan key dan value.
    2. Key pada dictionary bersifat unique, artinya tidak boleh ada yang sama.
    3. Dictionary juga bersifat mutable, artinya element di dalam dictionary dapat diubah.
    4. Di Python versi 3.7 ke bawah, dictionary tidak terurut. Namun di versi 3.7 ke atas,
    urutan data akan sesuai dengan waktu penambahan data.
    5. Tipe data pada key boleh bertipe apapun selain tipe yang immutable. Namun dalam kenyataannya,
    key dengan tipe string akan lebih sering dibutuhkan.
    6. Untuk valuenya bisa menggunakan tipe data apapun.
    7. Format penulisan dictionary: {key: value}

"""
from pprint import pprint

student = {
    "name": "dendi",
    "age": 32,
    "is_completed": True,
    "hobbies": ["coding", "gaming", "reading"]
}

print(student)
pprint(student)

print(10 * "=", "Mengakses dictionary menggunakan key", 10 * "=")

name = student["name"]  # mengakses dictionary dengan key
age = student.get("age")  # mengakses key dictionary dengan get()

print(name)
print(age)

all_keys = student.keys()  # mengambil hanya nilai key nya saja
all_values = student.values()  # mengambil nilai value nya saja
all_items = student.items()  # mengambil nilai key dan value

print(f"mengambil seluruh keys = {all_keys}")
print(f"mengambil seluruh values = {all_values}")
print(f"mengambil seluruh items = {all_items}")

print(10 * "=", "Mengubah nilai dictionary menggunakan update()", 10 * "=")

car = {
    "brand": "ford",
    "model": "mustang",
    "year": 2012
}

print(car)

car["year"] = 2024  # mengubah nilai dictionary dengan key

print(car)

car.update({  # mengubah nilai dictionary dengan method update()
    "model": "BMW",
})

print(car)

print(10 * "=", "Menambahkan nilai dictionary", 10 * "=")

car[
    "color"] = "black"  # bila menganti key di dictionary dan tidak ada, maka nilainya akan menjadi element baru di dictionary

print(car)

"""
    Menghapus Element pada Dictionary
    
    1. Untuk menghapus element pada dictionary, kita bisa menggunakan pop("key")
    2. Atau menggunakan keyword del
    3. Dan untuk menghapus item terakhir yang dimasukkan, kita bisa menggunakan method popitem()
    4. Untuk menghapus seluruh element pada dictionary, gunakan method clear()

"""
print(10 * "=", "Menghapus nilai di dictionary", 10 * "=")

student = {
    "name": "dendi",
    "age": 32,
    "gender": "male",
    "film": "action"
}

print(student)

student.pop("age")  # menghapus element dengan key

print(student)

student.popitem()  # menghapus element terakhir

print(student)

student.clear()  # menghapus semua element dictionary

print(student)
