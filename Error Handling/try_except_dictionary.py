var_dict = {"rata_rata": "1.0"}

try:
    print(f"rata-rata adalah: {var_dict['rata_rata']}")
except KeyError:
    print("Key tidak ditemukan.")
except TypeError:
    print("Anda tidak bisa membagi nilai dengan tipe data string.")
else:
    print("Kode ini dieskskusi jika tidak ada exception yang terjadi.")
finally:
    print("Kode ini dieksekusi terlepas dari ada atau tidaknya exception.")