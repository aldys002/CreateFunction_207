# nomor 1
def Temperatur (value, unit):
    if unit == 'C':  # Celsius ke Fahrenheit
        return (value * 9/5) + 32
    elif unit == 'F':  # Fahrenheit ke Celsius
        return (value - 32) * 5/9
    else:
        return "Satuan tidak valid! Gunakan 'C' untuk Celsius atau 'F' untuk Fahrenheit."


# Inputan
valueSuhu = float(input("Masukkan nilai suhu: "))
unitSuhu = input("Masukkan satuan suhu ('C' untuk Celsius, 'F' untuk Fahrenheit): ")

# hasil output
hasilSuhu = Temperatur(valueSuhu, unitSuhu)
print("Hasil konversi:", hasilSuhu)




luaslingkaran = lambda jarijari: 3.14 * jarijari ** 2

# Menerima input dari pengguna
jarijari = float(input("Masukkan jari-jari lingkaran: "))

# Menghitung dan menampilkan hasil luas
luas = luaslingkaran(jarijari)
print("Luas lingkaran dengan jari-jari", jarijari, "adalah:", luas)

