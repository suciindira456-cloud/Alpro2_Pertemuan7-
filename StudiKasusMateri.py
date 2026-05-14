# Program Sistem Pengolahan Nilai Mahasiswa

mahasiswa = []

# Input jumlah mahasiswa
jumlah = int(input("Masukkan jumlah mahasiswa: "))

# Input data mahasiswa
for i in range(jumlah):
    print(f"\nData Mahasiswa ke-{i+1}")

    nama = input("Nama Mahasiswa : ")
    tugas = float(input("Nilai Tugas   : "))
    uts = float(input("Nilai UTS     : "))
    uas = float(input("Nilai UAS     : "))

    # Menghitung nilai akhir
    nilai_akhir = (0.3 * tugas) + (0.3 * uts) + (0.4 * uas)

    # Menyimpan data mahasiswa
    mahasiswa.append({
        "nama": nama,
        "tugas": tugas,
        "uts": uts,
        "uas": uas,
        "akhir": nilai_akhir
    })

# Proses Sorting (Bubble Sort)
for i in range(len(mahasiswa)):
    for j in range(0, len(mahasiswa)-i-1):
        if mahasiswa[j]["akhir"] < mahasiswa[j+1]["akhir"]:
            mahasiswa[j], mahasiswa[j+1] = mahasiswa[j+1], mahasiswa[j]

# Menampilkan data mahasiswa
print("\n=== DATA NILAI MAHASISWA ===")
for data in mahasiswa:
    print(f"Nama         : {data['nama']}")
    print(f"Nilai Akhir  : {data['akhir']:.2f}")
    print("---------------------------")

# Proses Searching (Linear Search)
cari = input("\nMasukkan nama mahasiswa yang dicari: ")
ditemukan = False

for data in mahasiswa:
    if data["nama"].lower() == cari.lower():
        print("\nData Mahasiswa Ditemukan")
        print(f"Nama         : {data['nama']}")
        print(f"Nilai Akhir  : {data['akhir']:.2f}")
        ditemukan = True
        break

if not ditemukan:
    print("Mahasiswa tidak ditemukan")