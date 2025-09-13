# 1. Kamu sedang marathon TV series di netflix
#    1 episode berdurasi 35 min dengan total 10 episode
#    berapa jam kamu menonton TV series tersebut?

# ------------------------------------------------------------------------------------------------


# ------------------------------------------------------------------------------------------------

# 2. Kamu ingin membeli cupang dg harga 10rb dan koi dg harga 20rb
#    uang yg kamu bawa sebesar Rp.XXX000 (ganti XXX dg 3 angka terakhir NIM + 100)
#    kamu hanya beli 5 cupang dan 2 koi
#    berapa sisa uang kamu?

# ------------------------------------------------------------------------------------------------


# ------------------------------------------------------------------------------------------------

# # 3. Kamu ingin pergi liburan dg sepeda motor
#    total jarak perjalanan XXX KM (ganti XXX dg 3 angka terakhir NIM)
#    konsumsi BBM sepeda motor 2.7 KM per Liter
#    kapasitas tangki sepeda motor X Liter (ganti X dg 1 angka terakhir NIM)
#    harga bensin per liter Rp.1XXX0 (ganti XXX dg 3 angka terakhir NIM)
#    jika total bensin yg dibutuhkan > 3 liter, maka dapat diskon Rp.500 per liter
#    berapa total bensin yg dibutuhkan, harga bensin per liter setelah diskon (jika ada)- 
#    total biaya bensin, dan prakiraan berapa kali kamu harus mengisi bensin (dengan asumsi tangki penuh setiap kali isi)?
#    NB: HARUS PAKAI INPUT !!!!!

# ------------------------------------------------------------------------------------------------


# ------------------------------------------------------------------------------------------------




#                            😀 SELAMAT MENGERJAKAN !!!! 😀


durasi_per_episode = int(input("Masukkan durasi per episode (menit): "))   # contoh: 35
jumlah_episode = int(input("Masukkan jumlah episode: "))                   # contoh: 10

total_menit = durasi_per_episode * jumlah_episode
total_jam = total_menit // 60

print("\n1. Durasi menonton:", total_jam, "jam")
print("="*50)


harga_cupang = 10000
harga_koi = 20000

jumlah_cupang = int(input("\nMasukkan jumlah ikan cupang yang dibeli: "))   # contoh: 5
jumlah_koi = int(input("Masukkan jumlah ikan koi yang dibeli: "))           # contoh: 2
uang = int(input("Masukkan jumlah uang yang dibawa (Rp): "))           # contoh: 145000

total_belanja = (harga_cupang * jumlah_cupang) + (harga_koi * jumlah_koi)
sisa_uang = uang - total_belanja

print("\n2. Sisa uang yang tersisa adalah: Rp.", sisa_uang)
print("="*50)


jarak = float(input("\nMasukkan total jarak perjalanan (KM): "))           # contoh: 45
konsumsi_bbm = float(input("Masukkan konsumsi BBM (Liter/KM): "))          # contoh: 2.7
kapasitas_tangki = float(input("Masukkan kapasitas tangki (Liter): "))     # contoh: 5
harga_bensin = int(input("Masukkan harga bensin per liter (Rp): "))        # contoh: 10450

# Hitung total bensin yang dibutuhkan
total_bensin = jarak / konsumsi_bbm

# Cek diskon
if total_bensin > 3:
    harga_setelah_diskon = harga_bensin - 500
else:
    harga_setelah_diskon = harga_bensin

# Hitung total biaya bensin
total_biaya = total_bensin * harga_setelah_diskon

# Hitung berapa kali isi bensin (dibulatkan ke atas)
import math
jumlah_isi = math.ceil(total_bensin / kapasitas_tangki)

print("\n3. Hasil Perhitungan Liburan:")
print("Total bensin yang dibutuhkan: {:.2f} liter".format(total_bensin))
print("Harga bensin per liter setelah diskon: Rp.{}".format(harga_setelah_diskon))
print("Total biaya bensin: Rp.{:.0f}".format(total_biaya))
print("Prakiraan jumlah isi bensin: {} kali".format(jumlah_isi))
print("="*50)