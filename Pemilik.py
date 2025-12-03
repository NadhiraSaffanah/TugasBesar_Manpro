from Database import fetch_one, fetch_all, execute_query
from tabulate import tabulate
def tampilkan_menu_pemilik():
    MENU_OPTIONS = {
        '1': menu_kelola_asisten,
        '2': menu_kelola_vendor,
        '3': menu_kelola_jenis_vendor,
        '4': menu_laporan_kerjasama,
        '5': menu_laporan_event
    }

    while True:
        print("\n===Menu Pemilik===")
        print("1. Kelola data asisten")
        print("2. Kelola data vendor")
        print("3. Kelola data jenis vendor")
        print("4. Lihat laporan kerja sama dengan vendor")
        print("5. Lihat laporan event")
        print("0. Keluar")

        pilihan = input("Pilih menu: ")
        print()

        if pilihan == '0':
            print("Keluar dari menu pemilik.")
            break
        elif pilihan in MENU_OPTIONS:
            MENU_OPTIONS[pilihan]()
        else:
            print("Pilihan tidak valid.")

def menu_kelola_asisten():
    while True:
        print("\n--- Kelola Asisten ---")
        print("1. Tambah asisten")
        print("2. Lihat data asisten")
        print("3. Edit data asisten")
        print("4. Hapus data asisten")
        print("0. Kembali")

        pilihan = input("Pilih menu: ")
        print()

        if pilihan == '0':
            break

        elif pilihan == '1':
            id_User = input("ID user: ")
            username = input("Username: ")
            password = input("Password: ")
            nama = input("Nama: ")
            alamat = input("Alamat: ")
            no_telepon = input("No Telepon: ")
            email = input("Email: ")
            role = 'asisten'

            tambah_asisten(id_User, username, password, nama, alamat, no_telepon, email, role)

        elif pilihan == '2':
            while True:
                print("1. Lihat semua data asisten.")
                print("2. Lihat data asisten spesifik.")
                print("0. Kembali")

                pilihan = input("Pilih menu: ")
                print()

                if pilihan == '0':
                    break
                elif pilihan == '1':
                    lihat_semua_data_asisten()
                elif pilihan == '2':
                    id_User = int(input("ID asisten: "))
                    lihat_data_asisten(id_User)

        elif pilihan == '3':
            id_User = int(input("ID user: "))
            nama_baru = input("Nama Baru: ")
            alamat_baru = input("Alamat Baru: ")
            telepon_baru = input("Telepon Baru: ")
            email_baru = input("Email Baru: ")

            edit_data_asisten(id_User, nama_baru, alamat_baru, telepon_baru, email_baru)

        elif pilihan == '4':
            id_User = int(input("ID user: "))
            hapus_asisten(id_User)

        else:
            print("Pilihan tidak valid.")
        pass

def menu_kelola_vendor():
    while True:
        print("\n--- Kelola Vendor ---")
        print("1. Tambah vendor")
        print("2. Lihat data vendor")
        print("3. Edit data vendor")
        print("4. Hapus data vendor")
        print("0. Kembali")

        pilihan = input("Pilih menu: ")
        print()

        if pilihan == '0':
            break

        elif pilihan == '1':
            id_Vendor = int(input("ID vendor: "))
            nama = input("Nama: ")
            nama_pemilik = input("Nama Pemilik: ")
            alamat = input("Alamat: ")
            no_telepon = input("No Telepon: ")
            email = input("Email: ")
            harga_min = int(input("Harga Min: "))
            harga_max = int(input("Harga Max: "))
            jenis_vendor = input("Jenis Vendor: ")

            tambah_vendor(id_Vendor, nama, nama_pemilik, alamat, no_telepon, email, harga_min, harga_max, jenis_vendor)

        elif pilihan == '2':
            while True:
                print("1. Lihat semua data vendor")
                print("2. Lihat data vendor spesifik")
                print("0. Kembali")

                pilihan = input("Pilih menu: ")
                print()

                if pilihan == '0':
                    break
                elif pilihan == '1':
                    lihat_semua_data_vendor()
                elif pilihan == '2':
                    id_Vendor = int(input("ID vendor: "))
                    lihat_data_vendor(id_Vendor)
                else:
                    print("Pilihan tidak valid.")

        elif pilihan == '3':
            id_Vendor = int(input("ID vendor: "))
            nama_baru = input("Nama vendor baru: ")
            pemilik_baru = input("Pemilik baru: ")
            alamat_baru = input("Alamat baru: ")
            telepon_baru = input("Telepon baru: ")
            email_baru = input("Email baru: ")
            harga_min_baru = int(input("Harga min baru: "))
            harga_max_baru = int(input("Harga max baru: "))
            edit_data_vendor(id_Vendor, nama_baru, pemilik_baru, alamat_baru, telepon_baru, email_baru, harga_min_baru, harga_max_baru)

        elif pilihan == '4':
            id_Vendor = int(input("ID vendor: "))
            hapus_vendor(id_Vendor)

        else:
            print("Pilihan tidak valid.")

        pass

def menu_kelola_jenis_vendor():
    while True:
        print("\n--- Kelola Jenis Vendor ---")
        print("1. Lihat data jenis vendor")
        print("2. Edit data jenis vendor")
        print("0. Kembali")

        pilihan = input("Pilih menu: ")
        print()

        if pilihan == '0':
            break
        elif pilihan == '1':
            lihat_data_jenis_vendor()
        elif pilihan == '2':
            jenis_lama = input("Jenis lama: ")
            jenis_baru = input("Jenis baru: ")
            edit_jenis_vendor(jenis_lama, jenis_baru)
        else:
            print("Pilihan tidak valid.")
        pass

def menu_laporan_kerjasama():
    while True:
        print("\n--- Laporan Kerja Sama ---")
        print("1. Lihat semua laporan kerjasama")
        print("2. Lihat laporan kerjasama spesifik")
        print("3. Lihat frekuensi kerjasama semua vendor")
        print("4. Lihat frekuensi kerjasama vendor spesifik")
        print("0. Kembali")

        pilihan = input("Pilih menu: ")
        print()

        if pilihan == '0':
            break
        elif pilihan == '1':
            lihat_semua_laporan()
        elif pilihan == '2':
            id_Vendor = int(input("ID vendor: "))
            lihat_laporan_tertentu(id_Vendor)
        elif pilihan == '3':
            lihat_frekuensi_semua_vendor()
        elif pilihan == '4':
            id_Vendor = int(input("ID vendor: "))
            lihat_frekuensi_spesifik(id_Vendor)
        else:
            print("Pilihan tidak valid.")