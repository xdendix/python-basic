var = -1

if var < 0:
    raise ValueError("Bilangan negatif tidak diperbolehkan: {}".format(var))
else:
    for i in range(var):
        print(i + 1)
