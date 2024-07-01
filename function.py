from psycopg2.extras import RealDictCursor
import bcrypt
from datetime import datetime
from tabulate import tabulate
import os
import psycopg2

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_db_connection():
    conn = psycopg2.connect(
        dbname="algopro",
        user="postgres",
        password="chiel188",
    )
    return conn

# LOGIN ADMIN
def login_admin(username, password):
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    try:
        cur.execute("SELECT * FROM admin WHERE username = %s", (username,))
        admin = cur.fetchone()
        if admin:
            if bcrypt.checkpw(password.encode('utf-8'), admin['password'].encode('utf-8')):
                return admin
        return None
    except Exception as e:
        print(f'Error: {e}')
        return None
    finally:
        cur.close()
        conn.close()

# REGISTER CUSTOMER
def create_provinsi(cur, provinsi_name):
    cur.execute("SELECT provinsi_id FROM provinsi WHERE nama_provinsi = %s", (provinsi_name,))
    result = cur.fetchone()
    if result:
        return result['provinsi_id']
    else:
        cur.execute("INSERT INTO provinsi (nama_provinsi) VALUES (%s) RETURNING provinsi_id", (provinsi_name,))
        return cur.fetchone()['provinsi_id']

def create_kab_kota(cur, nama_kota, provinsi_id):
    cur.execute("SELECT kota_id FROM kota WHERE nama_kota = %s AND provinsi_provinsi_id = %s", (nama_kota, provinsi_id))
    result = cur.fetchone()
    if result:
        return result['kota_id']
    else:
        cur.execute("INSERT INTO kota (nama_kota, provinsi_provinsi_id) VALUES (%s, %s) RETURNING kota_id", (nama_kota, provinsi_id))
        return cur.fetchone()['kota_id']
    
def create_provinsi_gunung(provinsi_name):
    try:
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute("SELECT provinsi_id FROM provinsi WHERE nama_provinsi = %s", (provinsi_name,))
        result = cur.fetchone()
        if result:
            return result['provinsi_id']
        else:
            cur.execute("INSERT INTO provinsi (nama_provinsi) VALUES (%s) RETURNING provinsi_id", (provinsi_name,))
            provinsi_id = cur.fetchone()['provinsi_id']
            conn.commit()  # Commit transaksi
            return provinsi_id
    except psycopg2.Error as e:
        print("Error:", e)
        conn.rollback()  # Lakukan rollback jika terjadi kesalahan
        return None
    finally:
        cur.close()
        conn.close()

def create_kab_kota_gunung(nama_kota, provinsi_id):
    try:
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute("SELECT kota_id FROM kota WHERE nama_kota = %s AND provinsi_provinsi_id = %s", (nama_kota, provinsi_id))
        result = cur.fetchone()
        if result:
            return result['kota_id']
        else:
            cur.execute("INSERT INTO kota (nama_kota, provinsi_provinsi_id) VALUES (%s, %s) RETURNING kota_id", (nama_kota, provinsi_id))
            kota_id = cur.fetchone()['kota_id']
            conn.commit()  # Commit transaksi
            return kota_id
    except psycopg2.Error as e:
        print("Error:", e)
        conn.rollback()  # Lakukan rollback jika terjadi kesalahan
        return None
    finally:
        cur.close()
        conn.close()

def create_loket_loop(nama_gunung):
    provinsi = input("Masukkan nama provinsi: ")
    provinsi_id = create_provinsi_gunung(provinsi)
    kota = input("Masukkan nama kota: ")
    kota_id = create_kab_kota_gunung(kota, provinsi_id)
    if kota_id:
        gunung_id = cari_gunung_id(nama_gunung)
        if gunung_id:
                create_loket(kota_id, gunung_id)
    else:
        print("Pembuatan kota gagal.")


def register_customer(username, password, nama, nik, telepon, tanggal_lahir, alamat, kota, provinsi):
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    try:
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        
        provinsi_id = create_provinsi(cur, provinsi)
        kab_kota_id = create_kab_kota(cur, kota, provinsi_id)

        cur.execute("INSERT INTO customer (username, password, nama_lengkap, nik, telepon, tanggal_lahir, alamat, kota_kota_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
            (username, hashed_password, nama, nik, telepon, tanggal_lahir, alamat, kab_kota_id)
        )
        conn.commit()
        clear_screen()
        print("="*100)
        print("REGISTRASI BERHASIL".center(100))
        print("="*100)
        print("Silahkan login kembali")
        input("Klik enter untuk login kembali")
    except Exception as e:
        print(f'Error: {e}')
        conn.rollback()
    finally:
        cur.close()
        conn.close()

# LOGIN CUSTOMER
def login_customer(username, password):
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    try:
        cur.execute("SELECT * FROM customer WHERE username = %s", (username,))
        customer = cur.fetchone()
        if customer:
            if bcrypt.checkpw(password.encode('utf-8'), customer['password'].encode('utf-8')):
                return customer
        return None
    except Exception as e:
        print(f'Error: {e}')
        return None
    finally:
        cur.close()
        conn.close()

# DISPLAY CUSTOMER (ADMIN)
def display_customer():
    conn = get_db_connection()  
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    try:
        cursor.execute("select c.nama_lengkap, c.telepon, c.alamat, k.nama_kota, p.nama_provinsi from customer c join kota k on (k.kota_id = c.kota_kota_id) join provinsi p on (p.provinsi_id = k.provinsi_provinsi_id);") 
        customers = cursor.fetchall()
        data = []
        for customer in customers:
            nama = customer['nama_lengkap']
            telp = customer['telepon']
            alamat = customer['alamat']
            kota = customer['nama_kota']
            provinsi = customer['nama_provinsi']
            data.append([nama, telp, alamat, kota, provinsi])
        
        headers = ["Nama customer", "No. Telp", "Alamat", "Kota" ,"Provinsi"]
        print(tabulate(data, headers=headers, tablefmt="grid"))
    except psycopg2.Error as e:
        print("Error:", e)
    finally:
        cursor.close()
        conn.close()

