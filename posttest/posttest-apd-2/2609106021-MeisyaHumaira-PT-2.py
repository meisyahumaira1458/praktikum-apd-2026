list_bagasi = [12, 18, 7, 15, 20, 10]
total_berat_awal = list_bagasi[0] + list_bagasi[1] + list_bagasi[2] + list_bagasi[3] + list_bagasi[4] + list_bagasi[5]
total_berat_akhir = total_berat_awal + (total_berat_awal * 0.05)
rata_rata = total_berat_akhir / len(list_bagasi)
nim = 21
bolean = nim < rata_rata
posisi_tengah = list_bagasi[2:5]
total_berat_gram = total_berat_akhir * 1000
print("data bagasi (list):", list_bagasi)
print("total berat awal (kg):", total_berat_awal)
print("total berat akhir (kg):", total_berat_akhir)
print("rata-rata berat (kg):", rata_rata)
print("2 digit nim:", nim)
print("status bolean (nim < rata-rata):", bolean)
print("data posisi tengah (indeks 2-4):", posisi_tengah)
print("total berat akhir (gram):", total_berat_gram)
