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

def menu_laporan_event():
    while True:
        print("\n--- Laporan Event ---")
        print("1. Lihat event terdekat")
        print("2. Lihat event yang telah selesai")
        print("0. Kembali")

        pilihan = input("Pilih menu: ")
        print()

        if pilihan == '0':
            break
        elif pilihan == '1':
            lihat_event_terdekat()
        elif pilihan == '2':
            lihat_event_selesai()
        else:
            print("Pilihan tidak valid.")

# Fungsi CRUD asisten (disatukan untuk efisiensi penggunaan)
def tambah_asisten(id_User, username, password, nama, alamat, no_telepon, email, role):
    query = '''INSERT INTO [User] VALUES (?, ?, ?, ?, ?, ?, ?, ?)'''
    print()
    return "Input data asisten berhasil." if execute_query(query, (id_User, username, password, nama, alamat, no_telepon, email, role)) else "Input data asisten gagal."

def lihat_semua_data_asisten():
    hasil = fetch_all(
        '''
        SELECT id_User, nama, alamat, no_telepon, email 
        FROM [User]
        WHERE role = 'asisten'
        '''
    )
    print()
    if hasil:
        kolom = ['ID', 'Nama', 'Alamat', 'No Telepon', 'Email']  # Sesuaikan dengan struktur tabelmu
        print(tabulate(hasil, headers=kolom, tablefmt='grid'))
    else:
        print("Tidak ada data asisten ditemukan.")
    print()

def lihat_data_asisten(id_User):
    hasil = fetch_one('SELECT id_User, nama, alamat, no_telepon, email FROM [User] WHERE id_User = ?', (id_User,))
    print()

    if hasil:
        # Ambil nama kolom (jika fetch_one mengembalikan tuple, kamu butuh akses ke cursor.description)
        kolom = ['ID', 'Nama', 'Alamat', 'Nomor Telepon', 'Email']  # Ganti sesuai struktur tabelmu
        print(tabulate([hasil], headers=kolom, tablefmt='grid'))
    else:
        print("Asisten tidak ditemukan.")
    print()

def edit_data_asisten(id_User, nama_baru, alamat_baru, telepon_baru, email_baru):
    query = '''UPDATE [User] SET nama = ?, alamat = ?, no_telepon = ?, email = ? WHERE id_User = ?'''
    print()
    return "Data berhasil diubah." if execute_query(query, (nama_baru, alamat_baru, telepon_baru, email_baru, id_User)) else "Gagal mengubah data."

def hapus_asisten(id_User):
    execute_query('UPDATE UserEvent SET id_User = 1 WHERE id_User = ?', (id_User,))
    print()
    return "Data berhasil dihapus." if execute_query('DELETE FROM [User] WHERE id_User = ?', (id_User,)) else "Data tidak berhasil dihapus."

# Fungsi CRUD vendor
def tambah_vendor(id_Vendor, nama, nama_pemilik, alamat, no_telepon, email, harga_min, harga_max, jenis_vendor):
    query = '''INSERT INTO Vendor (id_Vendor, nama, nama_pemilik, alamat, no_telepon, email, harga_min, harga_max, jenis_vendor) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)'''
    print()
    return "Input data vendor berhasil." if execute_query(query, (id_Vendor, nama, nama_pemilik, alamat, no_telepon, email, harga_min, harga_max, jenis_vendor)) else "Input data vendor gagal."

def lihat_semua_data_vendor():
    hasil = fetch_all('SELECT * FROM Vendor')
    print()

    if hasil:
        kolom = ['ID', 'Nama Vendor', 'Pemilik', 'Alamat', 'No Telepon', 'Email', 'Harga Min', 'Harga Max', 'Jenis Vendor']  # Ganti sesuai struktur tabel Vendor
        print(tabulate(hasil, headers=kolom, tablefmt='grid'))
    else:
        print("Tidak ada data vendor ditemukan.")
    print()


def lihat_data_vendor(id_Vendor):
    hasil = fetch_one('SELECT * FROM Vendor WHERE id_Vendor = ?', (id_Vendor,))
    print()

    if hasil:
        kolom = ['ID', 'Nama Vendor', 'Pemilik', 'Alamat', 'No Telepon', 'Email', 'Harga Min', 'Harga Max', 'Jenis Vendor']  # Sesuaikan dengan struktur tabel Vendor
        print(tabulate([hasil], headers=kolom, tablefmt='grid'))
    else:
        print("Vendor tidak ditemukan.")
    print()

def edit_data_vendor(id_Vendor, nama_baru, pemilik_baru, alamat_baru, telepon_baru, email_baru, harga_min_baru, harga_max_baru):
    query = '''UPDATE Vendor SET nama = ?, nama_pemilik = ?, alamat = ?, no_telepon = ?, email = ?, harga_min = ?, harga_max = ? WHERE id_Vendor = ?'''
    return "Data vendor berhasil diubah." if execute_query(query, (nama_baru, pemilik_baru, alamat_baru, telepon_baru, email_baru, harga_min_baru, harga_max_baru, id_Vendor)) else "Gagal mengubah data vendor."

def hapus_vendor(id_Vendor): # FLAG
    print()
    execute_query('DELETE FROM EventVendor WHERE id_Vendor = ?', (id_Vendor,))
    return "Data berhasil dihapus." if execute_query('DELETE FROM Vendor WHERE id_Vendor = ?', (id_Vendor,)) else "Data tidak berhasil dihapus."

# Fungsi untuk Jenis Vendor
def lihat_data_jenis_vendor():
    hasil = fetch_all('SELECT DISTINCT jenis_vendor FROM Vendor WHERE jenis_vendor IS NOT NULL')
    print()

    if hasil:
        kolom = ['Jenis Vendor']
        print(tabulate(hasil, headers=kolom, tablefmt='grid'))
    else:
        print("Tidak ada data jenis vendor ditemukan.")
    print()

