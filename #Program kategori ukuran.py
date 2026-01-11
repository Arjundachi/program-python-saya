Panjang=float(input("Masukan panjang:"))
lebar=float(input("Masukan lebar:"))
luas= Panjang * lebar 

if luas <50:
   kategori= "kecil"
elif 50  <= luas <= 100:
   kategori= "sedang"
else:
   kategori= "besar"

print("luas:",luas)
print("kategori:",kategori)
