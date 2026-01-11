#Sebelum menjalankan program variabel nilai_kelas_si harus diisi dulu dengan angka.setelah itu baru dijalankan
#len:menghitung jumlah data dalam variabel
#sum:menghitung jumlah nilai dalam variabel
#sum/len:menghitung rata-rata


# Simpan 5 nilai ujian
nilai = []

for i in range(5):
    n = float(input(f"Masukkan nilai ke-{i+1}: "))
    nilai.append(n)

# Hitung rata-rata
rata = sum(nilai) / len(nilai)

# Tentukan status
if rata >= 70:
    status = "Lulus"
else:
    status = "Tidak Lulus"

# Output
print("\n=== HASIL ===")
print("Nilai:", nilai)
print("Rata-rata:", rata)
print("Status:", status)

