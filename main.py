nama_siswa = "Atha"
kelas_jurusan = "10 PPLG 2"

isi_kritiksaran = []

# Login

def login():
    print("Aplikasi Kritik Saran SMK Negeri 12 Surabaya")
    print("Selamat Datang!\n")

    while True:
        nama = input("Masukkan Nama: ")
        kelas = input("Masukkan Kelas dan Jurusan: ")
    
        if nama == nama_siswa and kelas == kelas_jurusan:
            print("")
            print("Login berhasil!")
            break
        else:
            print("Nama/Kelas Tidak Valid!")

# Create
def tulis_kritiksaran():
    print("")
    print(f"Dari: {nama_siswa} / {kelas_jurusan}")
    print("Ke: SMK Negeri 12 Surabaya")
    tulis = input("Masukkan Kritik/Saran Anda untuk SMK Negeri 12 Surabaya:\n")
    hasil = {
        "tulis" : tulis
    }
    isi_kritiksaran.append(hasil)
    print("")
    print("Terima Kasih Atas Kritik/Saran Yang Anda Berikan!")

# Read
def lihat_kritiksaran():
    print("")
    if len(isi_kritiksaran) == 0:
        print("Kritik/Saran Tidak Tersedia!")
    else:
        print(">>> Kritik/Saran Untuk SMK Negeri 12 Surabaya <<<\n")
        for i, s in enumerate(isi_kritiksaran, start=1):
            print(f"Kritik/Saran ke-{i}: {s['tulis']}")

# Update
def edit_kritiksaran():
    lihat_kritiksaran()
    if len(isi_kritiksaran) > 0:
        print("")
        nomor = int(input("Pilih Kritik/Saran Yang Ingin Diganti: ")) -1
        if nomor < len(isi_kritiksaran):
            tulis = input("Tulis Komentar Baru: ")
            isi_kritiksaran[nomor]["tulis"] = tulis
            print("")
            print("Kritik/Saran Telah Diedit!")

# Delete
def hapus_kritiksaran():
    lihat_kritiksaran()
    if len(isi_kritiksaran) > 0:
        print("")
        nomor = int(input("Pilih Kritik/Saran Yang Ingin Dihapus: ")) -1
        if nomor < len(isi_kritiksaran):
            isi_kritiksaran.pop(nomor)
            print("")
            print("Kritik/Saran Telah Dihapus!")

# Menu
def menu():
    while True:
        print("")
        print(f"Halo, {nama_siswa}")
        print("Apa yang anda akan lakukan hari ini?\n")
        print("1. Tulis Kritik/Saran")
        print("2. Lihat Kritik/Saran")
        print("3. Edit Kritik/Saran")
        print("4. Hapus Kritik/Saran")
        print("5. Keluar\n")

        pilih = input("Pilih Menu (1-5): ")

        if pilih == "1":
            tulis_kritiksaran()
        elif pilih == "2":
            lihat_kritiksaran()
        elif pilih == "3":
            edit_kritiksaran()
        elif pilih == "4":
            hapus_kritiksaran()
        elif pilih == "5":
            print("Sampai Jumpa!\n")
            break
        else:
            print("Pilihan Tidak Valid!")

# Program
login()
menu()

print("Program Selesai")