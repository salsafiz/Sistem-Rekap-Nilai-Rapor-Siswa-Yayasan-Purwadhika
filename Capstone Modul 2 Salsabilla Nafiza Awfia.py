#========================================================== Defining Variabel ==========================================================
from tabulate import tabulate
separator = "="*100
listdataSiswa = []
tableData = []
listJenjang = ["SD", "SMP", "SMA"]
jenjang = ""
kelasMin = 0
kelasMax = 0
#========================================================== Fungsi Jenjang ==========================================================
def jenjangSekolah():
    global jenjang, kelasMin, kelasMax
    while True:
        print(f"{separator}\n               Sistem Rekap Nilai Rapor Siswa Yayasan Sekolah Purwadhika BSD City\n{separator}")
        print("Pilihan role guru untuk menginput nilai siswa:")
        print("1. Guru SD Purwadhika BSD City")
        print("2. Guru SMP Purwadhika BSD City")
        print("3. Guru SMA Purwadhika BSD City")
        print(f"4. Keluar\n{separator}")
        pilihan = input("Masukkan menu: ")
        if pilihan == "1":
            jenjang = "SD"
            kelasMin = 1
            kelasMax = 6
            break
        elif pilihan == "2":
            jenjang = "SMP"
            kelasMin = 7
            kelasMax = 9
            break
        elif pilihan == "3":
            jenjang = "SMA"
            kelasMin = 10
            kelasMax = 12
            break
        elif pilihan == "4":
            exit()
        else:
            print("Masukkan angka yang benar!")
#========================================================== Fungsi Tampil Menu ==========================================================done
def menu():
    print(f"{separator}\n               Rekap Nilai Rapor Siswa Yayasan Sekolah {jenjang} Purwadhika BSD CITY\n{separator}")
    print(f"1. Tambah Data Siswa\n2. Tampilkan Data Siswa\n3. Update Data\n4. Hapus Data\n5. Statistik Nilai\n6. Berpindah Jenjang\n7. Exit\n{separator}")
#========================================================== Fungsi Input Nilai ==========================================================done
# bisa input nilai desimal dipisahkan dengan titik
def inputNilai(jenisNilai):                         #Tugas atau UTS atau UAS
    while True:
        nilai = input(f"Masukkan Nilai {jenisNilai}: ")
        if nilai.isnumeric():                                       #jika nilai bukan numeric maka akan input ulang untuk menghindari typo
            nilai = int(nilai)
            if nilai >= 1 and nilai <= 100:
                return nilai
        print("Nilai hanya boleh diisi angka bulat 1 sampai 100!")
#========================================================== Fungsi Hitung Kelulusan ==========================================================done
def hitungNilai(nilaiTugas, nilaiUTS, nilaiUAS):
    nilaiAkhir = (0.3 * nilaiTugas) + (0.3 * nilaiUTS) + (0.4 * nilaiUAS)
    return round(nilaiAkhir, 2)                 #agar desimal tetap rapi
#========================================================== Fungsi Kasih ABCDE ==========================================================done
def predikatNilai(nilaiAkhir):
    if nilaiAkhir >= 90:
        return "A"
    elif nilaiAkhir >= 80:
        return "B"
    elif nilaiAkhir >= 70:
        return "C"
    elif nilaiAkhir >= 60:
        return "D"
    else:
        return "E"
#========================================================== Fungsi Lulus ==========================================================done
def statusKelulusan(nilaiAkhir):
    if nilaiAkhir >= 75:
        return "Lulus"
    else:
        return "Tidak Lulus"
#========================================================== Fungsi Create ==========================================================done
def createData():
    global inputNama
    print(f"\nTambah Data Siswa\n{separator}")
    while True:
            inputNama = input(f"Masukkan Nama Siswa {jenjang}: ").title()
            if inputNama.isalpha():
                break
            print(f"Nama tidak boleh mengandung unsur selain alphabet!")
    while True:
        inputKelas = input(f"Masukkan Kelas ({kelasMin}-{kelasMax}) : ")
        if inputKelas.isnumeric():
            inputKelas = int(inputKelas)
            if kelasMin <= inputKelas <= kelasMax:
                break
        print(f"Kelas {jenjang} hanya boleh diisi angka {kelasMin} sampai {kelasMax}!")
    nilaiTugas = inputNilai("Tugas")                                # variabel sementara untuk simpan nilai yang didapat dari fungsi inputNilai
    nilaiUTS = inputNilai("UTS")                                    # variabel sementara untuk simpan nilai yang didapat dari fungsi inputNilai
    nilaiUAS = inputNilai("UAS")                                    # variabel sementara untuk simpan nilai yang didapat dari fungsi inputNilai
    nilaiAkhir = hitungNilai(nilaiTugas, nilaiUTS, nilaiUAS)        # variabel sementara untuk simpan nilai akhir yang didapat dari fungsi hitungNilai
    predikat = predikatNilai(nilaiAkhir)                            # variabel sementara untuk simpan nilai yang didapat dari fungsi predikatNilai
    status = statusKelulusan(nilaiAkhir)                            # variabel sementara untuk simpan nilai yang didapat dari fungsi statusKelulusan
    listdataSiswa.append([jenjang,inputNama, inputKelas, nilaiTugas, nilaiUTS, nilaiUAS, nilaiAkhir, predikat, status])
    print(f"\nData Siswa {jenjang} bernama {inputNama} berhasil ditambahkan!")
