import sqlite3

def init_db():
    conn = sqlite3.connect("cyber_university.db")
    cursor = conn.cursor()
    
    # Sınav formatına tam uyumlu Ogrenci Tablosu (3 Sütun)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Ogrenci (
        OgrenciID INT PRIMARY KEY,
        Ad VARCHAR(30) NOT NULL,
        Sinif INT CHECK (Sinif IN (1, 2))
    );
    """)
    
    # DersKaydi Tablosu
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS DersKaydi (
        KayitID INT PRIMARY KEY,
        OgrenciID INT NOT NULL,
        DersKodu VARCHAR(10) NOT NULL,
        Puan INT CHECK (Puan BETWEEN 0 AND 100),
        FOREIGN KEY (OgrenciID) REFERENCES Ogrenci(OgrenciID)
    );
    """)
    
    # Örnek Lab Verileri
    cursor.executemany("INSERT OR IGNORE INTO Ogrenci VALUES (?, ?, ?);", [
        (1, 'Kadir', 2),
        (2, 'Murat', 1),
        (3, 'Elif', 2)
    ])
    
    cursor.executemany("INSERT OR IGNORE INTO DersKaydi VALUES (?, ?, ?, ?);", [
        (101, 1, 'BGT006', 95),
        (102, 1, 'BGT002', 88),
        (103, 2, 'BGT006', 45)
    ])
    
    conn.commit()
    conn.close()
    print("[+] Lab veritabanı başarıyla oluşturuldu ve tablolar yüklendi.")

if __name__ == "__main__":
    init_db()
