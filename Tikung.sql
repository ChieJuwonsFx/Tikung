PGDMP                      |            algopro    16.2    16.2 j    h           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            i           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            j           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            k           1262    20365    algopro    DATABASE     �   CREATE DATABASE algopro WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'English_United States.1252';
    DROP DATABASE algopro;
                postgres    false            �            1259    21923    admin    TABLE     �   CREATE TABLE public.admin (
    admin_id integer NOT NULL,
    nama_lengkap character varying(64) NOT NULL,
    username character varying(16) NOT NULL,
    password character varying(128) NOT NULL,
    telepon character varying(16)
);
    DROP TABLE public.admin;
       public         heap    postgres    false            �            1259    21922    admin_admin_id_seq    SEQUENCE     �   CREATE SEQUENCE public.admin_admin_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 )   DROP SEQUENCE public.admin_admin_id_seq;
       public          postgres    false    216            l           0    0    admin_admin_id_seq    SEQUENCE OWNED BY     I   ALTER SEQUENCE public.admin_admin_id_seq OWNED BY public.admin.admin_id;
          public          postgres    false    215            �            1259    21934    customer    TABLE     �  CREATE TABLE public.customer (
    customer_id integer NOT NULL,
    nama_lengkap character varying(64) NOT NULL,
    nik character varying(16) NOT NULL,
    telepon character varying(16) NOT NULL,
    tanggal_lahir date NOT NULL,
    alamat character varying(128) NOT NULL,
    username character varying(16) NOT NULL,
    password character varying(128) NOT NULL,
    kota_kota_id integer NOT NULL
);
    DROP TABLE public.customer;
       public         heap    postgres    false            �            1259    21933    customer_customer_id_seq    SEQUENCE     �   CREATE SEQUENCE public.customer_customer_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 /   DROP SEQUENCE public.customer_customer_id_seq;
       public          postgres    false    218            m           0    0    customer_customer_id_seq    SEQUENCE OWNED BY     U   ALTER SEQUENCE public.customer_customer_id_seq OWNED BY public.customer.customer_id;
          public          postgres    false    217            �            1259    21944    detail_shift    TABLE     �   CREATE TABLE public.detail_shift (
    id_detail_shift integer NOT NULL,
    admin_admin_id integer NOT NULL,
    shift_shift_id integer NOT NULL
);
     DROP TABLE public.detail_shift;
       public         heap    postgres    false            �            1259    21943     detail_shift_id_detail_shift_seq    SEQUENCE     �   CREATE SEQUENCE public.detail_shift_id_detail_shift_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 7   DROP SEQUENCE public.detail_shift_id_detail_shift_seq;
       public          postgres    false    220            n           0    0     detail_shift_id_detail_shift_seq    SEQUENCE OWNED BY     e   ALTER SEQUENCE public.detail_shift_id_detail_shift_seq OWNED BY public.detail_shift.id_detail_shift;
          public          postgres    false    219            �            1259    21951    gunung    TABLE     �   CREATE TABLE public.gunung (
    gunung_id integer NOT NULL,
    nama_gunung character varying(64) NOT NULL,
    tinggi integer NOT NULL,
    harga integer NOT NULL,
    level_level_id integer NOT NULL
);
    DROP TABLE public.gunung;
       public         heap    postgres    false            �            1259    21950    gunung_gunung_id_seq    SEQUENCE     �   CREATE SEQUENCE public.gunung_gunung_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 +   DROP SEQUENCE public.gunung_gunung_id_seq;
       public          postgres    false    222            o           0    0    gunung_gunung_id_seq    SEQUENCE OWNED BY     M   ALTER SEQUENCE public.gunung_gunung_id_seq OWNED BY public.gunung.gunung_id;
          public          postgres    false    221            �            1259    21958    kota    TABLE     �   CREATE TABLE public.kota (
    kota_id integer NOT NULL,
    nama_kota character varying(64) NOT NULL,
    provinsi_provinsi_id integer NOT NULL
);
    DROP TABLE public.kota;
       public         heap    postgres    false            �            1259    21957    kota_kota_id_seq    SEQUENCE     �   CREATE SEQUENCE public.kota_kota_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 '   DROP SEQUENCE public.kota_kota_id_seq;
       public          postgres    false    224            p           0    0    kota_kota_id_seq    SEQUENCE OWNED BY     E   ALTER SEQUENCE public.kota_kota_id_seq OWNED BY public.kota.kota_id;
          public          postgres    false    223            �            1259    21965    level    TABLE     r   CREATE TABLE public.level (
    level_id integer NOT NULL,
    deskripsi_level character varying(255) NOT NULL
);
    DROP TABLE public.level;
       public         heap    postgres    false            �            1259    21964    level_level_id_seq    SEQUENCE     �   CREATE SEQUENCE public.level_level_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 )   DROP SEQUENCE public.level_level_id_seq;
       public          postgres    false    226            q           0    0    level_level_id_seq    SEQUENCE OWNED BY     I   ALTER SEQUENCE public.level_level_id_seq OWNED BY public.level.level_id;
          public          postgres    false    225            �            1259    21972    loket    TABLE     �   CREATE TABLE public.loket (
    loket_id integer NOT NULL,
    kota_kota_id integer NOT NULL,
    gunung_gunung_id integer NOT NULL
);
    DROP TABLE public.loket;
       public         heap    postgres    false            �            1259    21971    loket_loket_id_seq    SEQUENCE     �   CREATE SEQUENCE public.loket_loket_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 )   DROP SEQUENCE public.loket_loket_id_seq;
       public          postgres    false    228            r           0    0    loket_loket_id_seq    SEQUENCE OWNED BY     I   ALTER SEQUENCE public.loket_loket_id_seq OWNED BY public.loket.loket_id;
          public          postgres    false    227            �            1259    21979    metode    TABLE     �   CREATE TABLE public.metode (
    metode_id integer NOT NULL,
    nama_metode character varying(32) NOT NULL,
    no_rekening character varying(32) NOT NULL,
    nama_pemilik_rekening character varying(64) NOT NULL
);
    DROP TABLE public.metode;
       public         heap    postgres    false            �            1259    21978    metode_metode_id_seq    SEQUENCE     �   CREATE SEQUENCE public.metode_metode_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 +   DROP SEQUENCE public.metode_metode_id_seq;
       public          postgres    false    230            s           0    0    metode_metode_id_seq    SEQUENCE OWNED BY     M   ALTER SEQUENCE public.metode_metode_id_seq OWNED BY public.metode.metode_id;
          public          postgres    false    229            �            1259    21987 
   pembayaran    TABLE       CREATE TABLE public.pembayaran (
    pembayaran_id integer NOT NULL,
    total integer NOT NULL,
    status character varying(16) NOT NULL,
    bukti_bayar character varying(64) NOT NULL,
    metode_metode_id integer NOT NULL,
    pemesanan_pemesanan_id integer NOT NULL
);
    DROP TABLE public.pembayaran;
       public         heap    postgres    false            �            1259    21986    pembayaran_pembayaran_id_seq    SEQUENCE     �   CREATE SEQUENCE public.pembayaran_pembayaran_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 3   DROP SEQUENCE public.pembayaran_pembayaran_id_seq;
       public          postgres    false    232            t           0    0    pembayaran_pembayaran_id_seq    SEQUENCE OWNED BY     ]   ALTER SEQUENCE public.pembayaran_pembayaran_id_seq OWNED BY public.pembayaran.pembayaran_id;
          public          postgres    false    231            �            1259    21994 	   pemesanan    TABLE       CREATE TABLE public.pemesanan (
    pemesanan_id integer NOT NULL,
    tanggal_pesan date NOT NULL,
    tanggal_daki date NOT NULL,
    quantity integer NOT NULL,
    admin_admin_id integer NOT NULL,
    customer_customer_id integer NOT NULL,
    gunung_gunung_id integer NOT NULL
);
    DROP TABLE public.pemesanan;
       public         heap    postgres    false            �            1259    21993    pemesanan_pemesanan_id_seq    SEQUENCE     �   CREATE SEQUENCE public.pemesanan_pemesanan_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 1   DROP SEQUENCE public.pemesanan_pemesanan_id_seq;
       public          postgres    false    234            u           0    0    pemesanan_pemesanan_id_seq    SEQUENCE OWNED BY     Y   ALTER SEQUENCE public.pemesanan_pemesanan_id_seq OWNED BY public.pemesanan.pemesanan_id;
          public          postgres    false    233            �            1259    22001    provinsi    TABLE     u   CREATE TABLE public.provinsi (
    provinsi_id integer NOT NULL,
    nama_provinsi character varying(64) NOT NULL
);
    DROP TABLE public.provinsi;
       public         heap    postgres    false            �            1259    22000    provinsi_provinsi_id_seq    SEQUENCE     �   CREATE SEQUENCE public.provinsi_provinsi_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 /   DROP SEQUENCE public.provinsi_provinsi_id_seq;
       public          postgres    false    236            v           0    0    provinsi_provinsi_id_seq    SEQUENCE OWNED BY     U   ALTER SEQUENCE public.provinsi_provinsi_id_seq OWNED BY public.provinsi.provinsi_id;
          public          postgres    false    235            �            1259    22008    shift    TABLE       CREATE TABLE public.shift (
    shift_id integer NOT NULL,
    tanggal_berlaku date NOT NULL,
    tanggal_berakhir date NOT NULL,
    hari_shift character varying(16) NOT NULL,
    jam_awal_shift time without time zone NOT NULL,
    jam_akhir_shift time without time zone NOT NULL
);
    DROP TABLE public.shift;
       public         heap    postgres    false            �            1259    22007    shift_shift_id_seq    SEQUENCE     �   CREATE SEQUENCE public.shift_shift_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 )   DROP SEQUENCE public.shift_shift_id_seq;
       public          postgres    false    238            w           0    0    shift_shift_id_seq    SEQUENCE OWNED BY     I   ALTER SEQUENCE public.shift_shift_id_seq OWNED BY public.shift.shift_id;
          public          postgres    false    237            �           2604    21926    admin admin_id    DEFAULT     p   ALTER TABLE ONLY public.admin ALTER COLUMN admin_id SET DEFAULT nextval('public.admin_admin_id_seq'::regclass);
 =   ALTER TABLE public.admin ALTER COLUMN admin_id DROP DEFAULT;
       public          postgres    false    216    215    216            �           2604    21937    customer customer_id    DEFAULT     |   ALTER TABLE ONLY public.customer ALTER COLUMN customer_id SET DEFAULT nextval('public.customer_customer_id_seq'::regclass);
 C   ALTER TABLE public.customer ALTER COLUMN customer_id DROP DEFAULT;
       public          postgres    false    217    218    218            �           2604    21947    detail_shift id_detail_shift    DEFAULT     �   ALTER TABLE ONLY public.detail_shift ALTER COLUMN id_detail_shift SET DEFAULT nextval('public.detail_shift_id_detail_shift_seq'::regclass);
 K   ALTER TABLE public.detail_shift ALTER COLUMN id_detail_shift DROP DEFAULT;
       public          postgres    false    219    220    220            �           2604    21954    gunung gunung_id    DEFAULT     t   ALTER TABLE ONLY public.gunung ALTER COLUMN gunung_id SET DEFAULT nextval('public.gunung_gunung_id_seq'::regclass);
 ?   ALTER TABLE public.gunung ALTER COLUMN gunung_id DROP DEFAULT;
       public          postgres    false    222    221    222            �           2604    21961    kota kota_id    DEFAULT     l   ALTER TABLE ONLY public.kota ALTER COLUMN kota_id SET DEFAULT nextval('public.kota_kota_id_seq'::regclass);
 ;   ALTER TABLE public.kota ALTER COLUMN kota_id DROP DEFAULT;
       public          postgres    false    224    223    224            �           2604    21968    level level_id    DEFAULT     p   ALTER TABLE ONLY public.level ALTER COLUMN level_id SET DEFAULT nextval('public.level_level_id_seq'::regclass);
 =   ALTER TABLE public.level ALTER COLUMN level_id DROP DEFAULT;
       public          postgres    false    225    226    226            �           2604    21975    loket loket_id    DEFAULT     p   ALTER TABLE ONLY public.loket ALTER COLUMN loket_id SET DEFAULT nextval('public.loket_loket_id_seq'::regclass);
 =   ALTER TABLE public.loket ALTER COLUMN loket_id DROP DEFAULT;
       public          postgres    false    227    228    228            �           2604    21982    metode metode_id    DEFAULT     t   ALTER TABLE ONLY public.metode ALTER COLUMN metode_id SET DEFAULT nextval('public.metode_metode_id_seq'::regclass);
 ?   ALTER TABLE public.metode ALTER COLUMN metode_id DROP DEFAULT;
       public          postgres    false    230    229    230            �           2604    21990    pembayaran pembayaran_id    DEFAULT     �   ALTER TABLE ONLY public.pembayaran ALTER COLUMN pembayaran_id SET DEFAULT nextval('public.pembayaran_pembayaran_id_seq'::regclass);
 G   ALTER TABLE public.pembayaran ALTER COLUMN pembayaran_id DROP DEFAULT;
       public          postgres    false    231    232    232            �           2604    21997    pemesanan pemesanan_id    DEFAULT     �   ALTER TABLE ONLY public.pemesanan ALTER COLUMN pemesanan_id SET DEFAULT nextval('public.pemesanan_pemesanan_id_seq'::regclass);
 E   ALTER TABLE public.pemesanan ALTER COLUMN pemesanan_id DROP DEFAULT;
       public          postgres    false    233    234    234            �           2604    22004    provinsi provinsi_id    DEFAULT     |   ALTER TABLE ONLY public.provinsi ALTER COLUMN provinsi_id SET DEFAULT nextval('public.provinsi_provinsi_id_seq'::regclass);
 C   ALTER TABLE public.provinsi ALTER COLUMN provinsi_id DROP DEFAULT;
       public          postgres    false    235    236    236            �           2604    22011    shift shift_id    DEFAULT     p   ALTER TABLE ONLY public.shift ALTER COLUMN shift_id SET DEFAULT nextval('public.shift_shift_id_seq'::regclass);
 =   ALTER TABLE public.shift ALTER COLUMN shift_id DROP DEFAULT;
       public          postgres    false    238    237    238            O          0    21923    admin 
   TABLE DATA           T   COPY public.admin (admin_id, nama_lengkap, username, password, telepon) FROM stdin;
    public          postgres    false    216   t|       Q          0    21934    customer 
   TABLE DATA           �   COPY public.customer (customer_id, nama_lengkap, nik, telepon, tanggal_lahir, alamat, username, password, kota_kota_id) FROM stdin;
    public          postgres    false    218   t~       S          0    21944    detail_shift 
   TABLE DATA           W   COPY public.detail_shift (id_detail_shift, admin_admin_id, shift_shift_id) FROM stdin;
    public          postgres    false    220   �       U          0    21951    gunung 
   TABLE DATA           W   COPY public.gunung (gunung_id, nama_gunung, tinggi, harga, level_level_id) FROM stdin;
    public          postgres    false    222   �       W          0    21958    kota 
   TABLE DATA           H   COPY public.kota (kota_id, nama_kota, provinsi_provinsi_id) FROM stdin;
    public          postgres    false    224   0�       Y          0    21965    level 
   TABLE DATA           :   COPY public.level (level_id, deskripsi_level) FROM stdin;
    public          postgres    false    226   ��       [          0    21972    loket 
   TABLE DATA           I   COPY public.loket (loket_id, kota_kota_id, gunung_gunung_id) FROM stdin;
    public          postgres    false    228   ��       ]          0    21979    metode 
   TABLE DATA           \   COPY public.metode (metode_id, nama_metode, no_rekening, nama_pemilik_rekening) FROM stdin;
    public          postgres    false    230   �       _          0    21987 
   pembayaran 
   TABLE DATA           y   COPY public.pembayaran (pembayaran_id, total, status, bukti_bayar, metode_metode_id, pemesanan_pemesanan_id) FROM stdin;
    public          postgres    false    232   M�       a          0    21994 	   pemesanan 
   TABLE DATA           �   COPY public.pemesanan (pemesanan_id, tanggal_pesan, tanggal_daki, quantity, admin_admin_id, customer_customer_id, gunung_gunung_id) FROM stdin;
    public          postgres    false    234   ��       c          0    22001    provinsi 
   TABLE DATA           >   COPY public.provinsi (provinsi_id, nama_provinsi) FROM stdin;
    public          postgres    false    236   ؂       e          0    22008    shift 
   TABLE DATA           y   COPY public.shift (shift_id, tanggal_berlaku, tanggal_berakhir, hari_shift, jam_awal_shift, jam_akhir_shift) FROM stdin;
    public          postgres    false    238   �       x           0    0    admin_admin_id_seq    SEQUENCE SET     @   SELECT pg_catalog.setval('public.admin_admin_id_seq', 6, true);
          public          postgres    false    215            y           0    0    customer_customer_id_seq    SEQUENCE SET     F   SELECT pg_catalog.setval('public.customer_customer_id_seq', 2, true);
          public          postgres    false    217            z           0    0     detail_shift_id_detail_shift_seq    SEQUENCE SET     O   SELECT pg_catalog.setval('public.detail_shift_id_detail_shift_seq', 14, true);
          public          postgres    false    219            {           0    0    gunung_gunung_id_seq    SEQUENCE SET     B   SELECT pg_catalog.setval('public.gunung_gunung_id_seq', 3, true);
          public          postgres    false    221            |           0    0    kota_kota_id_seq    SEQUENCE SET     >   SELECT pg_catalog.setval('public.kota_kota_id_seq', 4, true);
          public          postgres    false    223            }           0    0    level_level_id_seq    SEQUENCE SET     @   SELECT pg_catalog.setval('public.level_level_id_seq', 5, true);
          public          postgres    false    225            ~           0    0    loket_loket_id_seq    SEQUENCE SET     @   SELECT pg_catalog.setval('public.loket_loket_id_seq', 4, true);
          public          postgres    false    227                       0    0    metode_metode_id_seq    SEQUENCE SET     B   SELECT pg_catalog.setval('public.metode_metode_id_seq', 2, true);
          public          postgres    false    229            �           0    0    pembayaran_pembayaran_id_seq    SEQUENCE SET     J   SELECT pg_catalog.setval('public.pembayaran_pembayaran_id_seq', 2, true);
          public          postgres    false    231            �           0    0    pemesanan_pemesanan_id_seq    SEQUENCE SET     H   SELECT pg_catalog.setval('public.pemesanan_pemesanan_id_seq', 2, true);
          public          postgres    false    233            �           0    0    provinsi_provinsi_id_seq    SEQUENCE SET     F   SELECT pg_catalog.setval('public.provinsi_provinsi_id_seq', 2, true);
          public          postgres    false    235            �           0    0    shift_shift_id_seq    SEQUENCE SET     A   SELECT pg_catalog.setval('public.shift_shift_id_seq', 14, true);
          public          postgres    false    237            �           2606    21928    admin admin_pkey 
   CONSTRAINT     T   ALTER TABLE ONLY public.admin
    ADD CONSTRAINT admin_pkey PRIMARY KEY (admin_id);
 :   ALTER TABLE ONLY public.admin DROP CONSTRAINT admin_pkey;
       public            postgres    false    216            �           2606    21939    customer customer_pkey 
   CONSTRAINT     ]   ALTER TABLE ONLY public.customer
    ADD CONSTRAINT customer_pkey PRIMARY KEY (customer_id);
 @   ALTER TABLE ONLY public.customer DROP CONSTRAINT customer_pkey;
       public            postgres    false    218            �           2606    21949    detail_shift detail_shift_pkey 
   CONSTRAINT     i   ALTER TABLE ONLY public.detail_shift
    ADD CONSTRAINT detail_shift_pkey PRIMARY KEY (id_detail_shift);
 H   ALTER TABLE ONLY public.detail_shift DROP CONSTRAINT detail_shift_pkey;
       public            postgres    false    220            �           2606    21956    gunung gunung_pkey 
   CONSTRAINT     W   ALTER TABLE ONLY public.gunung
    ADD CONSTRAINT gunung_pkey PRIMARY KEY (gunung_id);
 <   ALTER TABLE ONLY public.gunung DROP CONSTRAINT gunung_pkey;
       public            postgres    false    222            �           2606    21963    kota kota_pkey 
   CONSTRAINT     Q   ALTER TABLE ONLY public.kota
    ADD CONSTRAINT kota_pkey PRIMARY KEY (kota_id);
 8   ALTER TABLE ONLY public.kota DROP CONSTRAINT kota_pkey;
       public            postgres    false    224            �           2606    21970    level level_pkey 
   CONSTRAINT     T   ALTER TABLE ONLY public.level
    ADD CONSTRAINT level_pkey PRIMARY KEY (level_id);
 :   ALTER TABLE ONLY public.level DROP CONSTRAINT level_pkey;
       public            postgres    false    226            �           2606    21977    loket loket_pkey 
   CONSTRAINT     T   ALTER TABLE ONLY public.loket
    ADD CONSTRAINT loket_pkey PRIMARY KEY (loket_id);
 :   ALTER TABLE ONLY public.loket DROP CONSTRAINT loket_pkey;
       public            postgres    false    228            �           2606    21984    metode metode_pkey 
   CONSTRAINT     W   ALTER TABLE ONLY public.metode
    ADD CONSTRAINT metode_pkey PRIMARY KEY (metode_id);
 <   ALTER TABLE ONLY public.metode DROP CONSTRAINT metode_pkey;
       public            postgres    false    230            �           2606    21992    pembayaran pembayaran_pkey 
   CONSTRAINT     c   ALTER TABLE ONLY public.pembayaran
    ADD CONSTRAINT pembayaran_pkey PRIMARY KEY (pembayaran_id);
 D   ALTER TABLE ONLY public.pembayaran DROP CONSTRAINT pembayaran_pkey;
       public            postgres    false    232            �           2606    21999    pemesanan pemesanan_pkey 
   CONSTRAINT     `   ALTER TABLE ONLY public.pemesanan
    ADD CONSTRAINT pemesanan_pkey PRIMARY KEY (pemesanan_id);
 B   ALTER TABLE ONLY public.pemesanan DROP CONSTRAINT pemesanan_pkey;
       public            postgres    false    234            �           2606    22006    provinsi provinsi_pkey 
   CONSTRAINT     ]   ALTER TABLE ONLY public.provinsi
    ADD CONSTRAINT provinsi_pkey PRIMARY KEY (provinsi_id);
 @   ALTER TABLE ONLY public.provinsi DROP CONSTRAINT provinsi_pkey;
       public            postgres    false    236            �           2606    22013    shift shift_pkey 
   CONSTRAINT     T   ALTER TABLE ONLY public.shift
    ADD CONSTRAINT shift_pkey PRIMARY KEY (shift_id);
 :   ALTER TABLE ONLY public.shift DROP CONSTRAINT shift_pkey;
       public            postgres    false    238            �           2606    21932    admin telepon_admin 
   CONSTRAINT     Q   ALTER TABLE ONLY public.admin
    ADD CONSTRAINT telepon_admin UNIQUE (telepon);
 =   ALTER TABLE ONLY public.admin DROP CONSTRAINT telepon_admin;
       public            postgres    false    216            �           2606    21930    admin username_admin 
   CONSTRAINT     S   ALTER TABLE ONLY public.admin
    ADD CONSTRAINT username_admin UNIQUE (username);
 >   ALTER TABLE ONLY public.admin DROP CONSTRAINT username_admin;
       public            postgres    false    216            �           1259    21940    nik_customer    INDEX     @   CREATE INDEX nik_customer ON public.customer USING btree (nik);
     DROP INDEX public.nik_customer;
       public            postgres    false    218            �           1259    21985    no_rekening    INDEX     E   CREATE INDEX no_rekening ON public.metode USING btree (no_rekening);
    DROP INDEX public.no_rekening;
       public            postgres    false    230            �           1259    21941    telepon_customer    INDEX     H   CREATE INDEX telepon_customer ON public.customer USING btree (telepon);
 $   DROP INDEX public.telepon_customer;
       public            postgres    false    218            �           1259    21942    username_customer    INDEX     J   CREATE INDEX username_customer ON public.customer USING btree (username);
 %   DROP INDEX public.username_customer;
       public            postgres    false    218            �           2606    22014    customer customer_kota_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.customer
    ADD CONSTRAINT customer_kota_fk FOREIGN KEY (kota_kota_id) REFERENCES public.kota(kota_id);
 C   ALTER TABLE ONLY public.customer DROP CONSTRAINT customer_kota_fk;
       public          postgres    false    224    218    4771            �           2606    22019 "   detail_shift detail_shift_admin_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.detail_shift
    ADD CONSTRAINT detail_shift_admin_fk FOREIGN KEY (admin_admin_id) REFERENCES public.admin(admin_id);
 L   ALTER TABLE ONLY public.detail_shift DROP CONSTRAINT detail_shift_admin_fk;
       public          postgres    false    220    216    4756            �           2606    22024 "   detail_shift detail_shift_shift_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.detail_shift
    ADD CONSTRAINT detail_shift_shift_fk FOREIGN KEY (shift_shift_id) REFERENCES public.shift(shift_id);
 L   ALTER TABLE ONLY public.detail_shift DROP CONSTRAINT detail_shift_shift_fk;
       public          postgres    false    220    238    4786            �           2606    22029    gunung gunung_level_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.gunung
    ADD CONSTRAINT gunung_level_fk FOREIGN KEY (level_level_id) REFERENCES public.level(level_id);
 @   ALTER TABLE ONLY public.gunung DROP CONSTRAINT gunung_level_fk;
       public          postgres    false    226    222    4773            �           2606    22034    kota kota_provinsi_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.kota
    ADD CONSTRAINT kota_provinsi_fk FOREIGN KEY (provinsi_provinsi_id) REFERENCES public.provinsi(provinsi_id);
 ?   ALTER TABLE ONLY public.kota DROP CONSTRAINT kota_provinsi_fk;
       public          postgres    false    224    4784    236            �           2606    22039    loket loket_gunung_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.loket
    ADD CONSTRAINT loket_gunung_fk FOREIGN KEY (gunung_gunung_id) REFERENCES public.gunung(gunung_id);
 ?   ALTER TABLE ONLY public.loket DROP CONSTRAINT loket_gunung_fk;
       public          postgres    false    228    222    4769            �           2606    22044    loket loket_kota_fk    FK CONSTRAINT     {   ALTER TABLE ONLY public.loket
    ADD CONSTRAINT loket_kota_fk FOREIGN KEY (kota_kota_id) REFERENCES public.kota(kota_id);
 =   ALTER TABLE ONLY public.loket DROP CONSTRAINT loket_kota_fk;
       public          postgres    false    228    4771    224            �           2606    22049    pembayaran pembayaran_metode_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.pembayaran
    ADD CONSTRAINT pembayaran_metode_fk FOREIGN KEY (metode_metode_id) REFERENCES public.metode(metode_id);
 I   ALTER TABLE ONLY public.pembayaran DROP CONSTRAINT pembayaran_metode_fk;
       public          postgres    false    4777    230    232            �           2606    22054 "   pembayaran pembayaran_pemesanan_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.pembayaran
    ADD CONSTRAINT pembayaran_pemesanan_fk FOREIGN KEY (pemesanan_pemesanan_id) REFERENCES public.pemesanan(pemesanan_id);
 L   ALTER TABLE ONLY public.pembayaran DROP CONSTRAINT pembayaran_pemesanan_fk;
       public          postgres    false    234    232    4782            �           2606    22059    pemesanan pemesanan_admin_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.pemesanan
    ADD CONSTRAINT pemesanan_admin_fk FOREIGN KEY (admin_admin_id) REFERENCES public.admin(admin_id);
 F   ALTER TABLE ONLY public.pemesanan DROP CONSTRAINT pemesanan_admin_fk;
       public          postgres    false    234    216    4756            �           2606    22064    pemesanan pemesanan_customer_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.pemesanan
    ADD CONSTRAINT pemesanan_customer_fk FOREIGN KEY (customer_customer_id) REFERENCES public.customer(customer_id);
 I   ALTER TABLE ONLY public.pemesanan DROP CONSTRAINT pemesanan_customer_fk;
       public          postgres    false    234    218    4762            �           2606    22069    pemesanan pemesanan_gunung_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.pemesanan
    ADD CONSTRAINT pemesanan_gunung_fk FOREIGN KEY (gunung_gunung_id) REFERENCES public.gunung(gunung_id);
 G   ALTER TABLE ONLY public.pemesanan DROP CONSTRAINT pemesanan_gunung_fk;
       public          postgres    false    4769    234    222            O   �  x�E�͒�0 �sx
�1�p�A��UP���Kk@�4�Qx�uv�ڪ��|�]MВ
��Ie{�����U���'
�n@�`2w��S�����k#q��U�:Q|�e�OM"��)�Gr�IR�-��5���hf�K��N���=6��n/Y��ڻ{����[w)��Y�:k�������inߓ�7��G�k�O�]�^~�����Ú�����ʾ@O�� �P�NPqM�/���l��?]��t��1�8�}��NbE�p6������a+�[��}���6B��L�+},y��GU�'S+ᨫ̰N!�XC�%�v�Y�Y-ELR�.��K�X�^��dٞ���a[�Q��I�>f\�K`  � �ә�LP|,o�Zș��Ѷ��H���H�>�u�Z[�:�>�h�3}����lGsP��R1U>���Mϱ�~@�A�G��v�g��_'�{�L�C��v(����\v�x6�J��r�"���k��/��C�߆�i �^      Q     x�5λn�0��<�V��6�dLKM�%-�.�����A�&O_Ө����>�R��L?)�(3k�8
����  � ���"���������z��p~&���^�[䲛K�M�ُڧ\�����X]��]�I�3^�8a:�|n�8�h{�c��j5��qa�(�����q�	�ڨ��*����=���fޫ�O&�U���?��%QP/���Y��\]q)���uc�z��n���մ]z�Q�}�� �|�q~�SH      S   D   x����0�3SLdl�K/鿎�5�'�,ӕJL%^%Vt���=���-�]s�:p�u��ē�~d��      U   F   x�3����J���4672�44 Nc.#����ԢRNc3s3N#S��1�SQ~n>����%�1X�!W� J��      W   @   x�3����M��V��--�4�2��)�M�J�K�4�2��Ḿ0M8���s2�����=... :"@      Y   '  x��RIN�0<�W�F��~��#�R���ȋ�������0���۵u��޸~ ��І$��	�SVRp��Nhr�b9���y�s��>h�>"e�z9*�.`�%$ġh�#*���#�$dW�@E��fE�y����JG)�e���!����O��2�9�iyC����f��M�Z�̍G������6��u�/�B�^QG�3�Mi�C��O[�R/���j��@I#Z�t[?יwsJ~�ڂ�Rk��dd��Dh�����<�-��I�!Ei�<i/�N����Ŧ�eږqkޭ1��~�B      [   "   x�3�4�4�2�B.cNc i�i�i����� 4su      ]   T   x�3�)J�+NK-Rprv䴰44204255��L��LU��I�*-��SN�+�/��2�tI�K�4�042�00�020ǩ6F��� ���      _   <   x�3�46 ΀��Τ��LC���tNCNC.#NsS�\j^J&P,m�6�4����� ��      a   /   x�3�4202�50�50�3�89�A��.h��72��b���� �I
�      c   -   x�3��+-NTI�KOO,JTp%\F�^��@����"�=... ��      e   �   x���=
�0��Y����8���uj!K�@풂[�}�u�D_4�A�JHY��ڳ����9�Ļ�#����k_�����aB&�-��i�� ����M��$P밝���4dp,�]�b_I)�a��saC����>7^���9� �ǒC     