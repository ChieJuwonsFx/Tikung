import os
from tabulate import tabulate
import function as fn

def display_customer_data(username, password, nama, nik, telepon, tanggal_lahir, alamat, kota, provinsi):
    data = [[username, password, nama, nik, telepon, tanggal_lahir, alamat, kota, provinsi]]
    headers = ["Username", "Password" ,"Nama", "NIK", "No. Telp", "Tanggal Lahir", "Alamat", "Kota", "Provinsi"]
    print(tabulate(data, headers=headers, tablefmt="grid"))

def regist_proses():
    while True:
        print("="*100)
        print("REGISTER".center(100))
        print("="*100)
        
        while True:
            username = input('Masukkan username (minimal 8 karakter): ')
            if len(username) < 8:
                print('Username harus minimal 8 karakter. Silakan coba lagi.')
            else:
                break

        while True:
            password = input('Masukkan password (minimal 8 karakter): ')
            if len(password) < 8:
                print('Password harus minimal 8 karakter. Silakan coba lagi.')
            else:
                break
                
        nama = input("Nama lengkap: ")
        nik = input("NIK: ")
        telepon = input("Telepon: ")
        tanggal_lahir = input("Tanggal lahir (yyyy-mm-dd): ")
        alamat = input("Alamat: ")
        kota = input("Kota: ")
        provinsi = input("Provinsi: ")
        
        print("="*100)
        print("REGISTER".center(100))
        print("="*100)
        
        display_customer_data(username, password, nama, nik, telepon, tanggal_lahir, alamat, kota, provinsi)
        
        print("|1| Konfirmasi data\n|2| Batalkan registrasi")
        pilih = input("Tekan enter untuk isi ulang data: ")
        
        if pilih == "1":
            fn.register_customer(username, password, nama, nik, telepon, tanggal_lahir, alamat, kota, provinsi)
            break
        elif pilih == "2":
            break

def pembayaran(id_user):
    os.system('cls')
    methods = fn.metode_pembayaran()
    print("\nPilih Metode Pembayaran:")
    for method in methods:
        print(f"{method[0]}. {method[1]}")

    while True:
        try:
            metode_pembayaran_id = int(input("\nMasukkan ID metode pembayaran: "))
            selected_method = next((method for method in methods if method[0] == metode_pembayaran_id), None)
            if selected_method:
                no_rek = selected_method[2]
                nama_pemilik = selected_method[3]

                print(f"\nSilakan transfer ke rekening berikut:")
                print(f"Nomor Rekening: {no_rek}")
                print(f"Nama Pemilik: {nama_pemilik}")

                os.system('cls')
                bukti_pembayaran = input("Masukkan link bukti pembayaran: ")
                print(f"Terima kasih! Bukti pembayaran Anda telah diunggah dengan link: {bukti_pembayaran}")
                status = "Pending"
                id_pemesanan = fn.pemesanan_id_cari(id_user)
                total = fn .hitung_total_harga(id_pemesanan)
                fn.bukti_bayar(id_pemesanan, bukti_pembayaran)
                fn.simpan_pembayaran(total, status, bukti_pembayaran, metode_pembayaran_id, id_pemesanan)
                break
            else:
                print("ID metode pembayaran tidak valid. Silakan coba lagi.")
        except ValueError:
            print("ID metode pembayaran harus berupa angka.")

def daftar_menu_admin():
    # os.system('cls')
    print("\n" + "+" + "-"*50 + "+")
    print("|{:^50}|".format("MENU"))
    print("+" + "-"*50 + "+")
    print("|{:<50}|".format("1. Data Gunung"))
    print("|{:<50}|".format("2. Data Loket")) 
    print("|{:<50}|".format("3. Data Level"))
    print("|{:<50}|".format("4. Data Customer"))
    print("|{:<50}|".format("5. Data Admin"))
    print("|{:<50}|".format("6. Data Riwayat"))
    print("|{:<50}|".format("7. Data Jam Shift"))     
    print("|{:<50}|".format("8. Data Metode Pembayaran")) 
    print("|{:<50}|".format("9. Data Pemesanan")) 
    print("|{:<50}|".format("10. Data Pembayaran"))
    print("|{:<50}|".format("11. Data Jadwal Shift Karyawan"))      
    print("|{:<50}|".format("12. Keluar"))           
    print("+" + "-"*50 + "+")

