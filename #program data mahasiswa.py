# Input data mahasiswa
mahasiswa = []

jumlah = int(input("Masukkan jumlah mahasiswa: "))

for i in range(jumlah):
    nama = input(f"Nama mahasiswa ke-{i+1}: ")
    nilai = float(input("Nilai: "))
    mahasiswa.append((nama, nilai))
    print()

# Filter & tampilkan yang lulus
print("\n=== DAFTAR MAHASISWA LULUS ===")
for nama, nilai in mahasiswa:
    if nilai >= 60:
        # Tentukan predikat
        if nilai >= 85:
            predikat = "A"
        elif nilai >= 75:
            predikat = "B"
        elif nilai >= 60:
            predikat = "C"

        print(f"{nama} - Nilai: {nilai} - Predikat: {predikat}")