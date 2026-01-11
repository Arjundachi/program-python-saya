Tahun = int(input("Masukan tahun:"))
if (Tahun %  4==0 and Tahun % 100 !=0) or (Tahun % 400 ==0):
    print(Tahun,"Adalah tahun kabisat")
else:
    print(Tahun,"Bukan tahun kabisat donk")   