def admin_menu():
    while True:
        os.system('cls')
        print("="*100)
        print("ANDA MASUK SEBAGAI ADMIN".center(100))
        print("="*100)
        username = input("Username: ")
        password = input("Password: ")
        admin = fn.login_admin(username, password)
        if admin:
            menu_admin(True, admin)
            break
        else:
            while True:
                os.system('cls')
                print("="*100)
                print("USERNAME ATAU PASSWORD SALAH".center(100))
                print("="*100)
                print("[1] Retry\n[2] Exit")
                opsi = input("Pilihan: ")
                if opsi == "1":
                    break
                elif opsi == "2":
                    return
                
def menu_admin(akses, id_admin):
    while akses:
        # os.system('cls')
        print("="*100)
        print("MAIN MENU".center(100))
        print("="*100)
        daftar_menu_admin()
        pilihan = input("Pilih Menu: ")
        if pilihan == "1":
            # os.system('cls')
            print("+" + "-"*50 + "+")
            print("|{:^50}|".format("Data Gunung"))
            print("+" + "-"*50 + "+")
            fn.display_gunung()

            print("+" + "-"*50 + "+")
            print("|{:<50}|".format("1. Tambah Gunung"))
            print("|{:<50}|".format("2. Update Gunung"))
            print("|{:<50}|".format("3. Kembali"))
            print("|{:<50}|".format("4. Keluar"))
            print("+" + "-"*50 + "+")
            pilihan = input('Pilih menu: ')
            if pilihan == '1':
                # os.system('cls')
                nama_gunung = input("Masukkan nama gunung: ")
                tinggi = int(input("Masukkan tinggi gunung: "))
                harga = int(input("Masukkan harga gunung: "))
                fn.display_level()
                level = int(input("Masukkan ID level: "))
                fn.create_gunung(nama_gunung, tinggi, harga, level)
                while True:
                    fn.create_loket_loop(nama_gunung)               
                    konfirmasi = input("Apakah Anda ingin menambahkan loket lagi di kota yang sama? (y/n): ").strip().lower()
                    if konfirmasi != 'y':
                        break 
                
            elif pilihan == "2":
                # os.system('cls')
                fn.display_gunung()
                id_gunung = int(input("Masukkan ID gunung yang ingin diperbaharui: "))
                nama_gunung = input("Masukkan nama gunung: ")
                tinggi = int(input("Masukkan tinggi gunung: "))
                harga = int(input("Masukkan harga gunung: "))
                fn.display_level()
                level = int(input("Masukkan ID level: "))
                fn.update_gunung(id_gunung,nama_gunung,tinggi,harga,level)
            elif pilihan == "3":
                # os.system('cls')
                daftar_menu_admin()
            elif pilihan == "4":
                break
        elif pilihan == '2':
            # os.system('cls')
            print("+" + "-"*50 + "+")
            print("|{:^50}|".format("Data Loket"))
            print("+" + "-"*50 + "+")
            fn.display_loket()

            print("+" + "-"*50 + "+")
            print("|{:<50}|".format("1. Tambah Loket"))
            print("|{:<50}|".format("2. Update Loket"))
            print("|{:<50}|".format("3. Hapus Loket"))
            print("|{:<50}|".format("4. Kembali"))
            print("|{:<50}|".format("5. Keluar"))
            print("+" + "-"*50 + "+")
            pilihan = input('Pilih menu: ')
            if pilihan == '1':
                # os.system('cls')
                fn.display_kota()
                kota = int(input("Masukkan ID Kota: "))
                fn.display_gunung()
                gunung = int(input ("Masukkan ID Gunung: "))
                fn.create_loket(kota, gunung)
            elif pilihan == '2':
                # os.system('cls')
                fn.display_loket()
                id_loket = int(input("Masukkan ID loket yang ingin diperbaharui: "))
                fn.display_kota()
                kota = int(input("Masukkan ID Kota: "))
                fn.display_gunung()
                gunung = int(input ("Masukkan ID Gunung: "))
                fn.update_loket(id_loket, kota, gunung)
            elif pilihan == '3':
                # os.system('cls')
                fn.display_loket()
                id_loket = int(input("Masukkan ID loket yang ingin dihapus: "))
                fn.delete_loket(id_loket)
            elif pilihan == '4':
                # os.system('cls')
                daftar_menu_admin()
            elif pilihan == '5':
                break
        elif pilihan == '3':
            # os.system('cls')
            print("+" + "-"*50 + "+")
            print("|{:^50}|".format("Data Level"))
            print("+" + "-"*50 + "+")
            fn.display_level()

            print("+" + "-"*50 + "+")
            print("|{:<50}|".format("1. Tambah Level"))
            print("|{:<50}|".format("2. Update Level"))
            print("|{:<50}|".format("3. Kembali"))
            print("|{:<50}|".format("4. Keluar"))
            print("+" + "-"*50 + "+")
            pilihan = input('Pilih menu: ')
            if pilihan == '1':
                # os.system('cls')
                deskripsi = input("Masukkan Deskripsi Level Gunung ")
                fn.create_level(deskripsi)
            elif pilihan == '2':
                # os.system('cls')
                fn.display_level()
                id_level = int(input("Masukkan ID level yang akan diperbarui: "))
                deskripsi = input("Masukkan deskripsi level baru: ")
                fn.update_level(id_level, deskripsi)
            elif pilihan == '3':
                # os.system('cls')
                daftar_menu_admin()
            elif pilihan == '4':
                break
        elif pilihan == "4":
            while True:
                # os.system('cls')
                print("="*100)
                print("DATA CUSTOMER".center(100))
                print("="*100)
                fn.display_customer()
                print("|1| Urutkan Berdasarkan Nama (ASC)\n|2| Urutkan Berdasarkan Nama (DESC)\n|3| Kembali")
                pilihan = input("Pilihan: ")
                if pilihan == "1":
                    # os.system('cls')
                    print("="*100)
                    print("DATA CUSTOMER".center(100))
                    print("="*100)
                    fn.display_urut_customer_asc()
                    print("|1| Kembali")
                    milih = input("Pilihan: ")
                    if milih == "1":
                        break
                elif pilihan == "2":
                    # os.system('cls')
                    print("="*100)
                    print("DATA CUSTOMER".center(100))
                    print("="*100)
                    fn.display_urut_customer_desc()
                    print("|1| Kembali")
                    milih = input("Pilihan: ")
                    if milih == "1":
                        break
                elif pilihan == "3":
                    break
        elif pilihan == '5':
            # os.system('cls')
            print("+" + "-"*50 + "+")
            print("|{:^50}|".format("Data Admin"))
            print("+" + "-"*50 + "+")
            fn.display_admin()

            print("+" + "-"*50 + "+")
            print("|{:<50}|".format("1. Tambah Admin"))
            print("|{:<50}|".format("2. Update Admin"))
            print("|{:<50}|".format("3. Cari Admin"))
            print("|{:<50}|".format("4. Urutkan Admin Berdasarkan Nama"))
            print("|{:<50}|".format("5. Kembali"))
            print("|{:<50}|".format("6. Keluar"))
            print("+" + "-"*50 + "+")
            pilihan = input('Pilih menu: ')
            if pilihan == '1':
                # os.system('cls')
                nama = input("Masukkan nama admin: ")
                no_telp = input("Masukkan nomor telepon admin: ")
                username = input("Masukkan username Admin: ")
                password = input("Masukkan password Admin: ")
                fn.create_admin(nama, no_telp, username, password)
            elif pilihan == '2':
                # os.system('cls')
                fn.display_admin()
                id_admin = int(input("Masukkan ID admin yang akan diperbarui: "))
                nama = input("Masukkan nama: ")
                no_telp = input("Masukkan nomor telepon: ")
                username = input("Masukkan username: ")
                password = input("Masukkan password: ")
                fn.update_admin(id_admin, nama, no_telp, username, password)
            elif pilihan == '3':
                # os.system('cls')
                fn.display_cari_nama_admin()
                print("|1| Kembali")
                milih = input("Pilihan: ")
                if milih == "1":
                    break
            elif pilihan == '4':
                # os.system('cls')
                fn.display_urut_admin_asc()
                print("|1| Kembali")
                milih = input("Pilihan: ")
                if milih == "1":
                    break
            elif pilihan == '5':
                # os.system('cls')
                daftar_menu_admin()
            elif pilihan == '6':
                break
        elif pilihan == "6":
            while True:
                # os.system('cls')
                print("="*100)
                print("DATA RIWAYAT".center(100))
                print("="*100)
                print("|1| Urutkan Berdasarkan Tanggal Daki Terlama\n|2| Urutkan Berdasarkan Tanggal Daki Terbaru\n|3| Cari Berdasarkan Nama Customer\n|4| Cari Berdasarkan Nama Gunung\n|5| Kembali")
                pilihan = input("Pilihan: ")
                if pilihan == "1":
                    # os.system('cls')
                    print("="*100)
                    print("DATA RIWAYAT".center(100))
                    print("="*100)
                    fn.display_riwayat_urut_tanggal_daki_terlama()
                    print("|1| Kembali")
                    milih = input("Pilihan: ")
                    if milih == "1":
                        break
                elif pilihan == "2":
                    # os.system('cls')
                    print("="*100)
                    print("DATA RIWAYAT".center(100))
                    print("="*100)
                    fn.display_riwayat_urut_tanggal_daki_terbaru()
                    print("|1| Kembali")
                    milih = input("Pilihan: ")
                    if milih == "1":
                        break
                elif pilihan == "3":
                    # os.system('cls')
                    print("="*100)
                    print("DATA RIWAYAT".center(100))
                    print("="*100)
                    fn.display_riwayat_nama_customer()
                    print("|1| Kembali")
                    milih = input("Pilihan: ")
                    if milih == "1":
                        break
                elif pilihan == "4":
                    # os.system('cls')
                    print("="*100)
                    print("DATA RIWAYAT".center(100))
                    print("="*100)
                    fn.display_riwayat_nama_gunung()
                    print("|1| Kembali")
                    milih = input("Pilihan: ")
                    if milih == "1":
                        break
                elif pilihan == "5":
                    break            
        elif pilihan == '7':
            # os.system('cls')
            print("+" + "-"*50 + "+")
            print("|{:^50}|".format("Data Jam Shift"))
            print("+" + "-"*50 + "+")
            fn.display_shift()

            print("+" + "-"*50 + "+")
            print("|{:<50}|".format("1. Tambah Jam Shift"))
            print("|{:<50}|".format("2. Update Jam Shift"))
            print("|{:<50}|".format("3. Kembali"))
            print("|{:<50}|".format("4. Keluar"))
            print("+" + "-"*50 + "+")
            pilihan = input('Pilih menu: ')
            if pilihan == '1':
                # os.system('cls')
                tanggal_berlaku = input("Masukkan Tanggal Berlaku (YYYY-MM-DD): ")
                tanggal_berakhir = input("Masukkan Tanggal Berakhir (YYYY-MM-DD): ")
                hari_shift = input("Masukkan Hari (dalam Bahasa Inggris): ")
                jam_mulai = input("Masukkan jam mulai (00:00:00): ")
                jam_selesai = input("Masukkan jam selesai (00:00:00): ")
                fn.create_shift(tanggal_berlaku, tanggal_berakhir, hari_shift, jam_mulai, jam_selesai)
            elif pilihan == '2':
                # os.system('cls')
                fn.display_shift()
                id_shift = int(input("Masukkan ID shift yang akan diperbarui: "))
                tanggal_berlaku = input("Masukkan Tanggal Berlaku (YYYY-MM-DD): ")
                tanggal_berakhir = input("Masukkan Tanggal Berakhir (YYYY-MM-DD): ")
                hari_shift = input("Masukkan Hari (dalam Bahasa Inggris): ")
                jam_mulai = input("Masukkan jam mulai (00:00:00): ")
                jam_selesai = input("Masukkan jam selesai (00:00:00): ")
                fn.update_shift(id_shift, tanggal_berlaku, tanggal_berakhir, hari_shift, jam_mulai, jam_selesai)
            elif pilihan == '3':
                # os.system('cls')
                daftar_menu_admin()
            elif pilihan == '4':
                break
        elif pilihan == '8':
            # os.system('cls')
            print("+" + "-"*50 + "+")
            print("|{:^50}|".format("Data Metode Pembayaran"))
            print("+" + "-"*50 + "+")
            fn.display_metode()

            print("+" + "-"*50 + "+")  
            print("|{:<50}|".format("1. Tambah Metode"))
            print("|{:<50}|".format("2. Update Metode"))
            print("|{:<50}|".format("3. Kembali"))
            print("|{:<50}|".format("4. Keluar"))
            print("+" + "-"*50 + "+")
            pilihan = input('Pilih menu: ')
            if pilihan == '1':
                # os.system('cls')
                nama_metode = input("Masukkan nama metode pembayaran: ")
                no_rekening = input("Masukkan nomor rekening pengelola: ")
                nama_pemilik = input("Masukkan nama pemilik: ")
                fn.create_metode_pembayaran(nama_metode, no_rekening, nama_pemilik)
            elif pilihan == '2':
                # os.system('cls')
                fn.display_metode()
                id_metode = int(input("Masukkan ID metode pembayaran yang akan diperbarui: "))
                nama_metode = input("Masukkan nama metode pembayaran baru: ")
                no_rekening = input("Masukkan nomor rekening pengelola baru: ")
                nama_pemilik = input("Masukkan nama pemilik baru: ")
                fn.update_metode_pembayaran(id_metode, nama_metode, no_rekening, nama_pemilik)
            elif pilihan == '3':
                # os.system('cls')
                daftar_menu_admin()
            elif pilihan == '4':
                break                      
        elif pilihan == '9':
            # os.system('cls')
            print("+" + "-"*50 + "+")
            print("|{:^50}|".format("Data Pemesanan"))
            print("+" + "-"*50 + "+")
            fn.display_pemesanan()

            print("+" + "-"*50 + "+")
            print("|{:<50}|".format("1. Kembali"))
            print("|{:<50}|".format("2. Keluar"))
            print("+" + "-"*50 + "+")
            pilihan = input('Pilih menu: ')
            if pilihan == "1":
                # os.system('cls')
                daftar_menu_admin()
            elif pilihan == '2':
                break                    
        elif pilihan == '10':
            # os.system('cls')
            print("+" + "-"*50 + "+")
            print("|{:^50}|".format("Data Pembayaran"))
            print("+" + "-"*50 + "+")
            fn.display_pembayaran()

            print("+" + "-"*50 + "+")  
            print("|{:<50}|".format("1. Konfirmasi Pembayaran"))
            print("|{:<50}|".format("2. Kembali"))
            print("|{:<50}|".format("3. Keluar"))
            print("+" + "-"*50 + "+")
            pilihan = input('Pilih menu: ')
            if pilihan == '1':
                # os.system('cls')
                id_detail = int(input("Masukkan ID detail reservasi yang akan diperbarui: "))
                status_pembayaran = input("Masukkan status pembayaran baru (Paid/Pending): ")
                fn.update_status_pembayaran(id_detail, status_pembayaran)
            elif pilihan == '2':
                # os.system('cls')
                daftar_menu_admin()
            else:
                break 
        elif pilihan == '11':
            # os.system('cls')
            print("+" + "-"*50 + "+")
            print("|{:^50}|".format("Data Jadwal Shift Karyawan"))
            print("+" + "-"*50 + "+")
            fn.display_detail_shift()

            print("+" + "-"*50 + "+")  
            print("|{:<50}|".format("1. Tambah Jadwal Shift"))
            print("|{:<50}|".format("2. Update Jadwal Shift"))
            print("|{:<50}|".format("3. Kembali"))
            print("|{:<50}|".format("4. Keluar"))
            print("+" + "-"*50 + "+")
            pilihan = input('Pilih menu: ')
            if pilihan == '1':
                # os.system('cls')
                fn.display_admin()
                karyawan_id = int(input("Masukkan ID karyawan: "))
                # os.system('cls')
                fn.display_shift()
                jadwal_shift_id = int(input("Masukkan ID jadwal shift: "))
                fn.create_detail_shift(karyawan_id, jadwal_shift_id)
            elif pilihan == '2':
                fn.display_detail_shift()
                detail_id = int(input("Masukkan ID detail shift yang akan diperbarui: "))
                fn.display_admin()
                karyawan_id = int(input("Masukkan ID karywan yang akan diperbarui: "))
                fn.display_shift()
                jadwal_shift_id = int(input("Masukkan ID shift baru: "))
                fn.update_detail_shift(karyawan_id, jadwal_shift_id, detail_id)
            elif pilihan == '3':
                daftar_menu_admin()
            elif pilihan == '4':
                break  
        elif pilihan == "12":
            akses = False


