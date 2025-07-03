angka = [1, 2, 3, 4]
pangkat = []

for n in angka:
    pangkat.append(n**2)
print(pangkat)

# List comprehension
angka = [1, 2, 3, 4]
pangkat = [n**2 for n in angka]
print(pangkat)
