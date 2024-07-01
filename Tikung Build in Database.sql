CREATE TABLE admin (
    admin_id     SERIAL PRIMARY KEY,
    nama_lengkap VARCHAR(64) NOT NULL,
    username     VARCHAR(16) NOT NULL,
    password     VARCHAR(128) NOT NULL,
    telepon      VARCHAR(16)
);

ALTER TABLE admin ADD CONSTRAINT username_admin UNIQUE ( username );

ALTER TABLE admin ADD CONSTRAINT telepon_admin UNIQUE ( telepon );


CREATE TABLE customer (
    customer_id   SERIAL PRIMARY KEY,
    nama_lengkap  VARCHAR(64) NOT NULL,
    nik           VARCHAR(16) NOT NULL,
    telepon       VARCHAR(16) NOT NULL,
    tanggal_lahir DATE NOT NULL,
    alamat        VARCHAR(128) NOT NULL,
    username      VARCHAR(16) NOT NULL,
    password      VARCHAR(128) NOT NULL,
    kota_kota_id  INTEGER NOT NULL
);

CREATE INDEX nik_customer ON
    customer (
        nik
    ASC );

CREATE INDEX telepon_customer ON
    customer (
        telepon
    ASC );

CREATE INDEX username_customer ON
    customer (
        username
    ASC );


CREATE TABLE detail_shift (
    id_detail_shift SERIAL PRIMARY KEY,
    admin_admin_id  INTEGER NOT NULL,
    shift_shift_id  INTEGER NOT NULL
);


CREATE TABLE gunung (
    gunung_id      SERIAL PRIMARY KEY,
    nama_gunung    VARCHAR(64) NOT NULL,
    tinggi         INTEGER NOT NULL,
    harga          INTEGER NOT NULL,
    level_level_id INTEGER NOT NULL
);


CREATE TABLE kota (
    kota_id              SERIAL PRIMARY KEY,
    nama_kota            VARCHAR(64) NOT NULL,
    provinsi_provinsi_id INTEGER NOT NULL
);


CREATE TABLE level (
    level_id        SERIAL PRIMARY KEY,
    deskripsi_level VARCHAR(255) NOT NULL
);


CREATE TABLE loket (
    loket_id         SERIAL PRIMARY KEY,
    kota_kota_id     INTEGER NOT NULL,
    gunung_gunung_id INTEGER NOT NULL
);


CREATE TABLE metode (
    metode_id             SERIAL PRIMARY KEY,
    nama_metode           VARCHAR(32) NOT NULL,
    no_rekening           VARCHAR(32) NOT NULL,
    nama_pemilik_rekening VARCHAR(64) NOT NULL
);

CREATE INDEX no_rekening ON
    metode (
        no_rekening
    ASC );


CREATE TABLE pembayaran (
    pembayaran_id          SERIAL PRIMARY KEY,
	total				   INTEGER NOT NULL,
    status                 VARCHAR(16) NOT NULL,
	bukti_bayar			   VARCHAR(64) NOT NULL,
    metode_metode_id       INTEGER NOT NULL,
    pemesanan_pemesanan_id INTEGER NOT NULL
);


CREATE TABLE pemesanan (
    pemesanan_id         SERIAL PRIMARY KEY,
    tanggal_pesan        DATE NOT NULL,
    tanggal_daki         DATE NOT NULL,
    quantity             INTEGER NOT NULL,
    admin_admin_id       INTEGER NOT NULL,
    customer_customer_id INTEGER NOT NULL,
    gunung_gunung_id     INTEGER NOT NULL
);


CREATE TABLE provinsi (
    provinsi_id   SERIAL PRIMARY KEY,
    nama_provinsi VARCHAR(64) NOT NULL
);


CREATE TABLE shift (
    shift_id         SERIAL PRIMARY KEY,
    tanggal_berlaku  DATE NOT NULL,
    tanggal_berakhir DATE NOT NULL,
    hari_shift       VARCHAR(16) NOT NULL,
    jam_awal_shift   DATE NOT NULL,
    jam_akhir_shift  DATE NOT NULL
);


ALTER TABLE customer
    ADD CONSTRAINT customer_kota_fk FOREIGN KEY ( kota_kota_id )
        REFERENCES kota ( kota_id );

ALTER TABLE detail_shift
    ADD CONSTRAINT detail_shift_admin_fk FOREIGN KEY ( admin_admin_id )
        REFERENCES admin ( admin_id );

ALTER TABLE detail_shift
    ADD CONSTRAINT detail_shift_shift_fk FOREIGN KEY ( shift_shift_id )
        REFERENCES shift ( shift_id );

ALTER TABLE gunung
    ADD CONSTRAINT gunung_level_fk FOREIGN KEY ( level_level_id )
        REFERENCES level ( level_id );

