# Fungsi lambda untuk menghitung luas lingkaran
luaslingkaran = lambda jarijari: 3.14 * jarijari ** 2

# Menerima input dari pengguna
jarijari = float(input("Masukkan jari-jari lingkaran: "))

# Menghitung dan menampilkan hasil luas
luas = luaslingkaran(jarijari)
print("Luas lingkaran dengan jari-jari", jarijari, "adalah:", luas)