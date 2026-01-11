nama_barang = []
harga_barang = []
jumlah_barang = []

jumlah = int(input("Masukkan jumlah item: "))

for i in range(jumlah):
    print(f"\nItem ke-{i+1}")
    nama = input("Nama barang: ")
    harga = float(input("Harga: "))
    qty = int(input("Jumlah: "))

    nama_barang.append(nama)
    harga_barang.append(harga)
    jumlah_barang.append(qty)

# hitung total
total = 0
for i in range(jumlah):
    total += harga_barang[i] * jumlah_barang[i]

print("\n=== STRUK BELANJA ===")
for i in range(jumlah):
    print(f"{nama_barang[i]} x {jumlah_barang[i]} = {harga_barang[i] * jumlah_barang[i]}")

print(f"\nTotal belanja: {total}")

bayar = float(input("Uang bayar: "))
kembalian = bayar - total

print(f"Kembalian: {kembalian}")