# DISPLAY GUNUNG
def display_gunung():
    conn = get_db_connection()  
    cur = conn.cursor(cursor_factory=RealDictCursor)
    try:
        cur.execute("select g.gunung_id, g.nama_gunung, g.tinggi, le.level_id, g.harga, k.nama_kota, p.nama_provinsi from loket lo join kota k on (k.kota_id = lo.kota_kota_id) join gunung g on (lo.gunung_gunung_id = g.gunung_id) join level le on (g.level_level_id = le.level_id) join provinsi p on (p.provinsi_id = k.provinsi_provinsi_id);") 
        gunung1 = cur.fetchall()
        data = []
        for gunung in gunung1:
            id = gunung['gunung_id']
            nama = gunung['nama_gunung']
            tinggi = gunung['tinggi']
            level = gunung['level_id']
            harga = gunung['harga']
            kota = gunung ['nama_kota']
            provinsi = gunung['nama_provinsi']
            data.append([id, nama,tinggi, level, harga, kota, provinsi])
        
        headers = ["ID","Nama Gunung", "Tinggi", "Level", "Harga Tiket","Kota" ,"Provinsi"]
        print(tabulate(data, headers=headers, tablefmt="grid"))
    except psycopg2.Error as e:
        print("Error:", e)
    finally:
        cur.close()
        conn.close()

# RIWAYAT URUT TANGGAL DAKI DARI TERLAMA
def display_riwayat_urut_tanggal_daki_terlama():
    conn = get_db_connection()
    cur = conn.cursor()
    try:
        cur.execute(
            "SELECT p.pemesanan_id, p.tanggal_pesan, p.tanggal_daki, c.nama_lengkap, g.nama_gunung FROM pemesanan p JOIN customer c ON p.customer_customer_id = c.customer_id JOIN gunung g ON p.gunung_gunung_id = g.gunung_id"
            )
        riwayat_customer = cur.fetchall()

        riwayat_customer_urut = quicksort_ke_besar(riwayat_customer, key=lambda x: x[2])
        print(tabulate(riwayat_customer_urut, headers=["ID Pemesanan", "Tanggal Pesan", "Tanggal Daki", "Nama Customer", "Nama Gunung"], tablefmt="pretty"))

        conn.commit()
    except Exception as e:
        print(f"Error: {e}")
        conn.rollback()
    finally:
        cur.close()
        conn.close()

# RIWAYAT URUT TANGGAL DAKI DARI TERBARU
def display_riwayat_urut_tanggal_daki_terbaru():
    conn = get_db_connection()
    cur = conn.cursor()
    try:
        cur.execute(
            "SELECT p.pemesanan_id, p.tanggal_pesan, p.tanggal_daki, c.nama_lengkap, g.nama_gunung FROM pemesanan p JOIN customer c ON p.customer_customer_id = c.customer_id JOIN gunung g ON p.gunung_gunung_id = g.gunung_id"
            )
        riwayat_customer = cur.fetchall()

        riwayat_customer_urut = quicksort_ke_kecil(riwayat_customer, key=lambda x: x[2])
        print(tabulate(riwayat_customer_urut, headers=["ID Pemesanan", "Tanggal Pesan", "Tanggal Daki", "Nama Customer", "Nama Gunung"], tablefmt="pretty"))

        conn.commit()
    except Exception as e:
        print(f"Error: {e}")
        conn.rollback()
    finally:
        cur.close()
        conn.close()

# BINARY SEARCH
def binary_search(arr, x, y):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (high + low) // 2
        if arr[mid][y].lower().startswith(x):
            return mid
        elif arr[mid][y].lower() < x:
            low = mid + 1
        else:
            high = mid - 1

    return -1

# CARI RIWAYAT BERDASARKAN NAMA GUNUNG
def cari_riwayat_nama_gunung(conn, nama_gunung):
    conn = get_db_connection()
    cur = conn.cursor()
    hasil_gunung = []
    try:
        cur.execute(
            "SELECT p.pemesanan_id, p.tanggal_pesan, p.tanggal_daki, c.nama_lengkap, g.nama_gunung FROM pemesanan p JOIN customer c ON p.customer_customer_id = c.customer_id JOIN gunung g ON p.gunung_gunung_id = g.gunung_id ORDER BY g.nama_gunung"
        )
        riwayat_gunung = cur.fetchall()
        nama_gunung = nama_gunung.lower()
        indeks = 4
        # riwayat_gunung = quicksort(riwayat_gunung, key=lambda x: x[4].lower()) # Urutkan data berdasarkan nama gunung
        index = binary_search(riwayat_gunung, nama_gunung, indeks)
        if index != -1:
            hasil_gunung.append(riwayat_gunung[index])
            left_index = index - 1
            right_index = index + 1
            while left_index >= 0 and riwayat_gunung[left_index][4].lower().startswith(nama_gunung):
                hasil_gunung.append(riwayat_gunung[left_index])
                left_index -= 1
            while right_index < len(riwayat_gunung) and riwayat_gunung[right_index][4].lower().startswith(nama_gunung):
                hasil_gunung.append(riwayat_gunung[right_index])
                right_index += 1
        conn.commit()
    except Exception as e:
        print(f"Error: {e}")
        conn.rollback()
    finally:
        cur.close()
        conn.close()
    return hasil_gunung

def display_riwayat_nama_gunung():
    conn = get_db_connection()
    try:
        nama_gunung = input("Masukkan nama gunung yang ingin dicari: ")
        hasil_gunung = cari_riwayat_nama_gunung(conn, nama_gunung)
        if hasil_gunung:
            print(tabulate(hasil_gunung, headers=["ID Pemesanan", "Tanggal Pesan", "Tanggal Daki", "Nama Customer", "Nama Gunung"], tablefmt="pretty"))
        else:
            print("Riwayat customer dengan Nama Gunung", nama_gunung, "tidak ditemukan.")

    except Exception as e:
        print(f"Error: {e}")

# CARI RIWAYAT BERDASARKAN NAMA CUSTOMER
def cari_riwayat_nama_customer(conn, nama_customer):
    conn = get_db_connection()
    cur = conn.cursor()
    hasil_customer = []
    try:
        cur.execute(
            "SELECT p.pemesanan_id, p.tanggal_pesan, p.tanggal_daki, c.nama_lengkap, g.nama_gunung FROM pemesanan p JOIN customer c ON p.customer_customer_id = c.customer_id JOIN gunung g ON p.gunung_gunung_id = g.gunung_id ORDER BY c.nama_lengkap"
        )
        riwayat_customer = cur.fetchall()
        nama_customer = nama_customer.lower()
        indeks = 3
        # riwayat_customer = quicksort(riwayat_customer, key=lambda x: x[3].lower())
        index = binary_search(riwayat_customer, nama_customer, indeks)
        if index != -1:
            hasil_customer.append(riwayat_customer[index])
            kiri = index - 1
            kanan = index + 1
            while kiri >= 0 and riwayat_customer[kiri][3].lower().startswith(nama_customer):
                hasil_customer.append(riwayat_customer[kiri])
                kiri -= 1
            while kanan < len(riwayat_customer) and riwayat_customer[kanan][3].lower().startswith(nama_customer):
                hasil_customer.append(riwayat_customer[kanan])
                kanan += 1
        conn.commit()
    except Exception as e:
        print(f"Error: {e}")
        conn.rollback()
    finally:
        cur.close()
        conn.close()
    return hasil_customer