#========================================================== Fungsi Read ==========================================================
def readData():
    tableData = []
    if len(listdataSiswa) == 0:
        print("\nBelum ada data siswa.")
    for i in range(len(listdataSiswa)):                         #looping index 0-8 berisi jenjang,nama,kelas,tugas,uts,uas,nilaiakhir,predikat,kelulusan
        tableData.append([i + 1] + listdataSiswa[i])
    print()
    print(tabulate(tableData,
            headers=["No","Jenjang","Nama","Kelas","Tugas","UTS","UAS","Nilai Akhir","Predikat","Status"],
            tablefmt="rounded_grid"))                           #ujung sudut melengkung
#========================================================== Fungsi Update ==========================================================
def updateData():
    if len(listdataSiswa) == 0:
        print("\nBelum ada data siswa.")
        return 0                                                # agar tidak memunculkan tabel kosong
    readData()                                                  # kalau ada data di dalam tabel lgsg tampilkan read data
    nomorData = int(input("\nMasukkan nomor data yang ingin diupdate : "))
    if nomorData < 1 or nomorData > len(listdataSiswa):
        print("Nomor tidak ditemukan.")
        return 0
    index = nomorData-1
    print("\nMasukkan data baru")
    while True:
        inputNama = input("Masukkan Nama Siswa: ").title()
        if inputNama.isalpha():
            break
        print(f"Nama tidak boleh mengandung unsur selain alphabet!")
    while True:
        inputKelas = input("Masukkan Kelas : ")
        if inputKelas.isnumeric():
            inputKelas = int(inputKelas)
            if kelasMin <= inputKelas <= kelasMax:
                break
        print(f"Kelas hanya boleh diisi angka!")
    nilaiTugas = inputNilai("Tugas")
    nilaiUTS = inputNilai("UTS")
    nilaiUAS = inputNilai("UAS")
    nilaiAkhir = hitungNilai(nilaiTugas, nilaiUTS, nilaiUAS)
    predikat = predikatNilai(nilaiAkhir)
    status = statusKelulusan(nilaiAkhir)
    listdataSiswa[index] = [jenjang, inputNama, inputKelas, nilaiTugas, nilaiUTS, nilaiUAS, nilaiAkhir, predikat, status]
    print("\nData siswa berhasil diupdate!")
#========================================================== Fungsi Delete ==========================================================
def deleteData():
    if len(listdataSiswa) == 0:
        print("\nBelum ada data siswa.")
        return 0
    readData()
    nomorData = int(input("\nMasukkan nomor data yang ingin dihapus : "))
    if nomorData < 1 or nomorData > len(listdataSiswa):
        print("Nomor tidak ditemukan.")
        return 0
    listdataSiswa.pop(nomorData-1)
    print("\nData berhasil dihapus!")
#========================================================== Fungsi Statistik ==========================================================
def statistikData():
    if len(listdataSiswa) == 0:
        print("\nBelum ada data siswa.")
        return 0
    for j in range(len(listJenjang)):
        jenjangSekarang = listJenjang[j]
        jumlahSiswa = 0                         #redefining untuk reset nilai agar tidak mencampur 3 jenjang
        jumlahNilai = 0
        jumlahLulus = 0
        jumlahTidakLulus = 0
        nilaiTertinggi = None
        nilaiTerendah = None
        namaNilaiTertinggi = ""
        namaNilaiTerendah = ""
        for i in range(len(listdataSiswa)):
            if listdataSiswa[i][0] == jenjangSekarang:
                jumlahSiswa += 1
                jumlahNilai += listdataSiswa[i][6]
                if listdataSiswa[i][8] == "Lulus":
                    jumlahLulus += 1
                else:
                    jumlahTidakLulus += 1
                if nilaiTertinggi == None:
                    nilaiTertinggi = listdataSiswa[i][6]
                    nilaiTerendah = listdataSiswa[i][6]
                    namaNilaiTertinggi = listdataSiswa[i][1]
                    namaNilaiTerendah = listdataSiswa[i][1]
                if listdataSiswa[i][6] > nilaiTertinggi:
                    nilaiTertinggi = listdataSiswa[i][6]
                    namaNilaiTertinggi = listdataSiswa[i][1]
                if listdataSiswa[i][6] < nilaiTerendah:
                    nilaiTerendah = listdataSiswa[i][6]
                    namaNilaiTerendah = listdataSiswa[i][1]
        print("="*50)
        print(f"STATISTIK {jenjangSekarang}")
        print("="*50)
        if jumlahSiswa==0:
            print(f"Belum ada data siswa jenjang {jenjangSekarang}.")
        else:
            rerata = jumlahNilai/jumlahSiswa
            tableStatistik = [
                ["Jumlah Siswa", jumlahSiswa],
                ["Rata-rata Nilai", round(rerata, 2)],
                ["Jumlah Lulus", jumlahLulus],
                ["Jumlah Tidak Lulus", jumlahTidakLulus],
                ["Nilai Tertinggi", nilaiTertinggi],
                ["Nama Nilai Tertinggi", namaNilaiTertinggi],
                ["Nilai Terendah", nilaiTerendah],
                ["Nama Nilai Terendah", namaNilaiTerendah]]
            print(tabulate(tableStatistik, 
                           headers=["Informasi", "Hasil"], 
                           tablefmt="rounded_grid"))
#========================================================== Main Program ==========================================================
while True:
    jenjangSekolah()
    while True:
        menu()
        pilihanMenu = input("Masukkan pilihan menu: ")
        if pilihanMenu == "1":
            createData()
        elif pilihanMenu == "2":
            readData()
        elif pilihanMenu == "3":
            updateData()
        elif pilihanMenu == "4":
            deleteData()
        elif pilihanMenu == "5":
            statistikData()
        elif pilihanMenu == '6':
            print(f"\nKeluar dari Role Guru {jenjang}")
            break
        elif pilihanMenu == "7":
            print("\nTerima kasih selamat liburan!")
            exit()
        else:
            print("\nMenu tidak tersedia.")
