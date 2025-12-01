from Database import fetch_one, fetch_all, execute_query
from tabulate import tabulate
def tampilkan_menu_asisten():
    while True:
        print("\n===Menu Asisten===")
        print("1. Kelola data klien")
        print("2. Kelola data event")
        print("3. Kelola rincian budgeting")
        print("4. Laporan event")
        print("5. Lihat data vendor")
        print("0. Keluar")

        pilihan = input("Pilih menu: ")
        print()

        if pilihan == '1':
            menu_klien()
        elif pilihan == '2':
            menu_event()
        elif pilihan == '3':
            menu_budgeting()
        elif pilihan == '4':
            menu_laporan()
        elif pilihan == '5':
            menu_vendor()
        elif pilihan == '0':
            print("Keluar dari menu asisten.")
            break
        else:
            print("Pilihan tidak valid.")

# ============================
# SUB-MENU FUNGSI TERPISAH
# ============================
    def menu_klien():
        while True:
            print("\n=== Kelola Data Klien ===")
            print("1. Tambah klien")
            print("2. Lihat data klien")
            print("3. Edit data klien")
            print("4. Hapus data klien")
            print("0. Kembali")

            pilihan = input("Pilih menu: ")
            print()

            if pilihan == '1':
                print("=== Input Data Klien ===")
                id_klien = int(input("ID klien: "))
                nama = input("Nama klien: ")
                alamat = input("Alamat: ")
                no_telepon = input("Nomor telepon: ")
                email = input("Email: ")
                tanggal_registrasi = input("Tanggal registrasi: ")
                print(tambah_klien(id_klien, nama, alamat, no_telepon, email, tanggal_registrasi))

            elif pilihan == '2':
                id_Klien = int(input("Input ID klien: "))
                lihat_data_klien(id_Klien)

            elif pilihan == '3':
                print("=== Edit Data Klien ===")
                id_klien = int(input("ID klien: "))
                nama_baru = input("Nama baru klien: ")
                alamat = input("Alamat baru: ")
                no_telepon = input("Nomor telepon baru: ")
                email = input("Email baru: ")
                print(edit_data_klien(id_klien, nama_baru, alamat, no_telepon, email))

            elif pilihan == '4':
                id_klien = int(input("Input ID klien: "))
                print(hapus_data_klien(id_klien))

            elif pilihan == '0':
                break
            else:
                print("Pilihan tidak valid.")

    def menu_event():
        while True:
            print("\n=== Kelola Data Event ===")
            print("1. Tambah event")
            print("2. Lihat semua event")
            print("3. Lihat event spesifik")
            print("0. Kembali")

            pilihan = input("Pilih menu: ")
            print()

            if pilihan == '1':
                id_Event = int(input("ID event: "))
                nama = input("Nama event: ")
                jenis_event = input("Jenis event: ")
                tanggal_event = input("Tanggal event (YYYYMMDD): ")
                jumlah_undangan = int(input("Jumlah undangan: "))
                lokasi = input("Lokasi: ")
                status_event = input("Status event: ")
                total_budget = int(input("Total budget: "))
                id_Klien = int(input("ID klien: "))

                id_User = int(input("ID user: "))

                tambah_event(id_Event, jenis_event, tanggal_event, jumlah_undangan, lokasi, status_event, total_budget, id_Klien)
                tambah_user_event(id_Event, id_User)

            elif pilihan == '2':
                lihat_data_event()
            elif pilihan == '3':
                id_Klien = int(input("ID klien: "))
                lihat_event_spesifik(id_Klien)
            elif pilihan == '0':
                break
            else:
                print("Pilihan tidak valid.")

def menu_budgeting():
    while True:
        print("\n=== Rincian Budgeting ===")
        print("1. Lihat rincian budgeting")
        print("2. Lihat total rincian budgeting")
        print("3. Tambah vendor (harga dealing)")
        print("4. Ubah harga dealing")
        print("0. Kembali")

        pilihan = input("Pilih menu: ")
        print()

        if pilihan == '1':
            id_Klien = int(input("ID klien: "))
            lihat_rincian_budgeting(id_Klien)
        elif pilihan == '2':
            id_Event = int(input("ID event: "))
            total_budget_event(id_Event)
        elif pilihan == '3':
            id_Event = int(input("ID event: "))
            id_Vendor = int(input("ID vendor: "))
            harga_dealing = int(input("Harga dealing: "))
            tambah_harga_dealing(id_Event, id_Vendor, harga_dealing)
        elif pilihan == '4':
            id_Event = int(input("ID event: "))
            id_Vendor = int(input("ID vendor: "))
            harga_dealing = int(input("Harga dealing yang baru: "))
            update_harga_dealing(id_Event, id_Vendor, harga_dealing)
        elif pilihan == '0':
            break
        else:
            print("Pilihan tidak valid.")
