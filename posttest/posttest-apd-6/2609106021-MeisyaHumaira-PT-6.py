import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

inventaris = {
    "CAM01": {"nama": "Canon EOS 80D", "kategori": "Kamera DSLR", "harga": 150000, "status": "Tersedia"},
    "CAM02": {"nama": "Sony A6400", "kategori": "Kamera Mirrorless", "harga": 175000, "status": "Dipinjam"},
    "LNS01": {"nama": "Sony FE 50mm", "kategori": "Lensa", "harga": 75000, "status": "Tersedia"}
}

peminjaman = {
    "REQ01": {"peminjam": "Budi", "id_alat": "CAM02", "status": "Disetujui"}
}

users = {
    "admin": {"sandi": "admin123", "role": "Admin"}
}

while True:
    print("=" * 45)
    print(" APLIKASI PEMINJAMAN & INVENTARIS KAMERA ")
    print("=" * 45)
    print("1. Masuk sebagai Admin")
    print("2. Masuk sebagai Anggota")
    print("3. Register Akun Anggota Baru")
    print("4. Keluar Program")
    
    pilihan_awal = input("Silahkan pilih menu (1-4): ")

    if pilihan_awal == "1":
        clear_screen()
        print("--- LOGIN ADMIN ---")
        sandi = input("Masukkan Sandi Admin (ketik: admin123): ")
        if sandi == users["admin"]["sandi"]:
            while True:
                print("\n--- MENU UTAMA ADMIN ---")
                print("1. Lihat Semua Data Inventaris")
                print("2. Tambah Alat Kamera Baru")
                print("3. Ubah Status Alat")
                print("4. Hapus Data Alat Rusak")
                print("5. Kelola Persetujuan Peminjaman")
                print("6. Kembali ke Menu Utama")

                menu_admin = input("Pilih menu admin (1-6): ")

                if menu_admin == "1":
                    clear_screen()
                    print("\n--- DAFTAR INVENTARIS KAMERA ---")
                    print("ID     | Nama Alat          | Kategori     | Harga/Hari | Status")
                    print("-" * 65)
                    for id_alat, info in inventaris.items():
                        print(f"{id_alat} | {info['nama']:<18} | {info['kategori']:<12} | Rp{info['harga']:<8} | {info['status']}")

                elif menu_admin == "2":
                    clear_screen()
                    print("\n--- TAMBAH ALAT BARU ---")
                    id_baru = input("Masukkan ID Alat baru (Contoh: CAM03): ")
                    
                    if id_baru in inventaris:
                        print("Gagal! ID Alat sudah terdaftar di sistem.")
                    else:
                        nama = input("Masukkan Nama Alat: ")
                        kategori = input("Masukkan Kategori (Kamera/Lensa): ")
                        
                        harga_input = input("Masukkan Harga Sewa per Hari (angka): ")
                        if harga_input.isdigit():
                            harga = int(harga_input)
                            inventaris[id_baru] = {
                                "nama": nama,
                                "kategori": kategori,
                                "harga": harga,
                                "status": "Tersedia"
                            }
                            print("Berhasil! Alat kamera baru sudah ditambahkan.")
                        else:
                            print("Gagal! Harga sewa harus berupa angka.")

                elif menu_admin == "3":
                    clear_screen()
                    print("\n--- UBAH STATUS ALAT ---")
                    for id_alat, info in inventaris.items():
                        print(f"{id_alat} - {info['nama']} (Status saat ini: {info['status']})")
                    
                    id_cari = input("Masukkan ID Alat yang ingin diubah statusnya: ")

                    if id_cari in inventaris:
                        print("Pilihan Status:")
                        print("1. Tersedia")
                        print("2. Dipinjam")
                        print("3. Rusak")
                        pilih_status = input("Pilih nomor status baru (1-3): ")

                        if pilih_status == "1":
                            inventaris[id_cari]["status"] = "Tersedia"
                            print("Berhasil! Status alat telah diperbarui menjadi Tersedia.")
                        elif pilih_status == "2":
                            inventaris[id_cari]["status"] = "Dipinjam"
                            print("Berhasil! Status alat telah diperbarui menjadi Dipinjam.")
                        elif pilih_status == "3":
                            inventaris[id_cari]["status"] = "Rusak"
                            print("Berhasil! Status alat telah diperbarui menjadi Rusak.")
                        else:
                            print("Pilihan status tidak valid! Gagal memperbarui status.")
                    else:
                        print("Maaf, ID Alat tidak ditemukan.")

                elif menu_admin == "4":
                    clear_screen()
                    print("\n--- HAPUS DATA ALAT RUSAK ---")
                    for id_alat, info in inventaris.items():
                        print(f"{id_alat} - {info['nama']} (Status: {info['status']})")
                        
                    id_hapus = input("Masukkan ID Alat yang ingin dihapus dari sistem: ")
                    
                    if id_hapus in inventaris:
                        if inventaris[id_hapus]["status"] == "Rusak":
                            del inventaris[id_hapus]
                            print("Berhasil! Data alat yang rusak telah dihapus.")
                        else:
                            print(f"Gagal menghapus! Alat ini berstatus '{inventaris[id_hapus]['status']}'. Hanya alat dengan status 'Rusak' yang dapat dihapus.")
                    else:
                        print("Maaf, ID Alat tidak ditemukan.")

                elif menu_admin == "5":
                    clear_screen()
                    print("\n--- DAFTAR PERMINTAAN PEMINJAMAN ---")
                    for id_req, req in peminjaman.items():
                        print(f"ID Req: {id_req} | Peminjam: {req['peminjam']} | ID Alat: {req['id_alat']} | Status: {req['status']}")    

                    id_req = input("Masukkan ID Request yang ingin diproses: ")
                    
                    if id_req in peminjaman:
                        status_baru = input("Ubah status (Ketik: Disetujui / Ditolak): ")
                        if status_baru in ["Disetujui", "Ditolak"]:
                            peminjaman[id_req]["status"] = status_baru
                            if status_baru == "Disetujui":
                                alat_id = peminjaman[id_req]["id_alat"]
                                if alat_id in inventaris:
                                    inventaris[alat_id]["status"] = "Dipinjam"
                            print("Berhasil! Status peminjaman telah diperbarui.")
                        else:
                            print("Status tidak valid! Ketik 'Disetujui' atau 'Ditolak'.")
                    else:
                        print("Maaf, ID Request tidak ditemukan.")
                        
                elif menu_admin == "6":
                    clear_screen()
                    break
                else:
                    print("Pilihan tidak ada, silakan masukkan angka 1 sampai 6.")
        else:
            print("Sandi admin salah! Silakan coba lagi.")

    elif pilihan_awal == "2":
        clear_screen()
        print("\n--- LOGIN ANGGOTA ---")
        username = input("Masukkan Username/Nama Anda: ")
        sandi_user = input("Masukkan Sandi Anda: ")

        if username in users and users[username]["sandi"] == sandi_user and users[username]["role"] == "Anggota":
            while True:
                print(f"\n--- MENU PENGGUNA (Halo, {username}) ---")
                print("1. Lihat Katalog Alat yang Tersedia")
                print("2. Ajukan Peminjaman Alat")
                print("3. Cek Status Riwayat Peminjaman Saya")
                print("4. Kembali ke Menu Utama")
                
                pilih_pengguna = input("Pilih menu (1-4): ")

                if pilih_pengguna == "1":
                    clear_screen()
                    print("\n--- KATALOG KAMERA TERSEDIA ---")
                    ada_alat = False
                    for id_alat, info in inventaris.items():
                        if info["status"] == "Tersedia":
                            print(f"{id_alat} | {info['nama']} | {info['kategori']} | Rp{info['harga']}/hari")
                            ada_alat = True
                    if not ada_alat:
                        print("Belum ada alat yang tersedia saat ini.")

                elif pilih_pengguna == "2":
                    clear_screen()
                    print("\n--- FORM PENGAJUAN PEMINJAMAN ---")
                    for id_alat, info in inventaris.items():
                        if info["status"] == "Tersedia":
                            print(f"{id_alat} | {info['nama']} | Rp{info['harga']}")
                    
                    id_pilih = input("Masukkan ID Alat yang ingin dipinjam: ")

                    if id_pilih in inventaris and inventaris[id_pilih]["status"] == "Tersedia":
                        id_req_baru = "REQ0" + str(len(peminjaman) + 1)
                        peminjaman[id_req_baru] = {
                            "peminjam": username,
                            "id_alat": id_pilih,
                            "status": "Pending (Menunggu Admin)"
                        }
                        print("Berhasil mengajukan peminjaman! Kode Request kamu:", id_req_baru)
                    else:
                        print("Maaf, ID Alat tidak valid atau sedang tidak tersedia.")

                elif pilih_pengguna == "3":
                    clear_screen()
                    print(f"\n--- RIWAYAT PEMINJAMAN: {username} ---")
                    punya_riwayat = False
                    for id_req, req in peminjaman.items():
                        if req["peminjam"] == username:
                            print(f"ID Req: {id_req} | Alat ID: {req['id_alat']} | Status: {req['status']}")
                            punya_riwayat = True
                    if not punya_riwayat:
                        print("Kamu belum memiliki riwayat peminjaman.")
                        
                elif pilih_pengguna == "4":
                    clear_screen()
                    break
                else:
                    print("Pilihan tidak valid, silakan pilih 1 sampai 4.")
        else:
            print("Login gagal! Username atau sandi salah, atau akun belum terdaftar sebagai anggota.")

    elif pilihan_awal == "3":
        clear_screen()
        print("\n--- REGISTER AKUN ANGGOTA BARU ---")
        reg_user = input("Buat Username Baru: ")
        if reg_user in users or reg_user == "":
            print("Username sudah digunakan atau tidak boleh kosong. Silakan coba lagi.")
        else:
            reg_sandi = input("Buat Sandi Baru: ")
            users[reg_user] = {
                "sandi": reg_sandi,
                "role": "Anggota"
            }
            print("Registrasi berhasil! Silakan masuk melalui menu login Anggota.")

    elif pilihan_awal == "4":
        print("\nTerima kasih telah menggunakan program ini. Program selesai!")
        break
    else:
        print("Pilihan tidak valid. Silakan masukkan angka 1 sampai 4.")