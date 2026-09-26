# Simulasi Transaksi Pengisian BBM di SPBU
# Sesuaikan nama dan NIM dengan data diri Anda

NIM = "21" # Sesuaikan dengan 2 digit terakhir NIM Anda
nama = "meisya" # Sesuaikan dengan nama panggilan Anda

print("Selamat datang di SPBU!")
print()

input_nama = input("Masukkan nama panggilan Anda: ")

input_nim = input("Masukkan NIM Anda dua digit terakhir: ")

is_dua_digit_nim = len(input_nim) == 2 and input_nim.isdigit()
is_nama_lower = input_nama.lower() == nama.lower()
is_nim_valid = input_nim == NIM

if is_dua_digit_nim and is_nama_lower and is_nim_valid:
    print(f"Login berhasil! Selamat datang, {nama}")
    print() 
else:
    print("Login gagal! Nama atau NIM tidak valid.")
    exit()

print("===== PILIHAN JENIS BBM =====")
print("1. Pertalite (Rp 10.000/Liter)")
print("2. Pertamax (Rp 12.500/Liter)")
print("3. Pertamax Turbo (Rp 15.000/Liter)")

pilihan_bbm = int(input("Pilih jenis BBM (1-3): "))

if pilihan_bbm == 1:
    harga_per_liter = 10000
    jenis_bbm = "Pertalite"
elif pilihan_bbm == 2:
    harga_per_liter = 12500
    jenis_bbm = "Pertamax"
elif pilihan_bbm == 3:
    harga_per_liter = 15000
    jenis_bbm = "Pertamax Turbo"
else:
    
    print("Pilihan tidak valid. Silakan coba lagi.")
    exit()
if pilihan_bbm in [1, 2, 3]:
    jumlah_liter = float(input("Masukkan jumlah liter BBM yang ingin dibeli: "))
    if jumlah_liter <= 0:
        print("jumlah Liter harus lebih dari 0. Silakan coba lagi.  ")
    else:
        persen_diskon_liter = 0.0
        if jumlah_liter >= 10:
            persen_diskon_liter = 0.10
        elif jumlah_liter >= 5:
            persen_diskon_liter = 0.05
        else:
            persen_diskon_liter = 0.0

        is_member = input("Apakah Anda anggota SPBU? (ya/tidak): ")
        is_member = is_member.lower() == "ya"
        persen_diskon_member = 0.02 if is_member else 0.0

        total_harga = harga_per_liter * jumlah_liter
        diskon_liter = total_harga * persen_diskon_liter
        diskon_member = total_harga * persen_diskon_member
        total_diskon = diskon_liter + diskon_member
        total_bayar = total_harga - total_diskon

# --- Formating String untuk Struk Transaksi ---
        str_nama_nim = f"{nama} ({NIM})"
        str_harga_per_liter = f"Rp {harga_per_liter:,.2f}/liter"
        str_jumlah_liter = f"{jumlah_liter:.2f} liter"
        str_total_harga = f"Rp {total_harga:,.2f}"
        str_diskon_liter = f"Rp {diskon_liter:,.2f}"
        str_diskon_member = f"Rp {diskon_member:,.2f}"
        str_bayar = f"Rp {total_bayar:,.2f}"
        str_status_member = "Ya" if is_member else "Tidak"

# --- Cetak Struk Bentuk Tabel Manual ---
        print("=" *52)
        print("================= STRUK TRANSAKSI ==================")
        print("=" *52)
        print(f"| {'Nama & NIM':<18} | {str_nama_nim:<28} |")
        print(f"| {'Jenis BBM':<18} | {jenis_bbm:<28} |")
        print(f"| {'Harga per Liter':<18} | {str_harga_per_liter:<28} |")
        print(f"| {'Jumlah Liter':<18} | {str_jumlah_liter:<28} |")
        print("-" *52)
        print(f"| {'Total Harga':<18} | {str_total_harga:<28} |")
        print(f"| {'Diskon Liter':<18} | {str_diskon_liter:<28} |")
        print(f"| {'Diskon Member':<18} | {str_diskon_member:<28} |")
        print(f"| {'Status Member':<18} | {str_status_member:<28} |")
        print("-" *52)
        print(f"| {'Total Bayar':<18} | {str_bayar:<28} |")
        print("Terima kasih telah melakukan pengisian BBM di SPBU kami!")
        print("=" *52)