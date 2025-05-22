print(28 * "=")
print("Selamat Datang di Toko Dendi")
print(28 * "=")

produk = input("Masukkan Nama Produk: ")
harga = float(input("Masukkan Harga Produk: "))
diskon = float(input("Masukkan Diskon Produk: "))

potongan = harga * (diskon / 100)
harga_total = harga - potongan

print(15 * "=", "Rincian Pesanan", 15 * "=")
print(f"Produk: {produk}")
print(f"Harga: {harga}")
print(f"Diskon: {diskon}")
print(f"Total: {harga_total}")