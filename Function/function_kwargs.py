# **kwargs adalah parameter yang dapat menerima sejumlah argumen kunci (keyword arguments) yang tidak ditentukan sebelumnya.
# kwargs memungkinkan kita untuk mengirimkan sejumlah argumen kunci ke dalam fungsi tanpa harus menentukan setiap argumen secara eksplisit.

def showStudent(**std):
    print(type(std))
    print(f"Nama: {std['nama']}")
    print(f"Umur: {std['umur']}")
    print(f"Jurusan: {std['jurusan']}")


showStudent(
    nama="Budi",
    umur=20,
    jurusan="Teknik Informatika"
)