def display_riwayat_nama_customer():
    conn = get_db_connection()
    try:
        nama_customer = input("Masukkan nama customer yang ingin dicari: ")
        hasil_customer = cari_riwayat_nama_customer(conn, nama_customer)
        if hasil_customer:
            print(tabulate(hasil_customer, headers=["ID Pemesanan", "Tanggal Pesan", "Tanggal Daki", "Nama Customer", "Nama Gunung"], tablefmt="pretty"))
        else:
            print("Riwayat customer dengan Nama", nama_customer, "tidak ditemukan.")

    except Exception as e:
        print(f"Error: {e}")

# CARI GUNUNG BERDASARKAN NAMA GUNUNG
def cari_nama_gunung(conn, nama_gunung):
    conn = get_db_connection()
    cur = conn.cursor()
    hasil_gunung = []
    try:
        cur.execute(
            "select g.gunung_id, g.nama_gunung, g.tinggi, le.level_id, g.harga, k.nama_kota, p.nama_provinsi from loket lo join kota k on (k.kota_id = lo.kota_kota_id) join gunung g on (lo.gunung_gunung_id = g.gunung_id) join level le on (g.level_level_id = le.level_id) join provinsi p on (p.provinsi_id = k.provinsi_provinsi_id) order by nama_gunung;"
        )
        gunung = cur.fetchall()
        nama_gunung = nama_gunung.lower()
        indeks = 1
        # riwayat_gunung = quicksort(riwayat_gunung, key=lambda x: x[4].lower()) # Urutkan data berdasarkan nama gunung
        index = binary_search(gunung, nama_gunung, indeks)
        if index != -1:
            hasil_gunung.append(gunung[index])
            left_index = index - 1
            right_index = index + 1
            while left_index >= 0 and gunung[left_index][1].lower().startswith(nama_gunung):
                hasil_gunung.append(gunung[left_index])
                left_index -= 1
            while right_index < len(gunung) and gunung[right_index][1].lower().startswith(nama_gunung):
                hasil_gunung.append(gunung[right_index])
                right_index += 1
        conn.commit()
    except Exception as e:
        print(f"Error: {e}")
        conn.rollback()
    finally:
        cur.close()
        conn.close()
    return hasil_gunung

def display_nama_gunung():
    conn = get_db_connection()
    try:
        nama_gunung = input("Masukkan nama gunung yang ingin dicari: ")
        hasil_gunung = cari_nama_gunung(conn, nama_gunung)
        if hasil_gunung:
            print(tabulate(hasil_gunung, headers=["ID Gunung", "Nama Gunung", "Tinggi", "Level", "Harga", "Nama Kota", "Nama Provinsi"], tablefmt="pretty"))
        else:
            print("Gunung dengan Nama", nama_gunung, "tidak ditemukan.")

    except Exception as e:
        print(f"Error: {e}")

