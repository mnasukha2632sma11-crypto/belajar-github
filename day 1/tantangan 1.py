# 1. Persegi
sisi = float(input("Masukkan sisi persegi: "))
print(f"Luas Persegi: {sisi * sisi}")
print(f"Keliling Persegi: {4 * sisi}\n")

# 2. Persegi Panjang
p = float(input("Masukkan panjang: "))
l = float(input("Masukkan lebar: "))
print(f"Luas Persegi Panjang: {p * l}")
print(f"Keliling Persegi Panjang: {2 * (p + l)}\n")

# 3. Trapesium
a = float(input("Masukkan sisi atas: "))
b = float(input("Masukkan sisi bawah: "))
t = float(input("Masukkan tinggi: "))
sm = float(input("Masukkan sisi miring: "))
print(f"Luas Trapesium: {0.5 * (a + b) * t}")
print(f"Keliling Trapesium: {a + b + (2 * sm)}")