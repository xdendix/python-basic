username = input("Masukkan Username Anda: ")
password = input("Masukkan Password Anda: ")

hasil = username == "Admin" and len(password) >= 10
print("Status login Anda adalah: ", hasil)