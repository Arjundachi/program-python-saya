# Input data
nilai = []

jumlah = int(input("Masukkan jumlah nilai: "))

for i in range(jumlah):
    n = float(input(f"Nilai ke-{i+1}: "))
    nilai.append(n)

# Sorting dari yang terkecil ke terbesar
nilai.sort()

# Tampilkan dalam format ranking
print("\n=== RANKING NILAI ===")
rank = 1
for n in nilai:
    print(f"Rank {rank}: {n}")
    rank += 1