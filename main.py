import datetime as dt # Waktu

nama_siswa = "Atha"
kelas_jurusan = "10 PPLG 2"

# Login

def login():
    print("Aplikasi Kritik Saran SMK Negeri 12 Surabaya")
    print("Selamat Datang!\n")

    while True:
        nama = input("Masukkan Nama: ")
        kelas = input("Masukkan Kelas dan Jurusan: ")
    
        if nama == nama_siswa and kelas == kelas_jurusan:
            print("")
            print("Login berhasil!\n")
            break

        else:
            print("Nama/Kelas Tidak Valid!")

# Create
def komentar():
    print(f"Dari {nama_siswa} / {kelas_jurusan}")
    tanggal = dt.date.today()
    print(tanggal)

# Menu
def menu():
    print(f"Halo, {nama_siswa}")
    print("Apa yang anda akan lakukan hari ini?")
    print("1. Komentar")
    print("2. Lihat Komentar")
    print("3. Edit Komentar")
    print("4. Hapus Komentar\n")

    pilih = input("Pilih Menu (1-4): ")

    if pilih == "1":
        komentar()

# Program
login()
menu()