ALTER TABLE kota
    ADD CONSTRAINT kota_provinsi_fk FOREIGN KEY ( provinsi_provinsi_id )
        REFERENCES provinsi ( provinsi_id );

ALTER TABLE loket
    ADD CONSTRAINT loket_gunung_fk FOREIGN KEY ( gunung_gunung_id )
        REFERENCES gunung ( gunung_id );

ALTER TABLE loket
    ADD CONSTRAINT loket_kota_fk FOREIGN KEY ( kota_kota_id )
        REFERENCES kota ( kota_id );

ALTER TABLE pembayaran
    ADD CONSTRAINT pembayaran_metode_fk FOREIGN KEY ( metode_metode_id )
        REFERENCES metode ( metode_id );

ALTER TABLE pembayaran
    ADD CONSTRAINT pembayaran_pemesanan_fk FOREIGN KEY ( pemesanan_pemesanan_id )
        REFERENCES pemesanan ( pemesanan_id );

ALTER TABLE pemesanan
    ADD CONSTRAINT pemesanan_admin_fk FOREIGN KEY ( admin_admin_id )
        REFERENCES admin ( admin_id );

ALTER TABLE pemesanan
    ADD CONSTRAINT pemesanan_customer_fk FOREIGN KEY ( customer_customer_id )
        REFERENCES customer ( customer_id );

ALTER TABLE pemesanan
    ADD CONSTRAINT pemesanan_gunung_fk FOREIGN KEY ( gunung_gunung_id )
        REFERENCES gunung ( gunung_id );
		

INSERT INTO admin (nama_lengkap, username, password, telepon) VALUES
('Richie Olajuwon Santoso', 'chiejuwons', '$2y$10$EP7OFUnz0tMDAluF.qtr0ueBlzTk80qK.xktOrlEkNrg1xzLOOozu', '081238038207'),
('M. Raffy Putra N.', 'raffypetir', '$2y$10$b7bdd8Ci35wyphDq9G3qoet3Wvc60aOZZf5xOGz.BWShK40kXYNsC', '081234567890'),
('Almas Teva Zahran Dinastian', 'kalisate', '$2y$10$pbXYmDXlEBLV1D1yzgdd6.cFzfHuENs1eFM/BsWgiJf/urlwZQfBa', '081234123412'),
('Ahmad Fais Arifin', 'icangson','$2y$10$jDTn6sqre0n/LaZW3/7dO.XP93pMNGRnN1Z78RZxClddj7pbjERum', '081234567905'),
('Dyaksa Adi Pradana', 'adiadi12', '$2y$10$Mw2asiPDRt9LTQrMnBbGXu074nNyL.OIUVojTV32VDlUhGPNnm8te', '083456789056');

INSERT INTO shift (tanggal_berlaku, tanggal_berakhir, hari_shift, jam_awal_shift, jam_akhir_shift) VALUES
(TO_DATE('2024-05-01', 'YYYY-MM-DD'), TO_DATE('2024-06-30', 'YYYY-MM-DD'), 'Monday', '00:00:00', '12:00:00'),
(TO_DATE('2024-05-01', 'YYYY-MM-DD'), TO_DATE('2024-06-30', 'YYYY-MM-DD'), 'Tuesday', '00:00:00', '12:00:00'),
(TO_DATE('2024-05-01', 'YYYY-MM-DD'), TO_DATE('2024-06-30', 'YYYY-MM-DD'), 'Wednesday', '00:00:00', '12:00:00'),
(TO_DATE('2024-05-01', 'YYYY-MM-DD'), TO_DATE('2024-06-30', 'YYYY-MM-DD'), 'Thursday', '00:00:00', '12:00:00'),
(TO_DATE('2024-05-01', 'YYYY-MM-DD'), TO_DATE('2024-06-30', 'YYYY-MM-DD'), 'Friday', '00:00:00', '12:00:00'),
(TO_DATE('2024-05-01', 'YYYY-MM-DD'), TO_DATE('2024-06-30', 'YYYY-MM-DD'), 'Saturday', '00:00:00', '12:00:00'),
(TO_DATE('2024-05-01', 'YYYY-MM-DD'), TO_DATE('2024-06-30', 'YYYY-MM-DD'), 'Sunday', '00:00:00', '12:00:00'),
(TO_DATE('2024-05-01', 'YYYY-MM-DD'), TO_DATE('2024-06-30', 'YYYY-MM-DD'), 'Monday', '12:00:00', '24:00:00'),
(TO_DATE('2024-05-01', 'YYYY-MM-DD'), TO_DATE('2024-06-30', 'YYYY-MM-DD'), 'Tuesday', '12:00:00', '24:00:00'),
(TO_DATE('2024-05-01', 'YYYY-MM-DD'), TO_DATE('2024-06-30', 'YYYY-MM-DD'), 'Wednesday', '12:00:00', '24:00:00'),
(TO_DATE('2024-05-01', 'YYYY-MM-DD'), TO_DATE('2024-06-30', 'YYYY-MM-DD'), 'Thursday', '12:00:00', '24:00:00'),
(TO_DATE('2024-05-01', 'YYYY-MM-DD'), TO_DATE('2024-06-30', 'YYYY-MM-DD'), 'Friday', '12:00:00', '24:00:00'),
(TO_DATE('2024-05-01', 'YYYY-MM-DD'), TO_DATE('2024-06-30', 'YYYY-MM-DD'), 'Saturday', '12:00:00', '24:00:00'),
(TO_DATE('2024-05-01', 'YYYY-MM-DD'), TO_DATE('2024-06-30', 'YYYY-MM-DD'), 'Sunday', '12:00:00', '24:00:00');

