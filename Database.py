import pyodbc
import traceback

# Fungsi untuk koneksi ke database

def get_connection():
    return pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=localhost;'
        'DATABASE=Simulasi;'
        'Trusted_Connection=yes'
    )

# Fungsi untuk ambil satu data

def fetch_one(query, params=()):
    try:
        cnxn = get_connection()
        cursor = cnxn.cursor()
        cursor.execute(query, params)
        result = cursor.fetchone()
        cnxn.close()
        return result
    except Exception as e:
        print("[fetch_one] Error:", e)
        traceback.print_exc()
        return None

# Fungsi untuk ambil banyak data

def fetch_all(query, params=()):
    try:
        cnxn = get_connection()
        cursor = cnxn.cursor()
        cursor.execute(query, params)
        result = cursor.fetchall()
        cnxn.close()
        return result
    except Exception as e:
        print("[fetch_all] Error:", e)
        traceback.print_exc()
        return []

# Fungsi untuk eksekusi query tanpa return (insert, update, delete)

def execute_query(query, params=()):
    try:
        cnxn = get_connection()
        cursor = cnxn.cursor()
        cursor.execute(query, params)
        cnxn.commit()
        cnxn.close()
        return True
    except Exception as e:
        print("[execute_query] Error:", e)
        import traceback
        traceback.print_exc()
        return False