def menu_user():
    akses = True
    while akses:
        os.system('cls')
        print("="*100)
        print("ANDA MASUK SEBAGAI USER".center(100))
        print("="*100)
        print("|1| Login\n|2| Register\n|3| Kembali")
        pilihan = input("Pilihan: ")
        if pilihan == "1":
            os.system('cls')
            print("="*100)
            print("LOGIN".center(100))
            print("="*100)
            username = input("Username: ")
            password = input("Password: ")
            customer = fn.login_customer(username, password)
            id_user = fn.customer_id_cari(username)
            if customer:
                os.system('cls')
                while akses:
                    print("="*100)
                    print("MAIN MENU".center(100))
                    print("="*100)
                    print("|1| Urutkan Gunung\n|2| Cari Gunung\n|3| Exit")
                    pilih = input("Pilih Menu: ")
                    if pilih == "1":
                        os.system('cls')
                        fn.display_gunung()
                        print("|1| Urutkan berdasarkan nama (ASC)\n|2| Urutkan berdasarkan nama (DESC)\n|3| Urutkan berdasarkan tinggi (ASC)\n|4| Urutkan berdasarkan tinggi (DESC)\n|5| Urutkan berdasarkan level (ASC)\n|6| Urutkan berdasarkan level (DESC)\n|7| Urutkan berdasarkan harga (ASC)\n|8| Urutkan berdasarkan harga (DESC)\n|9| Exit")
                        pilih1 = input("Pilih Menu: ")
                        if pilih1 == "1":
                            os.system('cls')
                            fn.display_gunung_urut_nama_asc() 
                            fn.pemesanan(username) 
                            pembayaran(id_user)             
                        elif pilih1 == "2":
                            os.system('cls')
                            fn.display_gunung_urut_nama_desc() 
                            fn.pemesanan(username)
                            pembayaran(id_user)
                        elif pilih1 == "3":
                            os.system('cls')
                            fn.display_gunung_urut_tinggi_asc()    
                            fn.pemesanan(username)  
                            pembayaran(id_user)         
                        elif pilih1 == "4":
                            os.system('cls')
                            fn.display_gunung_urut_tinggi_desc()
                            fn.pemesanan(username)
                            pembayaran(id_user)
                        elif pilih1 == "5":
                            os.system('cls')
                            fn.display_gunung_urut_level_asc()
                            fn.pemesanan(username)
                            pembayaran(id_user)
                        elif pilih1 == "6":
                            os.system('cls')
                            fn.display_gunung_urut_level_desc()
                            fn.pemesanan(username)
                            pembayaran(id_user)
                        elif pilih1 == "7":
                            os.system('cls')
                            fn.display_gunung_urut_harga_asc()
                            fn.pemesanan(username)
                            pembayaran(id_user)
                        elif pilih1 == "8":
                            os.system('cls')
                            fn.display_gunung_urut_harga_desc()
                            fn.pemesanan(username)
                            pembayaran(id_user)
                        elif pilih1 == "9":
                            break
                    elif pilih == "2":
                        fn.display_nama_gunung()
                        fn.pemesanan(username)
                        pembayaran(id_user)
                    elif pilih == "3":
                        break
        elif pilihan == "2":
            regist_proses()
        elif pilihan == "3":
            break   
def main():
    token = True
    while token:
        os.system('cls')
        print("="*100)
        print("SELAMAT DATANG DI TIKUNG!".center(100))
        print("="*100)
        print("|1| User\n|2| Admin\n|3| Exit")
        opsi = input("Masuk sebagai: ")
        if opsi == "1":
            menu_user()
        elif opsi == "2":
            admin_menu()
        elif opsi == "3":
            token = False
    os.system('cls')
    print("="*100)
    print("TERIMA KASIH TELAH MENGGUNAKAN TIKUNG!".center(100))
    print("="*100)

main()