INSERT INTO detail_shift (admin_admin_id, shift_shift_id) VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5),
(1, 6),
(2, 7),
(3, 8),
(4, 9),
(5, 10),
(1, 11),
(2, 12),
(3, 13),
(4, 14);

INSERT INTO provinsi (nama_provinsi) VALUES
('Nusa Tenggara Barat'),
('Jawa Timur');

INSERT INTO kota (nama_kota, provinsi_provinsi_id) VALUES
('Lombok Timur', 1),
('Lumajang', 2),
('Malang', 2),
('Probolinggo', 2);

INSERT INTO level (deskripsi_level) VALUES
('Perjalanan pada jalur yang sudah ada dan jelas, beberapa bagian jalur terkelola untuk memudahkan perjalanan. Dilakukan secara singkat dalam sehari tanpa bermalam.'),
('Perjalanan pada jalur yang sudah ada dan jelas, dilakukan seharian dengan adanya kemungkinan berjalan malam sampai menginap.'),
('Perjalanan pada jalur yang sudah ada, hanya sesekali tertutup yang mudah dilewati. Harus bermalam sehingga peralatan berkemah dan perbekalan sudah diperlukan.'),
('Perjalanan pada jalur yang sudah ada kemungkinan tertutup dan curam sehingga terkadang butuh pembukaan jalur untuk dilewati.'),
('Perjalanan pada jalur yang sudah tertutup atau harus membuka jalur baru dengan beberapa bagian curam dan terjal.');

INSERT INTO gunung (nama_gunung, tinggi, harga, level_level_id) VALUES
('Rinjani', 3726, 10000, 3),
('Semeru', 3676, 25000, 3),
('Bromo', 2329, 30000, 1);

INSERT INTO customer (nama_lengkap, nik, telepon, tanggal_lahir, alamat, username, password, kota_kota_id) VALUES
('Lexandra Hansen', '3201024304050003', '081234567890', '2005-04-03', 'Jl. Merdeka No. 1', 'lexa1234', '$2y$10$HUs4DXBN7nlzS01Ra2VVPOz5dHN3M3UOMpr68Lsd3sWOGM8lDAQNG', 2),
('Valerie Oriena Minarno', '3509085707030001', '087890765412', '2003-07-17', 'Jln. Jawa No.7', 'valvalerie', '$2y$10$IX.D6VwTNAWp2PjCUtW5tOWGPyZpH2ded0EwZ1RKnXZLQE1eMg.6.', 3);

INSERT INTO loket (kota_kota_id, gunung_gunung_id) VALUES
(1, 1),
(2, 2),
(3, 2),
(4, 3);

INSERT INTO metode (nama_metode, no_rekening, nama_pemilik_rekening) VALUES
('Transfer BCA', '8912012556', 'Richie Olajuwon Santoso'),
('Dana', '081238038207', 'Richie Olajuwon Santoso');

INSERT INTO pemesanan (tanggal_pesan, tanggal_daki, quantity, admin_admin_id, customer_customer_id, gunung_gunung_id) VALUES
(TO_DATE('2024-06-01', 'YYYY-MM-DD'), TO_DATE('2024-06-30', 'YYYY-MM-DD'), 1, 3, 1, 3),
(TO_DATE('2024-06-11', 'YYYY-MM-DD'), TO_DATE('2024-06-25', 'YYYY-MM-DD'), 3, 1, 2, 2);

INSERT INTO pembayaran (total, status, bukti_bayar, metode_metode_id, pemesanan_pemesanan_id) VALUES
(30000, 'Paid', 'bukti1.png', 1, 1),
(75000, 'Pending', 'bukti2.png', 2, 2);