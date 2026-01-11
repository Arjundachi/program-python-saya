Nilai=float(input("Masukan nilai mahasiswa:"))
if Nilai >= 90 and Nilai <=100:
    Grade="A"
    keterangan="lulus dengan nilai terbaik dan ayah mu pasti bangga dengan mu"
elif Nilai >= 80 and Nilai <= 90:
     Grade="B"
     keterangan="lulus tapi harus lebih semangat lagi jangan malas"
elif Nilai >= 70 and Nilai <=80:
     Grade="C"
     keterangan="lulus tapi kurang belajarnya" 
elif Nilai >= 60 and Nilai <= 70:
     Grade="D"
     keterangan="tidak lulus dan payah sekali"
else:
     Grade="E"
     keterangan="fiks suka main judi online ini dan sangat memalukkan"         

   
print("Grade:",Grade)    
print("keterangan:",keterangan)
