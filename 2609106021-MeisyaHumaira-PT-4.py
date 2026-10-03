username_benar = "meisya"
password_benar = "021"

kesempatan = 3
login_berhasil = False

print("=== SYSTEM LOGIN PENGAJAR ===")
while kesempatan > 0 and not login_berhasil:
    username_input = input("Masukkan username (Nama Panggilan): ")
    password_input = input("Masukkan password (3 Digit NIM terakhir): ")

    if username_input == username_benar and password_input == password_benar:
        print("Login berhasil! Selamat datang, Meisya!")
        login_berhasil = True
    else:
        kesempatan -= 1
        print(f"Username atau password salah. Kesempatan tersisa: {kesempatan}")
        
if not login_berhasil:
    print("Login gagal. Silakan coba lagi nanti.")
    exit()

list_data_siswa = []
lanjut_input = "ya"

while lanjut_input.lower() == "ya":
        print("\n=== INPUT DATA SISWA ===")
        nama_siswa = input("Masukkan nama siswa: ") 
        kelas_siswa = input("Masukkan kelas siswa: ")

        status_ujian = input("Apakah siswa mengikuti ujian? (ya/tidak): ")

        if status_ujian.lower() == "ya":
            status_text = "Mengikuti Ujian"

            while True:
                benar = int(input("Masukkan jumlah soal benar (0-20): "))
                if 0 <= benar <= 20:
                    break
                else:
                    print("Jumlah soal benar harus antara 0 hingga 20. Silakan coba lagi.")

            salah = 20 - benar
            nilai = benar * 5
        else:
            status_text = "Tidak Mengikuti Ujian"
            nilai = 0

        if nilai >= 80:
            kategori_nilai = "Sangat Baik"
        elif nilai >= 60:
            kategori_nilai = "Baik"
        elif nilai >= 40:
            kategori_nilai = "Cukup"
        else:
            kategori_nilai = "Perlu belajar lagi ya!"

        data_siswa = {
            "Nama": nama_siswa,
            "Kelas": kelas_siswa,
            "Status Ujian": status_text,
            "Nilai": nilai,
            "Kategori Nilai": kategori_nilai
        }
        list_data_siswa.append(data_siswa)
        print()
        lanjut_input = input("Apakah Anda ingin memasukkan data siswa lain? (ya/tidak): ")
        print("="*40)

print("\n" +"="*40)
print("REKAP NILAI SISWA")
print("="*40)

daftar_kelas = []
for data in list_data_siswa:
    if data["Kelas"] not in daftar_kelas:
        daftar_kelas.append(data["Kelas"])
for kelas in daftar_kelas:
    print(f"\nKelas: {kelas}")
    print("-"*40)

    no = 1
    for data in list_data_siswa:
        if data["Kelas"] == kelas:
            print(f"{no}. Nama: {data['Nama']}, Status Ujian: {data['Status Ujian']}, Nilai: {data['Nilai']}, Kategori Nilai: {data['Kategori Nilai']}")
            no += 1