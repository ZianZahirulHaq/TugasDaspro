#STUDI KASUS 1
nilai = int(input("Masukkan nilai anda: "))
if (nilai >= 90):
    print("Nilai anda A")
elif(nilai<90 and nilai >= 80):
    print("Nilai anda B")
elif(nilai < 80 and nilai > 70):
    print("Nilai anda C")
elif(nilai < 70):
    print("Nilai anda D")
elif(nilai < 60):
    print("Nilai anda E")

#STUDI KASUS 2
JenisKelamin = input("Pilih jenis kelamin anda (L/P): ")
umur = int(input("Umur anda: "))
TinggiBadan = int(input("Tinggi Badan anda: "))
Iq = int(input("IQ anda: "))


if (JenisKelamin == "L"):
    if(umur >= 18 and umur <=25 and TinggiBadan >= 175 and Iq >= 130):
        print("Selamat anda adalah orang yang dapat menjadi model catwalk")
    else:
        print("ANDA GAGAL MENJADI MODEL CATWALk")
elif(JenisKelamin == "P"):
    if(umur >= 18 and umur <= 25 and TinggiBadan >= 170 and Iq >= 130) :
        print("Selamat anda adalah orang yang dapat menjadi model catwalk")
    else:
        print("ANDA GAGAL MENJADI MODEL CATWALK")
else:
    print("TIDAK MEMENUHI SYARAT")

#STUDI KASUS 3
nama = input("Masukkan Nama Anda: ")
tugas = int(input("Masukkan Nilai Tugas Anda: "))
uts = int(input("Masukkan Nilai UTS: "))
uas = int(input("Masukkan nilai UAS anda: "))
RataRataNilai = (tugas+uts+uas)/3 
print(RataRataNilai)

if (RataRataNilai >= 70):
    if(tugas >= 60 and uts >= 60 and uas >= 60):
        print(f"Selamat {nama} anda LULUS tanpa remedial")
    else:
        print(f"{nama} Kamu LULUS dengan REMEDIAL")
elif(RataRataNilai < 70):
    if(RataRataNilai >= 50):
        print(f"{nama} Kamu TIDAK LULUS dan boleh remedial")
    else:
        print(f"{nama} Kamu TIDAK LULUS dan TIDAK BISA REMEDIAL")
else:
    print("DATA YANG DIMASUKKAN SALAH")



