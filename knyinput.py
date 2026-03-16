import numpy as np
import pandas as pd

print("--- Demon Slayer Team ---")
print("Setiap tim terdiri dari 3 anggota.")
print("Silakan masukkan data anggota tim\n")

nama_list = []
rank_list = []
power_list = []
ranks_list = ["Mizunoto", "Mizunoe", "Kanoto", "Kanoe", "Tsuchinoto", "Tsuchinoe", "Hinoto", "Hinoe", "Kinoto", "Kinoe", "Hashira"]

for i in range(3):
    print(f"Anggota ke-{i+1}:")
    nama = input("Nama: ")
    print(f"Rank: {ranks_list}")
    rank = input("Input Rank: ").title()
    while rank not in ranks_list and "Hashira" not in rank:
        print("Rank tidak valid! Silakan pilih dari daftar atau masukkan gelar Hashira spesifik.")
        rank = input(f"Input rank: ").title()
    power = int(input("Power (1-100): "))
    
    nama_list.append(nama)
    rank_list.append(rank)
    power_list.append(power)
    print("-" * 30) 

rata_rata_tim = np.mean(power_list)

status_misi = []
for p in power_list:
    if p >= 90:
        status = "Sangat kuat"
    elif p >= 80:
        status = "Cukup kuat"
    else:
        status = "Lemah"
    status_misi.append(status)

if rata_rata_tim >= 80:
    status_tim = "KUAT. Siap bertarung melawan upper moon demons."
else:
    status_tim = "REGULER. Bisa melawan lower moon demons, tapi tetap hati-hati dan harus kerja sama."

df_tim = pd.DataFrame({
    'Nama': nama_list,
    'Rank': rank_list,
    'Power': power_list,
    'Status Individu': status_misi
})

print("\n" + "="*50)
print(df_tim)
print("="*50)
print(f"Statistik Tim: Rata-rata Power = {rata_rata_tim:.2f}")
print(f"Kesimpulan Tim: {status_tim}")

