# ===== PROGRAM KASIR MODULAR =====

nama_barang = []
harga_barang = []
jumlah_barang = []

def input_barang():
    jumlah = int(input("Masukkan jumlah item: "))
    for i in range(jumlah):
        print(f"\nItem ke-{i+1}")
        nama = input("Nama barang: ")
        harga = float(input("Harga: "))
        qty = int(input("Jumlah: "))
        nama_barang.append(nama)
        harga_barang.append(harga)
        jumlah_barang.append(qty)

def hitung_total():
    total = 0
    for i in range(len(nama_barang)):
        total += harga_barang[i] * jumlah_barang[i]
    return total

def cetak_struk(total):
    print("\n======= STRUK BELANJA =======")
    for i in range(len(nama_barang)):
        subtotal = harga_barang[i] * jumlah_barang[i]
        print(f"{nama_barang[i]} x {jumlah_barang[i]} = {subtotal}")
    print(f"\nTotal belanja: {total}")
    bayar = float(input("Uang bayar: "))
    kembalian = bayar - total
    print(f"Kembalian: {kembalian}")
    print("==============================")

# Main Program
input_barang()
total = hitung_total()
cetak_struk(total)