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
