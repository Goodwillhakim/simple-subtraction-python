def kurangkan (a: float, b: float) :
    return a - b

a = float(input("Masukan Angka: "))
b = float(input("Masukan Angka: "))

hasil = kurangkan (a, b)
print(f"Jadi Hasil Pengurangan Adalah",
round(hasil, 2))