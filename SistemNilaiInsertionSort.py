import os

# ================= MEMBERSIHKAN TERMINAL =================
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


# ================= INPUT DATA =================
def input_data():
    data = []

    jumlah = int(input("Jumlah mahasiswa: "))

    for i in range(jumlah):
        nilai = float(input(f"Nilai mahasiswa {i+1}: "))
        data.append(nilai)

    return data


# ================= HITUNG NILAI =================
def hitung_nilai(data):
    return data


# ================= INSERTION SORT =================
def insertion_sort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1

        # Urut terbesar ke terkecil
        while j >= 0 and data[j] < key:
            data[j + 1] = data[j]
            j -= 1

        data[j + 1] = key

    return data


# ================= LINEAR SEARCH =================
def linear_search(data, target):

    for i in range(len(data)):

        if data[i] == target:
            return i

    return -1


# ================= TAMPILKAN DATA =================
def tampilkan_data(data):
    print("\nData setelah terurut:", data)


# ================= PROGRAM UTAMA =================

# Bersihkan terminal
clear_screen()

print("===== SISTEM PENGOLAHAN NILAI =====\n")
print("nama: indira suci")
print("NIM: 552010125006\n")

# Input data
data = input_data()

# Tampilkan data sebelum sorting
print("\nData sebelum Terurut:", data)

# Proses hitung nilai
data = hitung_nilai(data)

# Proses Insertion Sort 
data = insertion_sort(data)

# Tampilkan data sesudah sorting
tampilkan_data(data)

# Cari nilai
target = float(input("\nCari nilai: "))

# Proses pencarian
posisi = linear_search(data, target)

# Hasil pencarian
if posisi != -1:
    print(f"Nilai ditemukan pada indeks ke-{posisi}")
else:
    print(f"Posisi: {posisi}")
    print("Data tidak ada dalam list")