def edit_jenis_vendor(jenis_lama, jenis_baru):
    print()
    return "Jenis vendor berhasil diperbarui." if execute_query('UPDATE Vendor SET jenis_vendor = ? WHERE jenis_vendor = ?', (jenis_baru, jenis_lama)) else "Gagal memperbarui jenis vendor."

# Fungsi laporan kerja sama dengan vendor
def lihat_semua_laporan():
    query = '''SELECT * FROM EventVendor ev JOIN Event e ON ev.id_Event = e.id_Event JOIN Vendor v ON ev.id_Vendor = v.id_Vendor'''
    hasil = fetch_all(query)
    print()
    for baris in hasil:
        print(baris) if hasil else print("Tidak ada laporan ditemukan.")
    print()

def lihat_laporan_tertentu(id_Vendor):
    query = '''SELECT e.nama, v.nama, jenis_vendor FROM EventVendor ev JOIN Event e ON ev.id_Event = e.id_Event JOIN Vendor v ON ev.id_Vendor = v.id_Vendor WHERE v.id_Vendor = ?'''
    hasil = fetch_all(query, (id_Vendor,))
    print()

    if hasil:
        kolom = ['Nama Event', 'Nama Vendor', 'Jenis Vendor']
        print(tabulate([hasil], headers=kolom, tablefmt='grid'))
    else:
        print("Data kerjasama tidak ditemukan untuk vendor tersebut.")
    print()

def lihat_semua_laporan():
    query = '''
            SELECT e.nama, v.nama, jenis_vendor
            FROM EventVendor ev
                JOIN Event e ON ev.id_Event = e.id_Event
                JOIN Vendor v ON ev.id_Vendor = v.id_Vendor 
            '''
    hasil = fetch_all(query)
    print()

    if hasil:
        # Ganti dengan nama kolom sebenarnya dari hasil JOIN
        kolom = [
            'Nama Event', 'Nama Vendor', 'Jenis Vendor'
        ]
        print(tabulate(hasil, headers=kolom, tablefmt='grid'))
    else:
        print("Tidak ada laporan ditemukan.")
    print()

def lihat_frekuensi_spesifik(id_Vendor):
    query = '''
            SELECT v.nama, v.jenis_vendor, COUNT(ev.id_Vendor)
            FROM EventVendor ev
                JOIN Event e ON ev.id_Event = e.id_Event
                JOIN Vendor v ON ev.id_Vendor = v.id_Vendor
            WHERE v.id_Vendor = ?
            GROUP BY v.nama, v.jenis_vendor 
            '''
    hasil = fetch_one(query, (id_Vendor,))
    print()

    if hasil:
        kolom = ['Nama Vendor', 'Jenis Vendor', 'Frekuensi Kerjasama']
        print(tabulate([hasil], headers=kolom, tablefmt='grid'))
    else:
        print("Data frekuensi tidak ditemukan untuk vendor tersebut.")
    print()

def lihat_frekuensi_semua_vendor():
    query = '''
            SELECT v.nama, v.jenis_vendor, COUNT(ev.id_Vendor)
            FROM EventVendor ev
                JOIN Event e ON ev.id_Event = e.id_Event
                JOIN Vendor v ON ev.id_Vendor = v.id_Vendor
            GROUP BY v.nama, v.jenis_vendor
            '''
    hasil = fetch_all(query)
    print()

    if hasil:
        kolom = ['Nama Vendor', 'Jenis Vendor', 'Frekuensi Kerjasama']
        print(tabulate(hasil, headers=kolom, tablefmt='grid'))
    else:
        print("Tidak ada frekuensi kerja sama yang ditemukan.")
    print()

# Fungsi laporan event
def lihat_event_terdekat():
    query = '''
            SELECT u.nama, k.nama, e.nama, tanggal_event, lokasi
            FROM UserEvent ue 
                JOIN [User] u ON u.id_User = ue.id_User
                JOIN Event e ON e.id_Event = ue.id_Event
                JOIN Klien k ON e.id_Klien = k.id_Klien
            WHERE status_event = 'upcoming'
            ORDER BY tanggal_event ASC
            '''
    hasil = fetch_all(query)
    print()

    if hasil:
        kolom = [
            'Nama Asisten', 'Nama Klien', 'Nama Event', 'Tanggal Event', 'Lokasi Event'
        ]
        print(tabulate(hasil, headers=kolom, tablefmt='grid'))
    else:
        print("Tidak ada upcoming event.")
    print()

def lihat_event_selesai():
    query = '''
        SELECT u.nama, k.nama, e.nama, tanggal_event, lokasi, SUM(harga_dealing) 
        FROM UserEvent ue 
            JOIN [User] u ON u.id_User = ue.id_User 
            JOIN Event e ON e.id_Event = ue.id_Event 
            JOIN EventVendor ev ON ev.id_Event = e.id_Event 
            JOIN Klien k ON e.id_Klien = k.id_Klien
        WHERE status_event = 'completed' 
		GROUP BY u.nama, k.nama, e.nama, tanggal_event, lokasi
        ORDER BY tanggal_event ASC
    '''
    hasil = fetch_all(query)
    print()

    if hasil:
        kolom = [
            'Nama Asisten', 'Nama Klien', 'Nama Event', 'Tanggal Event', 'Lokasi', 'Total Biaya'
        ]
        print(tabulate(hasil, headers=kolom, tablefmt='grid'))
    else:
        print("Tidak ada event selesai.")
    print()