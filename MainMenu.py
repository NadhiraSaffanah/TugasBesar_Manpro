from Database import get_connection
from Pemilik import tampilkan_menu_pemilik
from Asisten import tampilkan_menu_asisten  # Asumsikan kamu punya fungsi ini
from tabulate import tabulate
def login(username, password):
    cnxn = get_connection()
    cursor = cnxn.cursor()
    query = '''
        SELECT id_User, username, password, role
        FROM [User]
        WHERE username = ? AND password = ?
    '''
    cursor.execute(query, (username, password))
    user = cursor.fetchone()
    cnxn.close()

    if user:
        _, _, _, role = user
        return True, role
    else:
        return False, "\nUsername atau password salah."

def main():
    print("=== Selamat datang di Aplikasi Manajemen Event ===")
    username = input("Username: ")
    password = input("Password: ")

    sukses, hasil = login(username, password)
    if sukses:
        if hasil == 'pemilik':
            tampilkan_menu_pemilik()
        elif hasil == 'asisten':
            tampilkan_menu_asisten()
        else:
            print(f"Role tidak dikenali: {hasil}")
    else:
        print(hasil)

if __name__ == "__main__":
    main()
