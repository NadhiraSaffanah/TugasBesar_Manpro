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

def menu_laporan():
        while True:
            print("\n=== Laporan Event ===")
            print("1. Event yang sudah selesai")
            print("2. Event yang sedang berlangsung")
            print("0. Kembali")

            pilihan = input("Pilih menu: ")
            print()

            if pilihan == '1':
                id_User = int(input("ID user: "))
                completed_event(id_User)
            elif pilihan == '2':
                id_User = int(input("ID user: "))
                upcoming_event(id_User)
            elif pilihan == '0':
                break
            else:
                print("Pilihan tidak valid.")


def menu_vendor():
    while True:
        print("\n=== Data Vendor ===")
        print("1. Daftar vendor")
        print("0. Kembali")

        pilihan = input("Pilih menu: ")
        print()

        if pilihan == '1':
            jenis_vendor = input("Jenis vendor: ")
            daftar_vendor(jenis_vendor)
        elif pilihan == '0':
            break
        else:
            print("Pilihan tidak valid.")

# Fungsi CRUD asisten (disatukan untuk efisiensi penggunaan)
def tambah_klien(id_klien, nama, alamat, no_telepon, email, tanggal_registrasi):
    query = '''
        INSERT INTO Klien VALUES (?, ?, ?, ?, ?, ?)
    '''
    success = execute_query(query, (id_klien, nama, alamat, no_telepon, email, tanggal_registrasi))
    print()
    return "Input data Klien berhasil." if success else "Input data klien gagal."

def lihat_data_klien(id_Klien):
    query = 'SELECT nama, alamat, no_telepon, email, tanggal_registrasi FROM Klien WHERE id_Klien = ?'
    hasil = fetch_one(query, (id_Klien,))
    print()

    if hasil:
        kolom = ['Nama Klien', 'Alamat', 'No Telepon', 'Email', 'Tanggal Registrasi']  # Ganti sesuai struktur tabel Klien
        print(tabulate([hasil], headers=kolom, tablefmt='grid'))
    else:
        print("Klien tidak ditemukan.")

def edit_data_klien(id_klien, nama_baru, alamat_baru, telepon_baru, email_baru):
    query = '''
        UPDATE Klien SET nama = ?, alamat = ?, no_telepon = ?, email = ? WHERE id_Klien = ?
    '''
    success = execute_query(query, (nama_baru, alamat_baru, telepon_baru, email_baru, id_klien))
    print()
    return "Edit data Klien berhasil." if success else "Edit data klien gagal."

def hapus_data_klien(id_Klien):
    execute_query('DELETE FROM Event WHERE id_Klien = ?', (id_Klien,))
    query = 'DELETE FROM Klien WHERE id_Klien = ?'
    success = execute_query(query, (id_Klien,))
    print()
    return "Hapus data Klien berhasil." if success else "Hapus data klien gagal."

def tambah_event(id_Event, nama, jenis_event, tanggal_event, jumlah_undangan, lokasi, status_event, total_budget, id_Klien):
    query = '''
        INSERT INTO Event (id_Event, nama, jenis_event, tanggal_event, jumlah_undangan, lokasi, status_event, total_budget, id_Klien)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    '''
    params = (id_Event, nama, jenis_event, tanggal_event, jumlah_undangan, lokasi, status_event, total_budget, id_Klien)
    hasil = execute_query(query, params)
    print()
    return "Tambah event berhasil" if hasil else "Tambah event gagal."

def tambah_user_event(id_Event, id_User):
    query = 'INSERT INTO UserEvent (id_Event, id_User) VALUES (?, ?)'
    params = (id_Event, id_User)
    hasil = execute_query(query, params)
    print()
    return "Tambah user_event berhasil" if hasil else "Tambah User Event gagal."

def lihat_data_event():
    query = '''
            SELECT k.nama, k.alamat, e.nama, tanggal_event, lokasi, total_budget
            FROM EventVendor ev
                JOIN Event e ON e.id_Event = ev.id_Event
                JOIN Vendor v ON v.id_Vendor = ev.id_Vendor
                JOIN Klien k ON e.id_Klien = k.id_Klien 
            GROUP BY k.nama, k.alamat, e.nama, tanggal_event, lokasi, total_budget
            '''
    hasil = fetch_all(query)
    print()

    if hasil:
        kolom = [
            'Nama Klien', 'Alamat Klien', 'Nama Event', 'Tanggal Event', 'Lokai Event', 'Total Budget', 'Nama Vendor'
        ]
        print(tabulate(hasil, headers=kolom, tablefmt='grid'))
    else:
        print("Tidak ada data event ditemukan.")

def lihat_event_spesifik(id_Klien):
    query = '''
            SELECT k.nama, k.alamat, e.nama, tanggal_event, lokasi, total_budget
            FROM EventVendor ev 
                JOIN Event e ON e.id_Event = ev.id_Event 
                JOIN Vendor v ON v.id_Vendor = ev.id_Vendor 
                JOIN Klien k ON e.id_Klien = k.id_Klien
            WHERE k.id_Klien = ? 
            GROUP BY k.nama, k.alamat, e.nama, tanggal_event, lokasi, total_budget
            '''
    hasil = fetch_all(query, (id_Klien,))
    print()

    if hasil:
        kolom = [
            'Nama Klien', 'Alamat Klien', 'Nama Event', 'Tanggal Event', 'Lokasi', 'Total Budget', 'Nama Vendor'
        ]
        print(tabulate(hasil, headers=kolom, tablefmt='grid'))
    else:
        print("Tidak ada event untuk klien ini.")

