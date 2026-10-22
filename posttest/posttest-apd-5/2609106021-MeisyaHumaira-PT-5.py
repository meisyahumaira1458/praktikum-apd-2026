import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

inventaris = [
    ["CAM01", "Canon EOS 80D", "Kamera DSLR", 150000, "Tersedia"],
    ["CAM02", "Sony A6400", "Kamera Mirrorless", 175000, "Dipinjam"],
    ["LNS01", "Sony FE 50mm", "Lensa", 75000, "Tersedia"]
]

peminjaman = [
    ["REQ01", "Budi", "CAM02", "Disetujui"]
]

LOGIN = ("Admin", "Pengguna")

while True:
    print("APLIKASI PEMINJAMAN & INVENTARIS KAMERA")
    print("1. Masuk sebagai Admin")
    print("2. Masuk sebagai Anggota")
    print("3. Keluar Program")

    pilihan_awal = input("Silahkan pilih menu (1-3): ")

    if pilihan_awal == "1":
        sandi = input("Masukkan Sandi Admin (ketik: admin123): ")
        if sandi == "admin123":
            while True:
                print("\n--- MENU UTAMA ADMIN ---")
                print("1. Lihat Semua Data Inventaris ")
                print("2. Tambah Alat Kamera Baru ")
                print("3. Ubah Status Alat ")
                print("4. Hapus Data Alat Rusak ")
                print("5. Kelola Persetujuan Peminjaman")
                print("6. Kembali ke Menu Utama")

                menu_admin = input("Pilih menu admin (1-6): ")

                if menu_admin == "1":
                    print("\n--- DAFTAR INVENTARIS KAMERA ---")
                    print("ID   | Nama Alat          | Kategori     | Harga/Hari | Status")
                    print("-" * 60)
                    for item in inventaris:
                        print(item[0], " | ", item[1], " | ", item[2], " | Rp", item[3], " | ", item[4])

                elif menu_admin == "2":
                    print("\n--- TAMBAH ALAT BARU ---")
                    id_baru = input("Masukkan ID Alat baru (Contoh: CAM03): ")
                    nama = input("Masukkan Nama Alat: ")
                    kategori = input("Masukkan Kategori (Kamera/Lensa): ")
                    harga = int(input("Masukkan Harga Sewa per Hari (angka): "))
                    status_awal = "Tersedia"

                    inventaris.append([id_baru, nama, kategori, harga, status_awal])
                    print("Berhasil! Alat kamera baru sudah ditambahkan.")

                elif menu_admin == "3":
                    print("\n--- UBAH STATUS ALAT ---")
                    for item in inventaris:
                        print(item[0], "-", item[1], "(Status saat ini:", item[4], ")")
                    
                    id_cari = input("Masukkan ID Alat yang ingin diubah statusnya: ")

                    ketemu = False
                    for item in inventaris:
                        if item[0] == id_cari:
                            ketemu = True
                            print("Pilihan Status:")
                            print("1. Tersedia")
                            print("2. Dipinjam")
                            print("3. Rusak")
                            pilih_status = input("Pilih nomor status baru (1-3): ")

                            if pilih_status == "1":
                                item[4] = "Tersedia"
                                print("Berhasil! Status alat telah diperbarui menjadi Tersedia.")
                            elif pilih_status == "2":
                                item[4] = "Dipinjam"
                                print("Berhasil! Status alat telah diperbarui menjadi Dipinjam.")
                            elif pilih_status == "3":
                                item[4] = "Rusak"
                                print("Berhasil! Status alat telah diperbarui menjadi Rusak.")
                            else:
                                print("Pilihan status tidak valid! Gagal memperbarui status.")
                            break
                            
                    if not ketemu:
                        print("Maaf, ID Alat tidak ditemukan.")

                elif menu_admin == "4":
                    print("\n--- HAPUS DATA ALAT RUSAK ---")
                    for item in inventaris:
                        print(item[0], "-", item[1], "(Status:", item[4], ")")
                        
                    id_hapus = input("Masukkan ID Alat yang ingin dihapus dari sistem: ")
                    
                    ketemu = False
                    for i in range(len(inventaris)):
                        if inventaris[i][0] == id_hapus:
                            ketemu = True
                            
                            if inventaris[i][4] == "Rusak":
                                del inventaris[i]
                                print("Berhasil! Data alat yang rusak telah dihapus.")
                            else:
                                print(f"Gagal menghapus! Alat ini berstatus '{inventaris[i][4]}'. Hanya alat dengan status 'Rusak' yang dapat dihapus.")
                            break

                    if not ketemu:
                        print("Maaf, ID Alat tidak ditemukan.")
                elif menu_admin == "5":
                    print("\n--- DAFTAR PERMINTAAN PEMINJAMAN ---")
                    for req in peminjaman:
                        print("ID Req:", req[0], "| Peminjam:", req[1], "| ID Alat:", req[2], "| Status:", req[3])     

                    id_req = input("Masukkan ID Request yang ingin diproses: ")
                    
                    ketemu_req = False
                    for req in peminjaman:
                        if req[0] == id_req:
                            ketemu_req = True
                            status_baru = input("Ubah status (Ketik: Disetujui / Ditolak): ")
                            req[3] = status_baru

                            if status_baru == "Disetujui":
                                for item in inventaris:
                                    if item[0] == req[2]:
                                        item[4] = "Dipinjam"
                                        
                            print("Berhasil! Status peminjaman telah diperbarui.")
                            
                    if not ketemu_req:
                        print("Maaf, ID Request tidak ditemukan.")
                        
                elif menu_admin == "6":
                    break
                else:
                    print("Pilihan tidak ada, silakan masukkan angka 1 sampai 6.")
        else:
            print("Sandi admin salah! Silakan coba lagi.")

    elif pilihan_awal == "2":
        nama_user = input("\nMasukkan Nama Lengkap Anda: ")
        
        while True:
            print(f"\n--- MENU PENGGUNA (Halo, {nama_user}) ---")
            print("1. Lihat Katalog Alat yang Tersedia")
            print("2. Ajukan Peminjaman Alat")
            print("3. Cek Status Riwayat Peminjaman Saya")
            print("4. Kembali ke Menu Utama")
            
            pilih_pengguna = input("Pilih menu (1-4): ")

            if pilih_pengguna == "1":
                print("\n--- KATALOG KAMERA TERSEDIA ---")
                ada_alat = False
                for item in inventaris:
                    if item[4] == "Tersedia":
                        print(item[0], " | ", item[1], " | ", item[2], " | Rp", item[3], "/hari")
                        ada_alat = True
                if not ada_alat:
                    print("Belum ada alat yang tersedia saat ini.")

            elif pilih_pengguna == "2":
                print("\n--- FORM PENGAJUAN PEMINJAMAN ---")
                for item in inventaris:
                    if item[4] == "Tersedia":
                        print(item[0], " | ", item[1], " | Rp", item[3])
                id_pilih = input("Masukkan ID Alat yang ingin dipinjam: ")

                valid = False
                for item in inventaris:
                    if item[0] == id_pilih and item[4] == "Tersedia":
                        valid = True
                        break
                        
                if valid:
                    id_req_baru = "REQ0" + str(len(peminjaman) + 1)
                    peminjaman.append([id_req_baru, nama_user, id_pilih, "Pending (Menunggu Admin)"])
                    print("Berhasil mengajukan peminjaman! Kode Request kamu:", id_req_baru)
                else:
                    print("Maaf, ID Alat tidak valid atau sedang tidak tersedia.")

            elif pilih_pengguna == "3":
                print(f"\n--- RIWAYAT PEMINJAMAN: {nama_user} ---")
                punya_riwayat = False
                for req in peminjaman:
                    if req[1] == nama_user:
                        print("ID Req:", req[0], "| Alat ID:", req[2], "| Status:", req[3])
                        punya_riwayat = True
                if not punya_riwayat:
                    print("Kamu belum memiliki riwayat peminjaman.")
                    
            elif pilih_pengguna == "4":
                break
            else:
                print("Pilihan tidak valid, silakan pilih 1 sampai 4.")
                
    elif pilihan_awal == "3":
        print("\nTerima kasih telah menggunakan program ini. Program selesai!")
        break
    else:
        print("Pilihan tidak valid. Silakan masukkan angka 1, 2, atau 3.")