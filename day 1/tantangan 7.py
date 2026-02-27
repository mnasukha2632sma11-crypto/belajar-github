nama = input("Input Nama: ")
gaji_pokok = float(input("Input Gaji Pokok: "))

tunjangan = 0.20 * gaji_pokok
pajak = 0.15 * (gaji_pokok + tunjangan)
gaji_bersih = gaji_pokok + tunjangan - pajak

print(f"Nama: {nama}")
print(f"Gaji Pokok: {gaji_pokok}")
print(f"Gaji Bersih: {gaji_bersih}")