def lihat_rincian_budgeting(id_Klien):
    query = '''
            SELECT k.nama, e.nama, v.nama, jenis_vendor, harga_dealing 
            FROM EventVendor ev 
                JOIN Event e ON e.id_Event = ev.id_Event 
                JOIN Vendor v ON v.id_Vendor = ev.id_Vendor 
                JOIN Klien k ON e.id_Klien = k.id_Klien
            WHERE k.id_Klien = ? 
            '''
    hasil = fetch_all(query, (id_Klien,))
    print()

    if hasil:
        # Sesuaikan kolom berikut dengan hasil JOIN sebenarnya
        kolom = [
            'Nama Klien', 'Nama Event', 'Nama Vendor', 'Jenis Vendor', 'Harga Dealing'
        ]
        print(tabulate(hasil, headers=kolom, tablefmt='grid'))
    else:
        print("Tidak ada rincian budgeting ditemukan untuk klien ini.")

def total_budget_event(id_Event):
    query = '''
            SELECT SUM(harga_dealing)
            FROM EventVendor ev
                JOIN Event e ON e.id_Event = ev.id_Event
                JOIN Vendor v ON v.id_Vendor = ev.id_Vendor
                JOIN Klien k ON e.id_Klien = k.id_Klien
            WHERE k.id_Klien = ? 
            GROUP BY e.id_Event
            '''
    hasil = fetch_all(query, (id_Event,))
    print()

    if hasil and hasil[0][0] is not None:
        kolom = ['Nama Klien', 'Nama Event', 'Nama Vendor', 'Jenis Vendor', 'Total Harga Dealing']
        print(tabulate(hasil, headers=kolom, tablefmt='grid'))
    else:
        print("Tidak ada data budget untuk klien ini.")

def tambah_harga_dealing(id_Event, id_Vendor, harga_dealing):
    query = '''
        INSERT INTO
            EventVendor 
        VALUES (?, ?, ?)
    '''
    hasil = execute_query(query, (id_Event, id_Vendor, harga_dealing,))
    print()
    print("Tambah harga dealing berhasil." if hasil else "Tambah harga dealing gagal.")

def update_harga_dealing(id_Event, id_Vendor, harga_dealing):
    query = '''
        UPDATE 
            EventVendor 
        SET 
            harga_dealing = ? 
        WHERE 
            id_Event = ? AND id_Vendor = ? 
    '''
    hasil = execute_query(query, (harga_dealing, id_Event, id_Vendor,))
    print()
    print("Update harga dealing berhasil" if hasil else "Update harga dealing gagal.")

def completed_event(id_User):
    query = '''
            SELECT e.nama, k.nama, status_event 
            FROM UserEvent ev 
                JOIN [User] u ON u.id_User = ev.id_User
                JOIN Event e ON e.id_Event = ev.id_Event
                JOIN Klien k ON e.id_Klien = k.id_Klien
            WHERE status_event = 'completed' AND u.id_User = ? 
            '''
    hasil = fetch_all(query, (id_User,))
    print()

    if hasil:
        kolom = [
            'Nama Event', 'Nama Klien', 'Status Event'
        ]  # Ganti sesuai dengan struktur dan urutan kolom hasil join-mu
        print(tabulate(hasil, headers=kolom, tablefmt='grid'))
    else:
        print("Event tidak ditemukan.")

def upcoming_event(id_User):
    query = '''
            SELECT u.nama, k.nama, e.nama, tanggal_event, status_event \
            FROM UserEvent ev
                JOIN [User] u ON u.id_User = ev.id_User
                JOIN Event e ON e.id_Event = ev.id_Event 
            WHERE status_event = 'upcoming' AND u.id_User = ? 
            '''
    hasil = fetch_all(query, (id_User,))
    print()

    if hasil:
        kolom = [
            'Nama Asisten', 'Nama Klien', 'Nama Event', 'Tanggal Event', 'Status Event'
        ]
        print(tabulate(hasil, headers=kolom, tablefmt='grid'))
    else:
        print("Event tidak ditemukan.")


def daftar_vendor(jenis_vendor):
    query = '''
            SELECT nama, alamat, no_telepon, harga_min, harga_max, jenis_vendor
            FROM Vendor
            WHERE jenis_vendor = ? 
            '''
    hasil = fetch_all(query, (jenis_vendor,))
    print()

    if hasil:
        kolom = ['Nama Vendor', 'Alamat', 'No Telepon', 'Harga Min', 'Harga Max', 'Jenis Vendor']
        print(tabulate(hasil, headers=kolom, tablefmt='grid'))
    else:
        print("Jenis vendor tidak ditemukan.")