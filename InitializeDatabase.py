from Database import execute_query
# === Buat Database ===
def createUser():
    query = '''
    CREATE TABLE [User] (
        id_User int PRIMARY KEY, 
        username varchar(50), 
        password varchar(20), 
        nama varchar(60), 
        alamat varchar(100), 
        no_telepon varchar(13), 
        email varchar(320), 
        role varchar(7)
    )
    '''
    return "Database User berhasil dibuat." if execute_query(query) else "Database User gagal dibuat."

def createKlien():
    query = '''
    CREATE TABLE Klien (
        id_Klien int PRIMARY KEY, 
        nama varchar(60), 
        alamat varchar(100), 
        no_telepon varchar(13), 
        email varchar(320), 
        tanggal_registrasi date
    )
    '''
    return "Database Klien berhasil dibuat." if execute_query(query) else "Database Klien gagal dibuat."

def createEvent():
    query = '''
    CREATE TABLE Event (
        id_Event int PRIMARY KEY, 
        nama varchar(60),
        jenis_event varchar(20), 
        tanggal_event date, 
        jumlah_undangan int, 
        lokasi varchar(100), 
        status_event varchar(50), 
        total_budget money, 
        id_Klien int FOREIGN KEY REFERENCES Klien(id_Klien)
    )
    '''
    return "Database Event berhasil dibuat." if execute_query(query) else "Database Event gagal dibuat."

def alterKlien():
    query = '''
    ALTER TABLE 
        Event 
    ADD CONSTRAINT 
        [fk_klien] 
    FOREIGN KEY(id_Klien) REFERENCES Klien(id_Klien)
    '''
    return "Database Klien berhasil dialter." if execute_query(query) else "Database Klien gagal dialter."

def createVendor():
    query = '''
    CREATE TABLE Vendor (
        id_Vendor int PRIMARY KEY, 
        nama varchar(20), 
        nama_pemilik varchar(60), 
        alamat varchar(100), 
        no_telepon varchar(13), 
        email varchar(320), 
        harga_min money,
        harga_max money, 
        jenis_vendor varchar(20)
    )
    '''
    return "Database Vendor berhasil dibuat." if execute_query(query) else "Database Vendor gagal dibuat."

def createEventVendor():
    query = '''
    CREATE TABLE EventVendor (
        id_Event int, 
        id_Vendor int, 
        harga_dealing money,
        PRIMARY KEY (id_Event, id_Vendor), 
        FOREIGN KEY (id_Event) REFERENCES Event(id_Event), 
        FOREIGN KEY (id_Vendor) REFERENCES Vendor(id_Vendor)
    )
    '''
    return "Database EventVendor berhasil dibuat." if execute_query(query) else "Database EventVendor gagal dibuat."

def createUserEvent():
    query = '''
    CREATE TABLE UserEvent (
        id_User int, 
        id_Event int, 
        PRIMARY KEY (id_User, id_Event), 
        FOREIGN KEY (id_User) REFERENCES [User](id_User), 
        FOREIGN KEY (id_Event) REFERENCES Event(id_Event)
    )
    '''
    return "Database UserEvent berhasil dibuat." if execute_query(query) else "Database UserEvent gagal dibuat."

# === Insert Data Dummy ke Database ===
def insertOwner():
    query = '''
    INSERT INTO 
        [User] 
    VALUES 
        (1, 'ownerKapi', 'ownerKapi01', 'Kapi', 'Jalan Ciumbuleuit No. 94', '08123456789', 'kapi@gmail.com', 'pemilik')
    '''
    return "Owner berhasil dimasukkan." if execute_query(query) else "Owner gagal dimasukkan."