# QUICK SORT
# Dari kecil ke besar
def quicksort_ke_besar(arr, key=lambda x: x):
    if len(arr) <= 1:
        return arr
    pivot = key(arr[len(arr) // 2])
    left = [x for x in arr if key(x) < pivot]
    middle = [x for x in arr if key(x) == pivot]
    right = [x for x in arr if key(x) > pivot]
    return quicksort_ke_besar(left, key) + middle + quicksort_ke_besar(right, key)

# Dari besar ke kecil
def quicksort_ke_kecil(arr, key=lambda x: x):
    if len(arr) <= 1:
        return arr
    pivot = key(arr[len(arr) // 2])
    left = [x for x in arr if key(x) > pivot]
    middle = [x for x in arr if key(x) == pivot]
    right = [x for x in arr if key(x) < pivot]
    return quicksort_ke_kecil(left, key) + middle + quicksort_ke_kecil(right, key)

# GUNUNG URUT NAMA ASC
def display_gunung_urut_nama_asc():
    conn = get_db_connection()
    cur = conn.cursor()
    try:
        cur.execute(
            "select g.gunung_id, g.nama_gunung, g.tinggi, le.level_id, g.harga, k.nama_kota, p.nama_provinsi from loket lo join kota k on (k.kota_id = lo.kota_kota_id) join gunung g on (lo.gunung_gunung_id = g.gunung_id) join level le on (g.level_level_id = le.level_id) join provinsi p on (p.provinsi_id = k.provinsi_provinsi_id)"
            )
        gunung = cur.fetchall()

        gunung_urut = quicksort_ke_besar(gunung, key=lambda x: x[1].casefold())
        headers = ["ID", "Nama Gunung", "Tinggi", "Level", "Harga Tiket","Kota" ,"Provinsi"]
        print(tabulate(gunung_urut, headers=headers, tablefmt="grid"))
        conn.commit()
    except Exception as e:
        print(f"Error: {e}")
        conn.rollback()
    finally:
        cur.close()
        conn.close()

# GUNUNG URUT NAMA DESC
def display_gunung_urut_nama_desc():
    conn = get_db_connection()
    cur = conn.cursor()
    try:
        cur.execute(
            "select g.gunung_id, g.nama_gunung, g.tinggi, le.level_id, g.harga, k.nama_kota, p.nama_provinsi from loket lo join kota k on (k.kota_id = lo.kota_kota_id) join gunung g on (lo.gunung_gunung_id = g.gunung_id) join level le on (g.level_level_id = le.level_id) join provinsi p on (p.provinsi_id = k.provinsi_provinsi_id)"
            )
        gunung = cur.fetchall()

        gunung_urut = quicksort_ke_kecil(gunung, key=lambda x: x[1].casefold())
        headers = ["ID", "Nama Gunung", "Tinggi", "Level", "Harga Tiket","Kota" ,"Provinsi"]
        print(tabulate(gunung_urut, headers=headers, tablefmt="grid"))
        conn.commit()
    except Exception as e:
        print(f"Error: {e}")
        conn.rollback()
    finally:
        cur.close()
        conn.close()

# GUNUNG URUT TINGGI ASC
def display_gunung_urut_tinggi_asc():
    conn = get_db_connection()
    cur = conn.cursor()
    try:
        cur.execute(
            "select g.gunung_id, g.nama_gunung, g.tinggi, le.level_id, g.harga, k.nama_kota, p.nama_provinsi from loket lo join kota k on (k.kota_id = lo.kota_kota_id) join gunung g on (lo.gunung_gunung_id = g.gunung_id) join level le on (g.level_level_id = le.level_id) join provinsi p on (p.provinsi_id = k.provinsi_provinsi_id)"
            )
        gunung = cur.fetchall()

        gunung_urut = quicksort_ke_besar(gunung, key=lambda x: x[2])
        headers = ["ID", "Nama Gunung", "Tinggi", "Level", "Harga Tiket","Kota" ,"Provinsi"]
        print(tabulate(gunung_urut, headers=headers, tablefmt="grid"))
        
        conn.commit()
    except Exception as e:
        print(f"Error: {e}")
        conn.rollback()
    finally:
        cur.close()
        conn.close()

# GUNUNG URUT TINGGI DESC
def display_gunung_urut_tinggi_desc():
    conn = get_db_connection()
    cur = conn.cursor()
    try:
        cur.execute(
            "select g.gunung_id, g.nama_gunung, g.tinggi, le.level_id, g.harga, k.nama_kota, p.nama_provinsi from loket lo join kota k on (k.kota_id = lo.kota_kota_id) join gunung g on (lo.gunung_gunung_id = g.gunung_id) join level le on (g.level_level_id = le.level_id) join provinsi p on (p.provinsi_id = k.provinsi_provinsi_id)"
            )
        gunung = cur.fetchall()

        gunung_urut = quicksort_ke_kecil(gunung, key=lambda x: x[2])
        headers = ["ID", "Nama Gunung", "Tinggi", "Level", "Harga Tiket","Kota" ,"Provinsi"]
        print(tabulate(gunung_urut, headers=headers, tablefmt="grid"))
        conn.commit()
    except Exception as e:
        print(f"Error: {e}")
        conn.rollback()
    finally:
        cur.close()
        conn.close()

# GUNUNG URUT HARGA ASC
def display_gunung_urut_harga_asc():
    conn = get_db_connection()
    cur = conn.cursor()
    try:
        cur.execute(
            "select g.gunung_id, g.nama_gunung, g.tinggi, le.level_id, g.harga, k.nama_kota, p.nama_provinsi from loket lo join kota k on (k.kota_id = lo.kota_kota_id) join gunung g on (lo.gunung_gunung_id = g.gunung_id) join level le on (g.level_level_id = le.level_id) join provinsi p on (p.provinsi_id = k.provinsi_provinsi_id)"
            )
        gunung = cur.fetchall()

        gunung_urut = quicksort_ke_besar(gunung, key=lambda x: x[4])
        headers = ["ID", "Nama Gunung", "Tinggi", "Level", "Harga Tiket","Kota" ,"Provinsi"]
        print(tabulate(gunung_urut, headers=headers, tablefmt="grid"))
        conn.commit()
    except Exception as e:
        print(f"Error: {e}")
        conn.rollback()
    finally:
        cur.close()
        conn.close()

# GUNUNG URUT HARGA DESC
def display_gunung_urut_harga_desc():
    conn = get_db_connection()
    cur = conn.cursor()
    try:
        cur.execute(
            "select g.gunung_id, g.nama_gunung, g.tinggi, le.level_id, g.harga, k.nama_kota, p.nama_provinsi from loket lo join kota k on (k.kota_id = lo.kota_kota_id) join gunung g on (lo.gunung_gunung_id = g.gunung_id) join level le on (g.level_level_id = le.level_id) join provinsi p on (p.provinsi_id = k.provinsi_provinsi_id)"
            )
        gunung = cur.fetchall()

        gunung_urut = quicksort_ke_kecil(gunung, key=lambda x: x[4])
        headers = ["ID", "Nama Gunung", "Tinggi", "Level", "Harga Tiket","Kota" ,"Provinsi"]
        print("="*100)
        print("DATA GUNUNG".center(100))
        print("="*100)
        print(tabulate(gunung_urut, headers=headers, tablefmt="grid"))
        conn.commit()
    except Exception as e:
        print(f"Error: {e}")
        conn.rollback()
    finally:
        cur.close()
        conn.close()

# GUNUNG URUT LEVEL ASC
def display_gunung_urut_level_asc():
    conn = get_db_connection()
    cur = conn.cursor()
    try:
        cur.execute(
            "select g.gunung_id, g.nama_gunung, g.tinggi, le.level_id, g.harga, k.nama_kota, p.nama_provinsi from loket lo join kota k on (k.kota_id = lo.kota_kota_id) join gunung g on (lo.gunung_gunung_id = g.gunung_id) join level le on (g.level_level_id = le.level_id) join provinsi p on (p.provinsi_id = k.provinsi_provinsi_id)"
            )
        gunung = cur.fetchall()

        gunung_urut = quicksort_ke_besar(gunung, key=lambda x: x[3])
        headers = ["ID", "Nama Gunung", "Tinggi", "Level", "Harga Tiket","Kota" ,"Provinsi"]
        print(tabulate(gunung_urut, headers=headers, tablefmt="grid"))
        conn.commit()
    except Exception as e:
        print(f"Error: {e}")
        conn.rollback()
    finally:
        cur.close()
        conn.close()

# GUNUNG URUT LEVEL DESC
def display_gunung_urut_level_desc():
    conn = get_db_connection()
    cur = conn.cursor()
    try:
        cur.execute(
            "select g.gunung_id, g.nama_gunung, g.tinggi, le.level_id, g.harga, k.nama_kota, p.nama_provinsi from loket lo join kota k on (k.kota_id = lo.kota_kota_id) join gunung g on (lo.gunung_gunung_id = g.gunung_id) join level le on (g.level_level_id = le.level_id) join provinsi p on (p.provinsi_id = k.provinsi_provinsi_id)"
            )
        gunung = cur.fetchall()

        gunung_urut = quicksort_ke_kecil(gunung, key=lambda x: x[3])
        headers = ["ID", "Nama Gunung", "Tinggi", "Level", "Harga Tiket","Kota" ,"Provinsi"]
        print(tabulate(gunung_urut, headers=headers, tablefmt="grid"))
        conn.commit()
    except Exception as e:
        print(f"Error: {e}")
        conn.rollback()
    finally:
        cur.close()
        conn.close()

def customer_id_cari(username):
    conn = get_db_connection()
    cur = conn.cursor()
    try:
        cur.execute("SELECT customer_id FROM customer WHERE username = %s", (username,))
        result = cur.fetchone()
        if result:
            return result[0]
        else:
            print("Customer tidak ditemukan.")
            return None
    except Exception as e:
        print(f"Error getting customer ID: {e}")
    finally:
        cur.close()
        conn.close()


def admin_cari(nama_hari, waktu_pesan):
    conn = get_db_connection()
    cur = conn.cursor()
    try:
        jam_pesan = waktu_pesan.strftime('%H:%M:%S')

        cur.execute("SELECT a.admin_id FROM admin a JOIN detail_shift ds ON a.admin_id = ds.admin_admin_id JOIN shift s ON ds.shift_shift_id = s.shift_id WHERE s.hari_shift = %s AND s.jam_awal_shift <= %s AND s.jam_akhir_shift >= %s", (nama_hari, jam_pesan, jam_pesan))
        id_admin = cur.fetchone()
        
        if id_admin:
            return id_admin[0]
        else:
            print("Tidak ada admin yang tersedia untuk melayani pada waktu yang diminta.")
            return None
    except Exception as e:
        print(f"Error getting admin ID: {e}")
        return None
    finally:
        cur.close()
        conn.close()

def display_selected_gunung(gunung_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT g.gunung_id, g.nama_gunung, g.tinggi, g.harga, l.deskripsi_level, k.nama_kota FROM gunung g JOIN level l ON g.level_level_id = l.level_id JOIN loket lo ON g.gunung_id = lo.gunung_gunung_id JOIN kota k ON lo.kota_kota_id = k.kota_id WHERE g.gunung_id = %s", (gunung_id,))
    selected_gunung = cur.fetchone()
    if selected_gunung:
        print(tabulate([selected_gunung], headers=["ID Gunung", "Nama Gunung", "Tinggi", "Harga", "Level", "Loket"], tablefmt="pretty"))
    else:
        print("Gunung tidak ditemukan.")


def pemesanan(username):
    gunung_id = int(input("Masukkan ID Gunung yang ingin dipesan: "))
    display_selected_gunung(gunung_id)
    tanggal_pesan = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    tanggal_pesan_datetime = datetime.strptime(tanggal_pesan, "%Y-%m-%d %H:%M:%S")
    tanggal_daki = input("Masukkan Tanggal Daki (YYYY-MM-DD): ")
    quantity = int(input("Masukkan Jumlah Pendaki: "))
    hari = tanggal_pesan_datetime.strftime("%A")
    waktu_pesan = datetime.now().time()
    nama_hari = str(hari)
    
    id_admin = admin_cari(nama_hari, waktu_pesan)
    id_user = customer_id_cari(username)
    
    if id_user is None:
        print("Tidak dapat menemukan ID customer. Pemesanan gagal.")
        return

    conn = get_db_connection()
    cur = conn.cursor()
    try:
        cur.execute("INSERT INTO pemesanan (tanggal_pesan, tanggal_daki, quantity, admin_admin_id, customer_customer_id, gunung_gunung_id) VALUES (%s, %s, %s, %s, %s, %s)",
                    (tanggal_pesan, tanggal_daki, quantity, id_admin, id_user, gunung_id))
        conn.commit()
        print("Pemesanan berhasil!")
    except Exception as e:
        print(f"Error: {e}")
        conn.rollback()
    finally:
        cur.close()
        conn.close()

def hitung_total_harga(pemesanan_id):
    conn = get_db_connection()
    cur = conn.cursor()
    try:
        cur.execute("SELECT quantity, gunung_gunung_id FROM pemesanan WHERE pemesanan_id = %s", (pemesanan_id,))
        pemesanan_data = cur.fetchone()
        if not pemesanan_data:
            print("Pemesanan tidak ditemukan.")
            return None
        
        quantity = pemesanan_data[0]
        gunung_id = pemesanan_data[1]
        
        cur.execute("SELECT harga FROM gunung WHERE gunung_id = %s", (gunung_id,))
        gunung_data = cur.fetchone()
        if not gunung_data:
            print("Gunung tidak ditemukan.")
            return None
        
        harga = gunung_data[0]
        
        total_harga = quantity * harga
        return total_harga
    except Exception as e:
        print(f"Error calculating total price: {e}")
        return None
    finally:
        cur.close()
        conn.close()

def metode_pembayaran():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT metode_id, nama_metode, no_rekening, nama_pemilik_rekening_rekening FROM metode")
    methods = cur.fetchall()
    cur.close()
    conn.close()
    return methods

def pemesanan_id_cari(customer_id):
    conn = get_db_connection()
    cur = conn.cursor()
    try:
        cur.execute("SELECT pemesanan_id FROM pemesanan WHERE customer_customer_id = %s  ORDER BY pemesanan_id DESC LIMIT 1", (customer_id,))
        pemesanan_id = cur.fetchone()[0]
        return pemesanan_id
    except Exception as e:
        print(f"Error getting customer ID: {e}")
    finally:
        cur.close()
        conn.close()

def bukti_bayar(pemesanan_id, bukti_bayar):
    conn = get_db_connection()
    cur = conn.cursor()
    try:
        cur.execute(
            "UPDATE pembayaran SET bukti_bayar = %s WHERE pemesanan_pemesanan_id = %s",
            (bukti_bayar, pemesanan_id)
        )
        conn.commit()
        print("Bukti pembayaran berhasil disimpan ke database.")
    except Exception as e:
        print(f"Error: {e}")
        conn.rollback()
    finally:
        cur.close()
        conn.close()

def simpan_pembayaran(total, status, bukti_pembayaran, metode_pembayaran_id, id_pemesanan):
    conn = get_db_connection()
    cur = conn.cursor()
    try:
        cur.execute(
            "INSERT INTO pembayaran (total, status, bukti_bayar, metode_metode_id, pemesanan_pemesanan_id) VALUES (%s, %s, %s, %s, %s)",
            (total, status, bukti_pembayaran, metode_pembayaran_id, id_pemesanan)
        )
        conn.commit()
    except Exception as e:
        print(f"Error saving detail reservation: {e}")
        conn.rollback()
    finally:
        cur.close()
        conn.close()

# DISPLAY CUSTOMER URUT NAMA ASC
def display_urut_customer_asc():
    conn = get_db_connection()
    cur = conn.cursor()
    try:
        cur.execute(
            "SELECT c.nama_lengkap, c.nik, c.telepon, c.tanggal_lahir, c.alamat, k.nama_kota, p.nama_provinsi FROM customer c JOIN kota k ON c.kota_kota_id = k.kota_id JOIN provinsi p ON k.provinsi_provinsi_id = p.provinsi_id"
            )
        customer = cur.fetchall()

        customer_urut = quicksort_ke_besar(customer, key=lambda x: x[0].casefold())
        print(tabulate(customer_urut, headers=["Nama Lengkap", "NIK", "Telepon", "Tanggal Lahir", "Alamat", "Kota", "Provinsi"], tablefmt="pretty"))

        conn.commit()
    except Exception as e:
        print(f"Error: {e}")
        conn.rollback()
    finally:
        cur.close()
        conn.close()

# DISPLAY CUSTOMER URUT NAMA DESC
def display_urut_customer_desc():
    conn = get_db_connection()
    cur = conn.cursor()
    try:
        cur.execute(
            "SELECT c.nama_lengkap, c.nik, c.telepon, c.tanggal_lahir, c.alamat, k.nama_kota, p.nama_provinsi FROM customer c JOIN kota k ON c.kota_kota_id = k.kota_id JOIN provinsi p ON k.provinsi_provinsi_id = p.provinsi_id"
            )
        customer = cur.fetchall()

        customer_urut = quicksort_ke_kecil(customer, key=lambda x: x[0].casefold())
        print(tabulate(customer_urut, headers=["Nama Lengkap", "NIK", "Telepon", "Tanggal Lahir", "Alamat", "Kota", "Provinsi"], tablefmt="pretty"))

        conn.commit()
    except Exception as e:
        print(f"Error: {e}")
        conn.rollback()
    finally:
        cur.close()
        conn.close()


# DATA ADMIN
def display_admin():
    conn = get_db_connection()  
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    try:
        cursor.execute("SELECT admin_id, nama_lengkap, telepon, username FROM admin ORDER BY admin_id;") 
        admin = cursor.fetchall()
        data = []
        for admin in admin:
            id = admin ["admin_id"]
            name = admin['nama_lengkap']
            telp = admin['telepon']
            username = admin['username']
            data.append([id, name, telp, username])
        
        headers = ["ID", "Nama", "No. Telp", "Username"]
        print(tabulate(data, headers=headers, tablefmt="grid"))
    except psycopg2.Error as e:
        print("Error:", e)
    finally:
        cursor.close()
        conn.close()

def create_admin(nama, no_telp, username, password):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        cursor.execute("INSERT INTO admin (nama_lengkap, telepon, username, password) VALUES (%s, %s, %s, %s);",
        (nama, no_telp, username, hashed_password))
        conn.commit()
        print("Data admin berhasil ditambahkan!")
    except psycopg2.Error as e:
        conn.rollback()
        print("Error:", e)
    finally:
        cursor.close()
        conn.close()

def update_admin(id_admin, nama, no_telp, username, password):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        cursor.execute("UPDATE admin SET nama_lengkap = %s, telepon = %s, username = %s, password = %s WHERE admin_id = %s;",
        (nama, no_telp, username, hashed_password, id_admin))
        conn.commit()
        print("Data admin berhasil diperbarui!")
    except psycopg2.Error as e:
        conn.rollback()
        print("Error:", e)
    finally:
        cursor.close()
        conn.close()

def display_urut_admin_asc():
    conn = get_db_connection()
    cur = conn.cursor()
    try:
        cur.execute(
            "SELECT admin_id, nama_lengkap, telepon, username FROM admin ORDER BY admin_id;"
            )
        admin = cur.fetchall()

        admin_urut = quicksort_ke_besar(admin, key=lambda x: x[1].casefold())
        print(tabulate(admin_urut, headers=["ID", "Nama Lengkap", "No. Telp", "Username"], tablefmt="pretty"))

        conn.commit()
    except Exception as e:
        print(f"Error: {e}")
        conn.rollback()
    finally:
        cur.close()
        conn.close()

def cari_nama_admin(conn, nama_admin):
    cur = conn.cursor()
    hasil_admin = []
    try:
        cur.execute(
            "SELECT admin_id, nama_lengkap, telepon, username FROM admin ORDER BY nama_lengkap ;"
        )
        admin = cur.fetchall()
        nama_admin = nama_admin.lower()
        indeks = 1
        index = binary_search(admin, nama_admin, indeks)
        if index != -1:
            hasil_admin.append(admin[index])
            kiri = index - 1
            kanan = index + 1
            while kiri >= 0 and admin[kiri][indeks].lower().startswith(nama_admin):
                hasil_admin.append(admin[kiri])
                kiri -= 1
            while kanan < len(admin) and admin[kanan][indeks].lower().startswith(nama_admin):
                hasil_admin.append(admin[kanan])
                kanan += 1
        conn.commit()
    except Exception as e:
        print(f"Error: {e}")
        conn.rollback()
    finally:
        cur.close()
    return hasil_admin

def display_cari_nama_admin():
    conn = get_db_connection()
    try:
        nama_admin = input("Masukkan nama admin yang ingin dicari: ")
        hasil_admin = cari_nama_admin(conn, nama_admin)
        if hasil_admin:
            print(tabulate(hasil_admin, headers=["ID Admin", "Nama Lengkap", "Telepon", "Username"], tablefmt="pretty"))
        else:
            print("Admin dengan nama", nama_admin, "tidak ditemukan.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        conn.close()

# Data Shift
def display_shift():
    conn = get_db_connection()  
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    try:
        cursor.execute("SELECT shift_id, tanggal_berlaku, tanggal_berakhir, hari_shift, jam_awal_shift, jam_akhir_shift FROM shift ORDER BY shift_id;") 
        shifts = cursor.fetchall()
        data = []
        for shift in shifts:
            id = shift['shift_id']
            tanggal_berlaku = shift ['tanggal_berlaku']
            tanggal_berakhir = shift ['tanggal_berakhir']
            hari = shift['hari_shift']
            jam_awal = shift['jam_awal_shift']
            jam_akhir = shift['jam_akhir_shift']
            data.append([id, tanggal_berlaku, tanggal_berakhir, hari, jam_awal, jam_akhir ])
        
        headers = ["ID", "Tanggal Berlaku", "Tanggal Berakhir", "Hari", "Jam Awal", "Jam Akhir"]
        print(tabulate(data, headers=headers, tablefmt="grid"))
    except psycopg2.Error as e:
        print("Error:", e)
    finally:
        cursor.close()
        conn.close()

def create_shift(tanggal_berlaku, tanggal_berakhir, hari_shift, jam_awal_shift, jam_akhir_shift):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO shift (tanggal_berlaku, tanggal_berakhir, hari_shift, jam_awal_shift, jam_akhir_shift) VALUES (%s, %s, %s, %s, %s);",
        (tanggal_berlaku, tanggal_berakhir, hari_shift, jam_awal_shift, jam_akhir_shift))
        conn.commit()
        print("Data jadwal shift berhasil ditambahkan!")
    except psycopg2.Error as e:
        conn.rollback()
        print("Error:", e)
    finally:
        cursor.close()
        conn.close()

def update_shift(shift_id, tanggal_berlaku, tanggal_berakhir, hari_shift, jam_awal_shift, jam_akhir_shift):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("UPDATE shift SET tanggal_berlaku = %s, tanggal_berakhir = %s, hari_shift = %s, jam_awal_shift = %s, jam_akhir_shift = %s WHERE shift_id = %s;",
        (tanggal_berlaku, tanggal_berakhir, hari_shift, jam_awal_shift, jam_akhir_shift, shift_id))
        conn.commit()
        print("Data jadwal shift berhasil diperbarui!")
    except psycopg2.Error as e:
        conn.rollback()
        print("Error:", e)
    finally:
        cursor.close()
        conn.close()

def delete_shift(id_detail_shift):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM detail_shift WHERE id_detail_shift = %s;", (id_detail_shift,))

        conn.commit()
        if cursor.rowcount > 0:
            print(f"Detail shift dengan ID {id_detail_shift} berhasil dihapus.")
        else:
            print(f"Tidak ada ID {id_detail_shift} dalam detail shift.")
        
    except psycopg2.Error as e:
        conn.rollback()
        print("Error:", e)
    finally:
        cursor.close()
        conn.close()

# Data Metode Pembayaran
def display_metode():
    conn = get_db_connection()  
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    try:
        cursor.execute("SELECT metode_id, nama_metode, no_rekening, nama_pemilik_rekening FROM metode ORDER BY metode_id;") 
        cara = cursor.fetchall()
        data = []
        for metode in cara:
            id = metode['metode_id']
            nama = metode ['nama_metode']
            no_rek = metode ['no_rekening']
            pemilik = metode['nama_pemilik_rekening']
            data.append([id, nama, no_rek, pemilik])
        
        headers = ["ID", "Nama Metode", "No Rek", "Pemilik"]
        print(tabulate(data, headers=headers, tablefmt="grid"))
    except psycopg2.Error as e:
        print("Error:", e)
    finally:
        cursor.close()
        conn.close()

def create_metode_pembayaran(nama_metode, no_rekening, nama_pemilik_rekening):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO metode (nama_metode, no_rekening, nama_pemilik_rekening) VALUES (%s, %s, %s);", 
        (nama_metode, no_rekening, nama_pemilik_rekening))
        conn.commit()
        print("Data metode pembayaran berhasil ditambahkan!")
    except psycopg2.Error as e:
        conn.rollback()
        print("Error:", e)
    finally:
        cursor.close()
        conn.close()

def update_metode_pembayaran(metode_id, nama_metode, no_rekening, nama_pemilik_rekening):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("UPDATE metode SET nama_metode = %s, no_rekening = %s, nama_pemilik_rekening = %s WHERE metode_id = %s;", 
        (nama_metode, no_rekening, nama_pemilik_rekening, metode_id))
        conn.commit()
        print("Data metode pembayaran berhasil diperbarui!")
    except psycopg2.Error as e:
        conn.rollback()
        print("Error:", e)
    finally:
        cursor.close()
        conn.close()

# Data Detail Shift
def display_detail_shift():
    conn = get_db_connection()  
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    try:
        cursor.execute("SELECT ds.id_detail_shift, ds.admin_admin_id, k.nama_lengkap, ds.shift_shift_id, s.tanggal_berlaku, s.tanggal_berakhir, s.hari_shift, s.jam_awal_shift, s.jam_akhir_shift FROM detail_shift ds JOIN admin k ON ds.admin_admin_id = k.admin_id JOIN shift s ON ds.shift_shift_id = s.shift_id ORDER BY admin_id;") 
        shifts = cursor.fetchall()
        data = []
        for shift in shifts:
            detail_id = shift['id_detail_shift']
            admin_id = shift['admin_admin_id']
            nama_admin = shift['nama_lengkap']
            shift_id = shift['shift_shift_id']
            tanggal_berlaku = shift['tanggal_berlaku']
            tanggal_berakhir = shift['tanggal_berakhir']
            hari_shift = shift['hari_shift']
            jam_awal = shift['jam_awal_shift']
            jam_akhir = shift['jam_akhir_shift']
            data.append([detail_id, admin_id, nama_admin, hari_shift, jam_awal, jam_akhir, shift_id, tanggal_berlaku, tanggal_berakhir])
        
        headers = ["ID Detail", "ID admin", "Nama Admin", "Hari Shift", "Jam Awal", "Jam Akhir", "ID Shift", "Tanggal Berlaku", "Tanggal Berakhir"]
        print(tabulate(data, headers=headers, tablefmt="grid"))
    except psycopg2.Error as e:
        print("Error:", e)
    finally:
        cursor.close()
        conn.close()

def create_detail_shift(admin_id, shift_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO detail_shift (admin_admin_id, shift_shift_id) VALUES (%s, %s);",
        (admin_id, shift_id))
        conn.commit()
        print("Data detail shift berhasil ditambahkan!")
    except psycopg2.Error as e:
        conn.rollback()
        print("Error:", e)
    finally:
        cursor.close()
        conn.close()

def update_detail_shift(admin_id, shift_id, detail_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("UPDATE detail_shift SET admin_admin_id = %s, shift_shift_id = %s WHERE id_detail_shift = %s;",
        (admin_id, shift_id, detail_id))
        conn.commit()
        print("Data detail shift berhasil diperbarui!")
    except psycopg2.Error as e:
        conn.rollback()
        print("Error:", e)
    finally:
        cursor.close()
        conn.close()

def display_pembayaran():
    conn = get_db_connection()  
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    try:
        cursor.execute("SELECT pb.pembayaran_id, pb.total, pb.status, pb.bukti_bayar, m.nama_metode, pb.pemesanan_pemesanan_id FROM pembayaran pb JOIN metode m ON pb.metode_metode_id = m.metode_id ;") 
        pembayaran = cursor.fetchall()
        data = []
        for bayar in pembayaran:
            pembayaran_id = bayar['pembayaran_id']
            total = bayar['total']
            status = bayar['status']
            bukti_bayar = bayar['bukti_bayar']
            metode = bayar['nama_metode']
            pemesanan = bayar['pemesanan_pemesanan_id']
            data.append([pembayaran_id, total, bukti_bayar, status, metode, pemesanan])
        
        headers = ["ID Pembayaran", "Total Bayar", "Bukti Bayar", "Status Bayar", "Metode Pembayaran", "ID Pemesanan"]
        print(tabulate(data, headers=headers, tablefmt="grid"))
    except psycopg2.Error as e:
        print("Error:", e)
    finally:
        cursor.close()
        conn.close()

def update_status_pembayaran(id_detail, status_pembayaran):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("UPDATE pembayaran SET status = %s WHERE pembayaran_id = %s;""",
        (status_pembayaran, id_detail))
        conn.commit()
        print("Status pembayaran detail pemesanan berhasil diperbarui!")
    except psycopg2.Error as e:
        conn.rollback()
        print("Error:", e)
    finally:
        cursor.close()
        conn.close()

# Data pemesanan
def display_pemesanan():
    conn = get_db_connection()  
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    try:
        cursor.execute("SELECT ps.pemesanan_id, ps.tanggal_pesan, ps.tanggal_daki, ps.quantity, c.nama_lengkap, a.nama_lengkap as nama_admin FROM pemesanan ps JOIN customer c ON ps.customer_customer_id = c.customer_id JOIN admin a ON ps.admin_admin_id = a.admin_id ORDER BY pemesanan_id;") 
        pesan = cursor.fetchall()
        data = []
        for pemesanan in pesan:
            id = pemesanan['pemesanan_id']
            tanggal_pesan = pemesanan ['tanggal_pesan']
            tanggal_daki = pemesanan ['tanggal_daki']
            quantity = pemesanan ['quantity']
            customer = pemesanan['nama_lengkap']
            admin = pemesanan['nama_admin']
            data.append([id, tanggal_pesan, tanggal_daki, quantity, customer, admin])
        
        headers = ["ID", "Tanggal pemesanan", "Tanggal Jadwal", "Quantity", "Nama Customer", "Nama admin"]
        print(tabulate(data, headers=headers, tablefmt="grid"))
    except psycopg2.Error as e:
        print("Error:", e)
    finally:
        cursor.close()
        conn.close()


def display_level():
    conn = get_db_connection()  
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    try:
        cursor.execute("SELECT level_id, deskripsi_level FROM level ORDER BY level_id;") 
        levels = cursor.fetchall()
        data = []
        for level in levels:
            id = level['level_id']
            deskripsi = level ['deskripsi_level']
            data.append([id, deskripsi])
        
        headers = ["ID", "Deskripsi Level"]
        print(tabulate(data, headers=headers, tablefmt="grid"))
    except psycopg2.Error as e:
        print("Error:", e)
    finally:
        cursor.close()
        conn.close()

def create_level(deskripsi_level):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO level (deskripsi_level) VALUES (%s) RETURNING level_id;", (deskripsi_level,))
        level_id = cursor.fetchone()[0]
        conn.commit()
        return level_id
    except psycopg2.Error as e:
        print("Error:", e)
        conn.rollback()
    finally:
        cursor.close()
        conn.close()

def update_level(level_id, deskripsi_level):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("UPDATE level SET deskripsi_level = %s WHERE level_id = %s;", (deskripsi_level, level_id))
        conn.commit()
    except psycopg2.Error as e:
        print("Error:", e)
        conn.rollback()
    finally:
        cursor.close()
        conn.close()

def display_loket():
    conn = get_db_connection()  
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    try:
        cursor.execute("SELECT lo.loket_id, k.nama_kota, g.nama_gunung FROM loket lo JOIN kota k ON lo.kota_kota_id = k.kota_id JOIN gunung g ON lo.gunung_gunung_id = g.gunung_id;") 
        lokets = cursor.fetchall()
        data = []
        for loket in lokets:
            id = loket['loket_id']
            kota = loket ['nama_kota']
            gunung = loket ['nama_gunung']
            data.append([id, kota, gunung])
        
        headers = ["ID", "Kota", "Gunung"]
        print(tabulate(data, headers=headers, tablefmt="grid"))
    except psycopg2.Error as e:
        print("Error:", e)
    finally:
        cursor.close()
        conn.close()

def create_loket(kota_kota_id, gunung_gunung_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO loket (kota_kota_id, gunung_gunung_id) VALUES (%s, %s) RETURNING loket_id;", (kota_kota_id, gunung_gunung_id))
        loket_id = cursor.fetchone()[0]
        conn.commit()
        return loket_id
    except psycopg2.Error as e:
        print("Error:", e)
        conn.rollback()
    finally:
        cursor.close()
        conn.close()

def update_loket(loket_id, kota_kota_id, gunung_gunung_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("UPDATE loket SET kota_kota_id = %s, gunung_gunung_id = %s WHERE loket_id = %s;", (kota_kota_id, gunung_gunung_id, loket_id))
        conn.commit()
    except psycopg2.Error as e:
        print("Error:", e)
        conn.rollback()
    finally:
        cursor.close()
        conn.close()

def delete_loket(loket_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM loket WHERE loket_id = %s;", (loket_id,))
        conn.commit()
    except psycopg2.Error as e:
        print("Error:", e)
        conn.rollback()
    finally:
        cursor.close()
        conn.close()

        
def display_kota():
    conn = get_db_connection()  
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    try:
        cursor.execute("SELECT k.kota_id, k.nama_kota, p.nama_provinsi FROM kota k JOIN provinsi p ON k.provinsi_provinsi_id = p.provinsi_id;") 
        kotas = cursor.fetchall()
        data = []
        for kota in kotas:
            id = kota['kota_id']
            kota = kota ['nama_kota']
            provinsi = kota ['nama_provinsi']
            data.append([id, kota, provinsi])
        
        headers = ["ID", "Kota", "Provinsi"]
        print(tabulate(data, headers=headers, tablefmt="grid"))
    except psycopg2.Error as e:
        print("Error:", e)
    finally:
        cursor.close()
        conn.close()

def cari_gunung_id(nama_gunung):
    conn = get_db_connection()
    cur = conn.cursor()
    try:
        cur.execute("SELECT gunung_id FROM gunung WHERE nama_gunung = %s", (nama_gunung,))
        row = cur.fetchone()
        if row:
            return row[0] 
        else:
            return None
    except psycopg2.Error as e:
        print("Error:", e)
    finally:
        cur.close()
        conn.close()

def create_gunung(nama_gunung, tinggi, harga, level_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO gunung (nama_gunung, tinggi, harga, level_level_id) VALUES (%s, %s, %s, %s)",
            (nama_gunung, tinggi, harga, level_id)
        )
        conn.commit()
        print("Data gunung berhasil ditambahkan.")
    except psycopg2.Error as e:
        print("Error:", e)
    finally:
        cursor.close()
        conn.close()


def update_gunung(gunung_id, nama_gunung, tinggi, harga, level_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("UPDATE gunung SET nama_gunung=%s, tinggi=%s, harga=%s, level_level_id=%s WHERE gunung_id=%s",
                       (nama_gunung, tinggi, harga, level_id, gunung_id))
        conn.commit()
        print("Data gunung berhasil diperbarui.")
    except psycopg2.Error as e:
        print("Error:", e)
    finally:
        cursor.close()
        conn.close()