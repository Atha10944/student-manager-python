nama_siswa = "Atha"
kelas_jurusan = "10 PPLG 2"

isi_kritiksaran = []

# Login

def login():
    print("Aplikasi Kritik Saran SMK Negeri 12 Surabaya")
    print("Selamat Datang!\n")

    while True:
        nama = input("\33[0;49;37mMasukkan Nama: ")
        kelas = input("Masukkan Kelas dan Jurusan: ")
    
        if nama == nama_siswa and kelas == kelas_jurusan:
            print("")
            print("\33[1;49;36mLogin berhasil!\n")
            break
        else:
            print("")
            print("\33[1;49;31mNama/Kelas Tidak Valid!\n")

# Create
def tulis_kritiksaran():
    print("")
    print(f"Dari: {nama_siswa} / {kelas_jurusan}")
    print("Ke: SMK Negeri 12 Surabaya\n")
    tulis = input("Masukkan Kritik/Saran Anda untuk SMK Negeri 12 Surabaya:\n")
    hasil = {
        "tulis" : tulis
    }
    isi_kritiksaran.append(hasil)
    print("")
    print("\33[1;49;36mTerima Kasih Atas Kritik/Saran Yang Anda Berikan!\n")

# Read
def lihat_kritiksaran():
    print("")
    if len(isi_kritiksaran) == 0:
        print("\33[1;49;33mKritik/Saran Tidak Tersedia!\n")
    else:
        print(">>> Kritik/Saran Untuk SMK Negeri 12 Surabaya <<<\n")
        for i, s in enumerate(isi_kritiksaran, start=1):
            print(f"Kritik/Saran ke-{i}:\n{s['tulis']}\n")

# Update
def edit_kritiksaran():
    lihat_kritiksaran()
    if len(isi_kritiksaran) > 0:
        nomor = int(input("Pilih Nomor Kritik/Saran Yang Ingin Diubah: ")) -1
        if nomor < len(isi_kritiksaran):
            tulis = input("Tulis Kritik/Saran Baru: ")
            isi_kritiksaran[nomor]["tulis"] = tulis
            print("")
            print("\33[1;49;36mKritik/Saran Berhasil Diubah!\n")
        else:
            print("")
            print("\33[1;49;31mPilihan Tidak Valid!\n")

# Delete
def hapus_kritiksaran():
    lihat_kritiksaran()
    if len(isi_kritiksaran) > 0:
        nomor = int(input("Pilih Nomor Kritik/Saran Yang Ingin Dihapus: ")) -1
        if nomor < len(isi_kritiksaran):
            isi_kritiksaran.pop(nomor)
            print("")
            print("\33[1;49;36mKritik/Saran Berhasil Dihapus!\n")
        else:
            print("")
            print("\33[1;49;31Pilihan Tidak Valid!\n")

# Menu
def menu():
    while True:
        print(f"\33[0;49;37mHalo, {nama_siswa}")
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
            print("")
            print("\33[1;49;33mSampai Jumpa!")
            break
        else:
            print("")
            print("\33[1;49;31mPilihan Tidak Valid!\n")

# Program
login()
menu()