def insertAsisten():
    query = '''
    INSERT INTO 
        [User] 
    VALUES 
        (2, 'asDodo', 'asDodo01', 'Dodo', 'Jalan Ciumbuleuit No. 91', '082345678910', 'dodo@gmail.com', 'asisten'),
        (3, 'asWombat', 'asWombat01', 'Wombat', 'Jalan Ciumbuleuit No. 92', '0834567891011', 'wombat@gmail.com', 'asisten'),
        (4, 'asWovey', 'asWovey01', 'Wovey', 'Jalan Ciumbuleuit No. 93', '0845678910111', 'wovey@gmail.com', 'asisten')
    '''
    return "Asisten berhasil dimasukkan." if execute_query(query) else "Asisten gagal dimasukkan."

def insertKlien():
    query = '''
    INSERT INTO 
        Klien 
    VALUES
        (1, 'Andi Saputra', 'Jl. Merdeka No. 10', '081234567890', 'andi@email.com', '2024-01-15'),
        (2, 'Rina Lestari', 'Jl. Mawar No. 7', '082345678901', 'rina@email.com', '2024-02-20'),
        (3, 'Dewi Anggraini', 'Jl. Melati No. 5', '083456789012', 'dewi@email.com', '2024-03-05')
    '''
    return "Klien berhasil dimasukkan." if execute_query(query) else "Klien gagal dimasukkan."

def insertEvent():
    query = '''
    INSERT INTO 
        Event 
    VALUES
        (1, 'Andi & Suzy Wedding', 'Pernikahan', '2024-06-10', 200, 'Hotel Mulia', 'upcoming', 50000000, 1),
        (2, 'Rina Sweet Seventeen', 'Ulang Tahun', '2024-05-01', 50, 'Cafe Ceria', 'completed', 10000000, 2),
        (3, 'Data Integrity & Security Talkshow', 'Seminar', '2024-07-15', 100, 'Auditorium UI', 'upcoming', 20000000, 3)
    '''
    return "Event berhasil dimasukkan." if execute_query(query) else "Event gagal dimasukkan."

def insertVendor():
    query = '''
    INSERT INTO 
        Vendor 
    VALUES
        (1, 'Katering Enak', 'Bu Sari', 'Jl. Nangka No. 9', '081112223333', 'sari@katering.com', 5000000, 15000000, 'Katering'),
        (2, 'Dekor Mewah', 'Pak Budi', 'Jl. Melon No. 12', '082223334444', 'budi@dekor.com', 3000000, 12000000, 'Dekorasi'),
        (3, 'MC Ceria', 'Dino', 'Jl. Salak No. 3', '083334445555', 'dino@mc.com', 1000000, 5000000, 'MC'),
        (4, 'Sound Pro', 'Nina', 'Jl. Rambutan No. 4', '084445556666', 'nina@sound.com', 2000000, 8000000, 'Sound System')
    '''
    return "Vendor berhasil dimasukkan." if execute_query(query) else "Vendor gagal dimasukkan."

def insertEventVendor():
    query = '''
    INSERT INTO 
        EventVendor 
    VALUES
        (1, 1, 10000000),  -- Katering Enak untuk Pernikahan
        (1, 2, 8000000),   -- Dekor Mewah untuk Pernikahan
        (1, 3, 2000000),   -- MC Ceria untuk Pernikahan
        (2, 2, 4000000),   -- Dekor Mewah untuk Ulang Tahun
        (3, 4, 5000000)   -- Sound Pro untuk Seminar
    '''
    return "EventVendor berhasil dimasukkan." if execute_query(query) else "EventVendor gagal dimasukkan."

def insertUserEvent():
    query = '''
    INSERT INTO 
        UserEvent
    VALUES
        (2, 1),
        (3, 2),
        (4, 3)
    '''
    return "UserEvent berhasil dimasukkan." if execute_query(query) else "UserEvent gagal dimasukkan."

if __name__ == "__main__":
    print(createUser())
    print(createKlien())
    print(createEvent())
    print(createVendor())
    print(createEventVendor())
    print(createUserEvent())

    print(insertOwner())
    print(insertAsisten())
    print(insertKlien())
    print(insertEvent())
    print(alterKlien())
    print(insertVendor())
    print(insertEventVendor())
    print(insertUserEvent())